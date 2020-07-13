#!/usr/bin/env python3

import os
import subprocess
import re

# bridge name to monitor with lan interfaces
bridge_iface = 'br-lan'

# monitor all new fdb entries in these ifaces
watch_ifaces = ['wlan0', 'wlan1']

# after new entry is found in watch_ifaces, remove them from these port(s) (string appended to bridge cmd show/del)
# if you change vlan id,also change it in rec_port below
switch_ports = [
                  ['dev','lan1','vlan', '1', 'self'],
               ]

rec = re.compile('(([0-9a-fA-F]:?){12}) dev ([a-z0-9-]+) master %s' % (bridge_iface))
rec_port = re.compile('([0-9a-fA-F]:?){12} vlan 1 self')

print("start monitoring fdb", flush=True)
proc = subprocess.Popen(['/usr/sbin/bridge','monitor', 'fdb'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, close_fds=True)
while True:
  stdout_line = proc.stdout.readline()
  stderr_line = proc.stdout.readline()
  if not stdout_line and not stderr_line:
    break

  line = stderr_line.rstrip()
  if (line.startswith('Deleted')):
    continue

  m = rec.match(line)
  if not m:
    continue
  else:
    mac = m.group(1)
    iface = m.group(3)

    if iface in watch_ifaces:
      for switch_port in switch_ports:
        proc_port = subprocess.run(['/usr/sbin/bridge', 'fdb', 'show', 'br', bridge_iface, *switch_port],
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,  close_fds = True)

        for line_port in proc_port.stdout.decode().split('\n'):
          if line_port == '': break
          rec_port.match(line_port)
          if (rec_port):
            print("found mac: {} on iface: {}, deleting fdb from {}".format(mac, iface, (*switch_port)), flush=True)
            proc_delentry = subprocess.run(["/usr/sbin/bridge", "fdb", "del", mac, *switch_port], close_fds=True)
