#!/bin/bash
# Author: Joakim Sørensen @ludeeus
#
# usage: nuke_topics.sh [broker] [user] [password]
# example: bash nuke_topics.sh 192.168.1.13 mqtt PassW0rd!

host=$1
username=$2
password=$3

topics=$(mosquitto_sub -h $host -u $username -P $password  -t '#' -v --retained-only -W 10)
for topic in $topics; do
  mosquitto_pub -h $host -t $topic -r -n -u $username -P $password
done
