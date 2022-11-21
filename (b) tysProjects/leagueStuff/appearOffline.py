import os

os.system('cmd /k "netsh advfirewall firewall add rule name=”lolchat” dir=out remoteip=192.64.174.69 protocol=TCP '
          'action=block"')
