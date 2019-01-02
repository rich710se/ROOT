"""Update dependecies for add-ons in the community add-on project."""
from alpinepkgs.packages import get_package
from github import Github

TOKEN = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
COMMIT_MSG = ':arrow_up: Upgrades {} to version {}'
GH = Github(TOKEN)
REPO = "{}/{}"
ORG = 'hassio-addons'

ADDONS = [
    {
        'repo': 'addon-magicmirror',
        'addon_name': 'magicmirror'
    }
]


def commit(org, repo, path, msg, content, sha):
    """Commit changes."""
    repository = "{}/{}".format(org, repo)
    ghrepo = GH.get_repo(repository)
    print(ghrepo.update_file(path, msg, content, sha))


def get_file_obj(org, repo, file):
    """Return the file object."""
    repository = "{}/{}".format(org, repo)
    ghrepo = GH.get_repo(repository)
    obj = ghrepo.get_contents(file)
    return obj


def get_file_content(obj):
    """Return the content of the file."""
    return obj.decoded_content.decode()


def get_apk_packages_with_updates(addons):
    """Return JSON with upgradable packages.
    addons should be like this:
    [
        {
            'repo': 'addon-mqtt',
            'addon_name': 'mqtt'
        }
    ]
    """
    for addon in addons:
        addon_data = {}
        repo = addon['repo']
        repository = REPO.format(ORG, repo)
        print('Checking for apk uppdates for', repository)
        file_path = "{}/Dockerfile".format(addon['addon_name'])
        remote_file = get_file_obj(ORG, repo, file_path)
        masterfile = get_file_content(remote_file)
        run = masterfile.split('RUN')[1].split('LABEL')[0]
        packages = []
        updates = []
        if 'apk' in run:
            cmds = run.split('&&')
            for cmd in cmds:
                if 'apk add' in cmd:
                    all_apk_lines = cmd.replace(' ', '').split('\\\n')
                    for pkg in all_apk_lines:
                        if '=' in pkg:
                            if '@legacy' in pkg:
                                package = pkg.split('@')[0]
                                branch = 'v3.7'
                            elif '@edge' in pkg:
                                package = pkg.split('@')[0]
                                branch = 'edge'
                            else:
                                package = pkg.split('=')[0]
                                branch = 'v3.8'
                            version = pkg.split('=')[1]

                            this = {'package': package,
                                    'branch': branch,
                                    'version': version,
                                    'search_string': pkg}

                            packages.append(this)

        for pkg in packages:
            if 'apkadd--no-cache' in pkg['package']:
                pack = pkg['package'].replace('apkadd--no-cache', "")
            else:
                pack = pkg['package']
            data = get_package(pack, pkg['branch'])
            package = data['package']
            version = data['x86_64']['version']
            if version != pkg['version']:
                this = {'package': package,
                        'version': version,
                        'source': 'apk',
                        'search_string': pkg['search_string']}
                updates.append(this)
        if updates:
            addon_data[addon['addon_name']] = {}
            addon_data[addon['addon_name']]['repo'] = addon['repo']
            addon_data[addon['addon_name']]['addon_name'] = addon['addon_name']
            addon_data[addon['addon_name']]['updates'] = updates
    return addon_data


def update_remote_dockerfile(addon_data):
    """Update the remote dockerfile."""
    for addon in addon_data:
        repo = addon_data[addon]['repo']
        print("Starting upgrades for " + ORG + "/" + repo)
        for package in addon_data[addon]['updates']:
            msg = COMMIT_MSG.format(package['package'], package['version'])

            file_path = "{}/Dockerfile".format(addon_data[addon]['addon_name'])
            remote_file = get_file_obj(ORG, repo, file_path)

            search_string_dict = package['search_string'].split('=')
            replace_string = search_string_dict[0] + '=' + package['version']

            new_content = get_file_content(remote_file)
            new_content = new_content.replace(package['search_string'],
                                              replace_string)
            print(msg)
            commit(ORG, repo, file_path, msg, new_content, remote_file.sha)


ADDON_DATA = get_apk_packages_with_updates(ADDONS)
update_remote_dockerfile(ADDON_DATA)
