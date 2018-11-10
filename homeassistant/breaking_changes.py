"""Create breaking_change list for HA."""
import json
import requests

CURRENT_JSON = 'https://raw.githubusercontent.com/ludeeus/ROOT/master/homeassistant/breaking_changes.json'

HA_URLS = ['https://www.home-assistant.io/blog/2018/05/27/release-70',
           'https://www.home-assistant.io/blog/2018/06/08/release-71',
           'https://www.home-assistant.io/blog/2018/06/22/release-72',
           'https://www.home-assistant.io/blog/2018/07/06/release-73',
           'https://www.home-assistant.io/blog/2018/07/20/release-74',
           'https://www.home-assistant.io/blog/2018/08/03/release-75',
           'https://www.home-assistant.io/blog/2018/08/17/release-76',
           'https://www.home-assistant.io/blog/2018/08/29/release-77',
           'https://www.home-assistant.io/blog/2018/09/17/release-78',
           'https://www.home-assistant.io/blog/2018/09/28/release-79',
           'https://www.home-assistant.io/blog/2018/10/12/release-80',
           'https://www.home-assistant.io/blog/2018/10/26/release-81',
           'https://www.home-assistant.io/blog/2018/11/09/release-82']
NEW_JSON = []
BASE_JSON = requests.get(CURRENT_JSON).json()
for HA_URL in HA_URLS:
    HA_VERSION = "0.{}.x".format(HA_URL[-2:])
    VERSION_EXIST = False
    for version in BASE_JSON:
        if HA_VERSION == version['version']:
            VERSION_EXIST = True
        #old = {}
        #old['version'] = version['version']
        #old['data'] = version['data']
        #NEW_JSON.append(old)
    if not VERSION_EXIST:
        NEW_VERSION = requests.get(HA_URL).text.split('\n')
        RAW_CHANGES = []
        ADD = {}
        ADD['version'] = HA_VERSION
        ADD['data'] = []
        CONTROL = []
        for line in NEW_VERSION:
            if "(breaking change)" in line:
                RAW_CHANGES.append(line)
        for change in RAW_CHANGES:
            try:
                PR = {}
                pr = str(change).split('home-assistant/home-assistant/pull/')[1].split('"')[0]
                if pr not in CONTROL:
                    prlink = 'https://github.com/home-assistant/home-assistant/pull/{}'.format(pr)
                    component = str(change).split('(<a href="/components/')[1].split('/">')[0]
                    doclink = 'https://www.home-assistant.io/components/{}'.format(component)
                    description = str(change).split('  <li>')[1].split('(<a ')[0].replace('</code>','').replace('<code class="highlighter-rouge">','').replace('\u2019','`').replace('\u201c','').replace('\u201d','')
                    PR['pr'] = pr
                    PR['prlink'] = prlink
                    PR['component'] = component
                    PR['doclink'] = doclink
                    PR['description'] = description
                    ADD['data'].append(PR)
                    CONTROL.append(pr)
            except:
                print("Something wrong happend...")
        NEW_JSON.append(ADD)
with open('breaking_changes.json', 'w') as file:
    json.dump(NEW_JSON, file, sort_keys=True, indent=4, ensure_ascii=True)
file.close()
