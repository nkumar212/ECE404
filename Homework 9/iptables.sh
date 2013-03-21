#! /bin/bash



iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT
iptables -A INPUT -p tcp --src engineering.purdue.edu --destination-port 22 -j ACCEPT
iptables -A INPUT -p tcp --destination-port 113 -j ACCEPT
iptables -A INPUT -p tcp --src 20.10.4.56 --destination-port 80 -j ACCEPT
iptables -A INPUT -j REJECT


