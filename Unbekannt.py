#!/usr/bin/python3
import time
import sys
import os

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#   Unbekannt Framwork 6.0                    #
#                                             #
#   Github:    github.com/i-am-unbekannt      #
#   Instagram: instagram.com/i_am_unbekannt   #
#   Site:      i-am-unbekannt.github.io       #
#                                             #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

try:
	from colorama import Fore, init
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: colorama\n[*] Try: pip3 install colorama")
	sys.exit()
	
try:
	import webbrowser
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: webbrowser\n[*] Try: pip3 install webbrowser")
	sys.exit()
	
try:
	from termcolor import colored
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: termcolor\n[*] Try: pip3 install tercolor")
	sys.exit()
	
try:
	from tcping import Ping
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: tcping\n[*] Try: pip3 install tcping")
	sys.exit()
	
try:
	import urllib.request
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: urllib\n[*] Try: pip3 install urllib")
	sys.exit()
	
try:
	import subprocess
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: subprocess\n[*] Try: pip3 install subprocess")
	sys.exit()
	
try:
	from pathlib import Path
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: pathlib\n[*] Try: pip3 install pathlib")
	sys.exit()

try:
	import socket
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: socket\n[*] Try: pip3 install socket")
	sys.exit()

try:
	import requests
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: requests\n[*] Try: pip3 install requests")
	sys.exit()
	
try:
	import json
except ModuleNotFoundError:
	print("\n[*] ModuleNotFoundError: json\n[*] Try: pip3 install json")
	sys.exit()
	
init()
R = Fore.LIGHTRED_EX
Y = Fore.YELLOW
G = Fore.LIGHTGREEN_EX
M = Fore.MAGENTA
W = Fore.WHITE
B = Fore.LIGHTBLUE_EX
path_to_ew = 'libreq/Evil-Win.py'
pathEW = Path(path_to_ew)
path_to_de = 'libreq/deauther.sh'
pathDE = Path(path_to_de)
path_to_cl = 'libreq/client.exe'
pathCL = Path(path_to_cl)
path_to_be = 'libreq/beacon.py'
pathBE = Path(path_to_be)

def load_animation():
	print()
	load_str = "starting the unbekannt framework console..."
	ls_len = len(load_str)
	animation = "|/-\\"
	anicount = 0
	counttime = 0		
	i = 0					

	while (counttime != 100):
		time.sleep(0.075)
		load_str_list = list(load_str)
		x = ord(load_str_list[i])
		y = 0							
		if x != 32 and x != 46:			
			if x>90:
				y = x-32
			else:
				y = x + 32
			load_str_list[i]= chr(y)
		res =''			
		for j in range(ls_len):
			res = res + load_str_list[j]
		sys.stdout.write(B+"\r"+"[*] "+W+res + animation[anicount])
		sys.stdout.flush()
		load_str = res
		anicount = (anicount + 1)% 4
		i =(i + 1)% ls_len
		counttime = counttime + 1
load_animation()

def main():
	def mainscreen():
		os.system('cls' if os.name == 'nt' else 'clear')
		print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

		''')

		def ansinput():
			ans = input(R+'['+ colored('unbekannt', 'white', attrs=['underline']) +R+']'+W+'~: ')
			if ans == "req":
				try:
					os.system("clear")
					def sudo():
						try:
							if os.geteuid() != 0:
								return True		
						except:
								return False
					def connect(host='http://google.com'):
						try:
							urllib.request.urlopen(host) #Python 3.x
							return True
						except:
							return False
					def libreqevil():
						try:
							if pathEW.is_file():
								return True
						except:
								return False
					def libreqdeauther():
						try:
							if pathDE.is_file():
								return True
						except:
								return False
					def libreqclient():
						try:
							if pathCL.is_file():
								return True
						except:
								return False
					def libreqbeacon():
						try:
							if pathBE.is_file():
								return True
						except:
								return False

					print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

					''')
					print(R+"[*]"+W+" Checking requirements...\n"+R+"[!]"+W+" If you have errors please check that every requirement is on 'OK'\n")
					print(W+" Sudo Permissions     [ "+R+"FAILED"+W+" ]" if sudo() else W+" Sudo Permissions     [   "+G+"OK"+W+"   ]")
					print(W+" Internet             [   "+G+"OK"+W+"   ]" if connect() else " Internet             [ "+R+"FAILED"+W+" ]" )
					print(W+" Check beacon.py      [   "+G+"OK"+W+"   ]" if libreqbeacon() else " Check beacon.py      [ "+R+"FAILED"+W+" ]")
					print(W+" Check client.exe     [   "+G+"OK"+W+"   ]" if libreqclient() else " Check client.exe     [ "+R+"FAILED"+W+" ]")
					print(W+" Check deauther.sh    [   "+G+"OK"+W+"   ]" if libreqdeauther() else " Check deauther.sh    [ "+R+"FAILED"+W+" ]")
					print(W+" Check Evil-Win.py    [   "+G+"OK"+W+"   ]" if libreqevil() else " Check Evil-Win.py    [ "+R+"FAILED"+W+" ]")
					print()
					ansinput()

				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"requirements"+W)
					ansinput()

			if ans == "deauther":
				try:
					os.system("clear")
					print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

					''')
					os.system("sudo bash libreq/deauther.sh")
					print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

					''')
					ansinput()
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"Deauther"+W)
					ansinput()

			if ans == "evil":
				try:
					EWip = input(W+"[Evil-Win] ip > ")
					EWpo = input(W+"[Evil-Win] port > ")
					os.system(f'sudo python3 libreq/Evil-Win.py {EWip} {EWpo}')
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"Evil Win"+W)
					ansinput()

			if ans == "beacon":
				try:
					os.system("sudo python3 libreq/beacon.py")
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"beacon"+W)
					ansinput()

			if ans == "mail":
				print(W+"""┏━("""+R+"""Message from Unbekannt"""+W+""")
┃ Access to your Google Account from less secure apps
┃ 
┃ To better protect your account, effective May 30, 2022, Google will no longer support any third-party apps
┃ or devices that use your username and password to log into your Google Account.
┃
┗━(more: https://support.google.com/accounts/answer/6010255)""")
				ansinput()

			if ans == "database":
				print(R+'''╔═ '''+W+'''DATABASE'''+R+''' ═══════════════════════════════════════════════════════════════════════════════╗
║ 01  '''+W+'''- instant-stresser.com   '''+R+'''11  '''+W+'''- nightmarestresser.com   '''+R+'''21  '''+W+'''- booter.vip              '''+R+'''║
║ 02  '''+W+'''- hardstresser.com       '''+R+'''12  '''+W+'''- sunstresser.com         '''+R+'''22  '''+W+'''- zdstresser.net          '''+R+'''║
║ 03  '''+W+'''- freestresser.to        '''+R+'''13  '''+W+'''- layer7-security.net     '''+R+'''23  '''+W+'''- supremesecurityteam.com '''+R+'''║
║ 04  '''+W+'''- ipstress.in            '''+R+'''14  '''+W+'''- cybervm.io              '''+R+'''24  '''+W+'''- lightstress.pw          '''+R+'''║
║ 05  '''+W+'''- str3ssed.com           '''+R+'''15  '''+W+'''- stresser.world          '''+R+'''25  '''+W+'''- stresser.app            '''+R+'''║
║ 06  '''+W+'''- ts3booter.net          '''+R+'''16  '''+W+'''- anonboot.com            '''+R+'''26  '''+W+'''- booter.cc               '''+R+'''║
║ 07  '''+W+'''- ipstresser.com         '''+R+'''17  '''+W+'''- booter.sx               '''+R+'''27  '''+W+'''- darkstress.xyz          '''+R+'''║
║ 08  '''+W+'''- ripstresser.net        '''+R+'''18  '''+W+'''- darkbooter.xyz          '''+R+'''28  '''+W+'''- evil-stress.xyz         '''+R+'''║
║ 09  '''+W+'''- databooter.to          '''+R+'''19  '''+W+'''- vtoxicity.net           '''+R+'''29  '''+W+'''- downed.rip              '''+R+'''║
║ 10  '''+W+'''- asylumstresser.to      '''+R+'''20  '''+W+'''- smack.rip               '''+R+'''30  '''+W+'''- olympicstress.com       '''+R+'''║
╚══════════════════════════════════════════════════════════════════════════════════════════╝''')
				try:
					option = input(R+'['+ colored('unbekannt'+R+'@'+W+'database', 'white', attrs=['underline']) +R+']'+W+' SITE: ')
					if option == "1":
						webbrowser.open("https://instant-stresser.com")
						ansinput()
					if option == "2":
						webbrowser.open("https://hardstresser.com")
						ansinput()
					if option == "3":
						webbrowser.open("https://freestresser.to")
						ansinput()
					if option == "4":
						webbrowser.open("https://ipstress.in")
						ansinput()
					if option == "5":
						webbrowser.open("https://str3ssed.com")
						ansinput()
					if option == "6":
						webbrowser.open("https://ts3booter.net")
						ansinput()
					if option == "7":
						webbrowser.open("https://ipstresser.com")
						ansinput()	
					if option == "8":
						webbrowser.open("https://ripstresser.net")
						ansinput()	
					if option == "9":
						webbrowser.open("https://databooter.to")
						ansinput()	
					if option == "10":
						webbrowser.open("https://asylumstresser.to")
						ansinput()
					if option == "11":
						webbrowser.open("https://nightmarestresser.com")
						ansinput()	
					if option == "12":
						webbrowser.open("https://sunstresser.com")
						ansinput()	
					if option == "13":
						webbrowser.open("https://layer7-security.net")
						ansinput()	
					if option == "14":
						webbrowser.open("https://cybervm.io")
						ansinput()	
					if option == "15":
						webbrowser.open("https://stresser.world")
						ansinput()	
					if option == "16":
						webbrowser.open("https://anonboot.com")
						ansinput()	
					if option == "17":
						webbrowser.open("https://booter.sx")
						ansinput()	
					if option == "18":
						webbrowser.open("https://darkbooter.xyz")
						ansinput()	
					if option == "19":
						webbrowser.open("https://vtoxicity.net")
						ansinput()	
					if option == "20":
						webbrowser.open("https://smack.rip")
						ansinput()	
					if option == "21":
						webbrowser.open("https://booter.vip")
						ansinput()	
					if option == "22":
						webbrowser.open("https://zdstresser.net")
						ansinput()	
					if option == "23":
						webbrowser.open("https://supremesecurityteam.com")
						ansinput()	
					if option == "24":
						webbrowser.open("https://lightstress.pw")
						ansinput()	
					if option == "25":
						webbrowser.open("https://stresser.app")
						ansinput()	
					if option == "26":
						webbrowser.open("https://booter.cc")
						ansinput()	
					if option == "27":
						webbrowser.open("https://darkstress.xyz")
						ansinput()	
					if option == "28":
						webbrowser.open("https://evil-stress.xyz")
						ansinput()	
					if option == "29":
						webbrowser.open("https://downed.rip")
						ansinput()	
					if option == "30":
						webbrowser.open("https://olympicstress.com")
						ansinput()		
					else:
						print(R+"[-]"+W+" Unknown command in database"+R+": "+W+option)
						ansinput()
				except KeyboardInterrupt:
					print()
					print(R+"[-]"+W+" Leaving module: "+R+"DataBase"+W)
					ansinput()
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"DataBase"+W)
					ansinput()

			if ans == "lookup":
				print(R+'''╔═ '''+W+'''LOOKUP'''+R+''' ═══════════╗
║ -d '''+W+'''- domain lookup '''+R+'''║
║ -i '''+W+'''- ip lookup     '''+R+'''║ 
╚════════════════════╝''')

				lookupans = input(R+'['+ colored('unbekannt'+R+'@'+W+'lookup', 'white', attrs=['underline']) +R+']'+W+'~: ')
				if lookupans == "-i":
					print(B+"[+]"+W+" Using ip lookup")
					try:
						ip_address = input(R+'['+ colored('unbekannt'+R+'@'+W+'lookup', 'white', attrs=['underline']) +R+']'+W+' IP: ')
						request_url = 'https://geolocation-db.com/jsonp/' + ip_address
						response = requests.get(request_url)
						result = response.content.decode()
						result = result.split("(")[1].strip(")")
						result  = json.loads(result)
						print(B+"[+] "+W+"Lookup Result "+R+">>"+W)
						print(result)
						ansinput()
					except KeyboardInterrupt:
						print()
						print(R+"[-]"+W+" Leaving module")
						ansinput()
					except:
						print(R+"[-] "+W+"Error in module: "+R+"Lookup"+W)
						ansinput()

				if lookupans == "-d":
					try:
						print(B+"[+]"+W+" Using domain lookup")
						dlook = input(R+'['+ colored('unbekannt'+R+'@'+W+'lookup', 'white', attrs=['underline']) +R+']'+W+' URL: ')
						adrs = socket.gethostbyname(dlook)
						print(B+"[+] "+W+dlook+" "+R+">>"+W+" "+adrs)
						ansinput()
					except KeyboardInterrupt:
						print()
						print(R+"[-]"+W+" Leaving module")
						ansinput()
					except:
						print(R+"[-]"+W+" Error in module: "+R+"Lookup"+W)
						ansinput()

			if ans == "pinger":
				try:
					ip_list = input(R+'['+ colored('unbekannt'+R+'@'+W+'pinger', 'white', attrs=['underline']) +R+']'+W+' IP  : ')
					port = input(R+'['+ colored('unbekannt'+R+'@'+W+'pinger', 'white', attrs=['underline']) +R+']'+W+' PORT: ')
					time = int(input(R+'['+ colored('unbekannt'+R+'@'+W+'pinger', 'white', attrs=['underline']) +R+']'+W+' TIME: '))
				except KeyboardInterrupt:
					print()
					print(R+"[-]"+W+" Leaving module: "+R+"Pinger"+W)
					ansinput()
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"Pinger"+W)
					ansinput()

				try:
					print(B+"[+]"+W+" Press "+R+"CTRL+C"+W+" to stop ping"+R+"!"+W)
					ping = Ping(ip_list, port, 60)
					ping.ping(time)
					ansinput()
				except TimeoutError:
					print(R+"[-]"+W+" Host is down")
					ansinput()
				except KeyboardInterrupt:
					print()
					print(R+"[-]"+W+" Leaving module: "+R+"Pinger"+W)
					ansinput()
				except:
					print()
					print(R+"[-]"+W+" Error in module: "+R+"Pinger"+W)
					ansinput()
			

			if ans == ".":
				import pwd
				userLINUX = pwd.getpwuid(os.getuid())[0]
				print(B+"[+]"+W+" Press "+R+"CTRL+C"+W+" to exit terminal"+R+"!")
				def ConsoleLog():
					try:
						sc = input(R+'['+ colored('terminal'+R+'@'+W+userLINUX, 'white', attrs=['underline']) +R+']'+W+'~: ')
						command = sc
						subprocess.run(command, shell=True)
						ConsoleLog()

					except KeyboardInterrupt:
						print()
						print(R+"[-]"+W+" Leaving module: "+R+"Shell"+W)
						ansinput()
					
					except:
						print()
						ansinput()
				ConsoleLog()
				ansinput()

			if ans == "clear":
				os.system('cls' if os.name == 'nt' else 'clear')
				print(R+'''             
   _____     _       _               _   
  |  |  |___| |_ ___| |_ ___ ___ ___| |_   '''+W+'''Type '''+R+'''HELP'''+W+''' for Command List'''+R+'''!
  |  |  |   | . | -_| '_| .'|   |   |  _|  '''+W+'''Version '''+R+'''6.0
  |_____|_|_|___|___|_,_|__,|_|_|_|_|_|    '''+W+'''Coded by '''+R+'''@i_am_unbekannt

				''')
				ansinput()

			if ans == "HELP":
				print(R+'''╔═ '''+W+'''HELP'''+R+''' ═════════════════════════════════╗
║ exit    '''+W+'''- exit unbekannt               '''+R+'''║
║ help    '''+W+'''- view all commands            '''+R+'''║
║ .       '''+W+'''- run a shell command          '''+R+'''║
║ clear   '''+W+'''- clear the screen             '''+R+'''║
╚════════════════════════════════════════╝

╔═'''+W+''' MODULES'''+R+''' ══════════════════════════════╗
║ pinger   '''+W+'''- Load the pinger module      '''+R+'''║
║ lookup   '''+W+'''- Load the lookup module      '''+R+'''║
║ database '''+W+'''- Load the database module    '''+R+'''║
║ mail     '''+W+'''- Load the mailbomber module  '''+R+'''║
║ beacon   '''+W+'''- Load the beacon module      '''+R+'''║
║ evil     '''+W+'''- Load the evil win module    '''+R+'''║
║ deauther '''+W+'''- Load the deauther module    '''+R+'''║
║ req      '''+W+'''- Checking requirements       '''+R+'''║
╚════════════════════════════════════════╝''')
				ansinput()

			if ans == "help":
				print(R+'''╔═ '''+W+'''HELP'''+R+''' ═════════════════════════════════╗
║ exit    '''+W+'''- exit unbekannt               '''+R+'''║
║ help    '''+W+'''- view all commands            '''+R+'''║
║ .       '''+W+'''- run a shell command          '''+R+'''║
║ clear   '''+W+'''- clear the screen             '''+R+'''║
╚════════════════════════════════════════╝

╔═'''+W+''' MODULES'''+R+''' ══════════════════════════════╗
║ pinger   '''+W+'''- Load the pinger module      '''+R+'''║
║ lookup   '''+W+'''- Load the lookup module      '''+R+'''║
║ database '''+W+'''- Load the database module    '''+R+'''║
║ mail     '''+W+'''- Load the mailbomber module  '''+R+'''║
║ beacon   '''+W+'''- Load the beacon module      '''+R+'''║
║ evil     '''+W+'''- Load the evil win module    '''+R+'''║
║ deauther '''+W+'''- Load the deauther module    '''+R+'''║
║ req      '''+W+'''- Checking requirements       '''+R+'''║
╚════════════════════════════════════════╝''')
				ansinput()

			if ans == "":
				ansinput()

			if ans == "exit":
				sys.exit()

			if ans == "e":
				sys.exit()
				
			if ans == "quit":
				sys.exit()
				
			if ans == "q":
				sys.exit()
				
			else:
				print(R+"[-]"+W+" Unknown command"+R+": "+W+ans)
				ansinput()
		ansinput()
	mainscreen()	
main()
#sudo cloudflared service install eyJhIjoiYmY1MTZmYzFjMTZlZDFmNWM4OTc3YTY4OThhODMzN2IiLCJ0IjoiNWZhYTBiOGEtMjZkNi00ZGFiLWI2MWQtNmQwZDJkNjFmMTk1IiwicyI6IlpqQXpaamswTkdNdFlXRmlNUzAwTXpNMExXSXhNVFF0WlROa1pEWXlaalEzTVRVeCJ9
