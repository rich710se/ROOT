#!/bin/bash
PR=$1

if (( EUID != 0 )); then
    echo "Error: This must be run as root (with sudo)."
    exit 1
fi

if [[ -z "$PR" ]]; then
    echo "Error: Missing PR argument."
    echo ""
    echo "Run: bash test_pr.sh PRNUMBER"
    exit 1
fi
git clone https://github.com/home-assistant/hassbian-scripts.git hassbian_config_install
cd hassbian_config_install || exit 1
git fetch origin +refs/pull/"$PR"/merge
git checkout FETCH_HEAD

chmod 755 -R package
dpkg-deb --build package/
apt install -y ./package.deb --reinstall --allow-downgrades

cd || exit 1
rm -r hassbian_config_install
