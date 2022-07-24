#!/usr/bin/python3
import os, sys

if os.geteuid() != 0:
  exit("[*] ERROR: Permission denied\n[*] Please try again, using 'sudo python3 install.py'\n")

print(""""
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#   Unbekannt Framwork 6.0 Installer          #
#                                             #
#   Github:    github.com/i-am-unbekannt      #
#   Instagram: instagram.com/i_am_unbekannt   #
#   Flowcode:  flowcode.com/page/unbekannt    #
#                                             #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
""")

ans = input("[*] Start Installing? [y/n] ")
if ans == "n":
  sys.exit()

if ans == "y":
  print("<================================>\n[*] Installing mkd3...\n<================================>")
  os.system("sudo apt-get install mdk3")

  print("<================================>\n[*] Installing macchanger...\n<================================>")
  os.system("sudo apt-get install macchanger")

  print("<================================>\n[*] Installing python requirements...\n<================================>")
  os.system("pip3 install -r requirements.txt")

  print("\n\n[*] Done!\n[*] Starting Unbekannt Framework...")
  os.system("sudo python3 Unbekannt.py")
