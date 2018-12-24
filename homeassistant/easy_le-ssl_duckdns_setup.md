#!/bin/bash
#Author: Joakim Sørensen @ludeeus
#
# This script uses LE's dns challange to verify the domain, this means that you do not need to open any additional ports.
# Only run this on the client that is running homeassistant.
# You need to know your DuckDNS subdomain, and token. 
#
# This script will add 2 cronjobs to the user running homeassistant, so duckdns and certs are auto updated.
# 
# To run this paste these lines on the client:
# wget -q https://gitlab.com/ludeeus/toolbox/raw/master/homeassistant/auto_duckdns_and_le-cert.sh
# sudo bash auto_duckdns_and_le-cert.sh

if (( EUID != 0 )); then
    echo "Error: must be run as root (with sudo) for this to be possible"
    exit 1
fi

getrunning=$( ps -ef | grep bin/hass | wc -l)
if [ $getrunning == "1" ]; then
	echo "homeassistant not found.."
	echo -n "enter the username that is running homeassistant: "
	read -r hauser
	if [ ! "$hauser" ]; then
		exit
	fi

else
	getuser=$(ps -ef | grep bin/hass | head -1 | awk -F'  ' '{print $1}')
	if [[ $getuser = *"+"* ]]; then
		getuser=${getuser::-1}
	fi
	hauser=$(cut -d: -f1 /etc/passwd | grep $getuser)
    echo "found user $hauser running homeassistant.."
fi

echo "Enter your duckdns subdomain:"
echo "(if your domain is 'example.duckdns.org' type example)"
echo -n "subdomain: "
read -r domain
if [ ! "$domain" ]; then
    exit
fi
if [[ $domain = *"duckdns"* ]]; then
    domain=$(echo "$domain" | cut -d\. -f1)
fi
if [[ $domain = *"//"* ]]; then
    domain=$(echo "$domain" | cut -d/ -f3)
fi


echo -n "DuckDNS token: "
read -r token
echo
if [ ! "$token" ]; then
    exit
fi
echo -n "Do you want to generate certificates to use SSL(https)? [N/y] : "
read -r SSL_RESPONSE

echo "Changing to homeassistant user..."
sudo -u $hauser -H /bin/bash << EOF
cd

if [ "$SSL_RESPONSE" == "y" ] || [ "$SSL_RESPONSE" == "Y" ]; then
    git clone https://github.com/lukas2511/dehydrated.git
    cd dehydrated  || exit
    echo $domain".duckdns.org" | tee domains.txt
    echo "CHALLENGETYPE='dns-01'" | tee -a config
    echo "HOOK='./hook.sh'" | tee -a config
    curl -so ./hook.sh https://raw.githubusercontent.com/home-assistant/hassbian-scripts/dev/package/opt/hassbian/suites/files/ssl_hook.sh
    sed -i 's/myhome/'$domain'/g' ./hook.sh
    sed -i 's/your-duckdns-token/'$token'/g' ./hook.sh
    chmod 755 hook.sh
    ./dehydrated --register  --accept-terms
    ./dehydrated -c
fi

echo "Creating duckdns folder..."
cd /home/$hauser || exit
mkdir duckdns
cd duckdns || exit

echo "Creating a script file to be used by cron."
echo "echo url='https://www.duckdns.org/update?domains=$domain&token=$token&ip=' | curl -k -o ~/duckdns/duck.log -K -" > duck.sh

echo "Setting premissions..."
chmod 700 duck.sh

echo "Creating cron job..."
(crontab -l ; echo "*/5 * * * * /home/$hauser/duckdns/duck.sh >/dev/null 2>&1")| crontab -
if [ "$SSL_RESPONSE" == "y" ] || [ "$SSL_RESPONSE" == "Y" ]; then
    (crontab -l ; echo "0 1 1 * * cd /home/$hauser/dehydrated && ./dehydrated -c")| crontab -
fi

echo "Changing to root user..."
EOF

echo "Restarting cron service..."
sudo systemctl restart cron.service

echo "Checking the installation..."
if [ "$SSL_RESPONSE" == "y" ] || [ "$SSL_RESPONSE" == "Y" ]; then
    certvalidation=$(find /home/$hauser/dehydrated/certs/"$domain".duckdns.org/ -maxdepth 1 -type f | sort | grep privkey)
else
    certvalidation="ok"
fi
if [ ! -f /home/$hauser/duckdns/duck.sh ]; then
    dnsvalidation=""
else
    dnsvalidation="ok"
fi

if [ ! -z "${certvalidation}" ] && [ ! -z "${dnsvalidation}" ]; then
    echo
    echo -e "\\e[32mInstallation done..\\e[0m"
    echo
    if [ "$SSL_RESPONSE" == "y" ] || [ "$SSL_RESPONSE" == "Y" ]; then
        echo "Remember to update your configuration.yaml to take advantage of SSL!"
        echo "Documentation for this can be found here <https://home-assistant.io/components/http/>."
        echo "your certs are located here: /home/$hauser/dehydrated/certs/"$domain".duckdns.org/"
        echo
    fi
else
    echo
    echo -e "\\e[31mInstallation failed..."
    echo
    exit 1
fi
exit 0