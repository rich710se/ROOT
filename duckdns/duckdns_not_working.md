# _DuckDNS is not working_

_/rant\_start_

This statement is **FALSE**..

I have seen that statement multiple times and **never** has that been the case.

DuckDNS is like a phonebook, it has **one** job and that is to assign a subdomain name to an IP,

If `my-ha-domain.duckdns.org` resolves to your IP then DuckDNS **is** working and you should check elsewwhere.

Verify this with `nslookup` on Windows or a webservice like https://network-tools.com/nslook/


nslookup:

```shell
C:\Users\user>nslookup my-ha-domain.duckdns.org
Server:  a0d7b954-pi-hole
Address:  192.168.2.200

Non-authoritative answer:
Name:    my-ha-domain.duckdns.org
Address:  127.0.0.1
```

_/rant\_end_