#!/usr/bin/python3
import os

if os.geteuid() != 0:
  exit("[*] ERROR: Permission denied\n[*] Please try again, using 'sudo python3 install.py'\n")


print("[*] Installing mkd3...")
os.system("sudo apt-get install mdk3")

print("[*] Installing macchanger...")
os.system("sudo apt-get install macchanger")

print("[*] Installing python requirements...")
os.system("pip3 install -r requirements.txt")

print("[!] Done")
