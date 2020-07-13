# Fix for >300s unresponsivnes on turris omnia 4.0+ when wifi client move from lan port to wifi.
This soft will manualy remove fdb entry from specified lan port(s) when they appear on wifi.

# Installation

Cloned repo need to be located in /root/tempfix_fdb_dsa

```
git clone https://github.com/stanojr/tempfix_fdb_dsa.git
chmod 755 tempfix_fdb_dsa/tempfix*
cp tempfix_fdb_dsa/tempfix_fdb_dsa /etc/init.d/tempfix_fdb_dsa
# you can specify ports of secondary APs/switch in tempfix_fdb_dsa/tempfix_fdb_dsa.py
# default is lan1
/etc/init.d/tempfix_fdb_dsa start
/etc/init.d/tempfix_fdb_dsa enable
```

