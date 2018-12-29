#!/bin/bash
# This script will install hassbian-config on the unit.
#

if [ "$(id -u)" != "0" ]; then
echo "This script must be run with sudo. Use \"sudo ${0} ${*}\"" 1>&2
exit 1
fi

echo "Updating distro..."
apt update
apt upgrade -y
apt dist-upgrade

echo "Installing additional software..."
apt-get install -y git python3 curl python3-venv python3-pip bluetooth libbluetooth-dev rng-tools htop tmux avahi-daemon libtool autoconf rfkill apt-transport-https
pip3 install --upgrade virtualenv

echo "Adding homeassistant user and install dir..."
addgroup homeassistant
useradd -u 1001 -g homeassistant -rm homeassistant
mkdir /srv/homeassistant
chown homeassistant:homeassistant -R /srv/homeassistant
chown homeassistant:homeassistant -R /home/homeassistant
usermod -G dialout -a homeassistant
usermod -G i2c -a homeassistant
usermod -G gpio -a homeassistant
usermod -G spi -a homeassistant

echo "Downloading and installing hassbian-config..."
echo "deb [trusted=yes] https://gitlab.com/hassbian/repository/raw/master stretch main" | sudo tee /etc/apt/sources.list.d/hassbian-config.list
apt-get update
apt install -y hassbian-scripts

echo "Installation complete..."