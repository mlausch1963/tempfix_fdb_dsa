# Fix for >300s unresponsivnes on turris omnia 4.0+ when wifi client move from lan port to wifi.

# Installation

```
root@turris:~# git clone https://github.com/stanojr/tempfix_fdb_dsa.git
root@turris:~# chmod 755 tempfix_fdb_dsa/*
root@turris:~# cp tempfix_fdb_dsa /etc/init.d/tempfix_fdb_dsa
root@turris:~# /etc/init.d/tempfix_fdb_dsa start
root@turris:~# /etc/init.d/tempfix_fdb_dsa enable
```

