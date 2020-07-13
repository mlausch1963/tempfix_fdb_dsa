# Fix for >300s unresponsivnes on turris omnia 4.0+ when wifi client move from lan port to wifi.

# Installation

Cloned repo need to be located in /root/tempfix_fdb_dsa

```
git clone https://github.com/stanojr/tempfix_fdb_dsa.git
chmod 755 tempfix_fdb_dsa/tempfix*
cp tempfix_fdb_dsa/tempfix_fdb_dsa /etc/init.d/tempfix_fdb_dsa
/etc/init.d/tempfix_fdb_dsa start
/etc/init.d/tempfix_fdb_dsa enable
```

