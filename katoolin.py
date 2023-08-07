#!/usr/bin/python

import os
import sys, traceback


#!/usr/bin/env python

categories = {
	1:['information_gathering', 
	['acccheck', 'ace-voip', 'amap', 'automater', 'braa', 'casefile', 'cdpsnarf', 'cisco-torch', 
	'cookie-cadger', 'copy-router-config', 'dmitry', 'dnmap', 'dnsenum', 'dnsmap', 'dnsrecon',
	'dnstracer', 'dnswalk', 'dotdotpwn', 'enum4linux', 'enumiax', 'fierce', 'firewalk', 'fragroute',
	'fragrouter', 'ghost-phisher', 'golismero', 'goofile', 'xplico', 'hping3', 'intrace', 'ismtp',
	'lbd', 'maltego-teeth', 'masscan', 'metagoofil', 'miranda', 'nbtscan-unixwiz', 'nmap', 'p0f',
	'parsero', 'recon-ng', 'set', 'smtp-user-enum', 'snmpcheck', 'sslcaudit', 'sslsplit', 'sslstrip',
	'sslyze', 'thc-ipv6', 'theharvester', 'tlssled', 'twofi', 'urlcrazy','wireshark', 'wol-e']
	],
	
	2:['vulnerability_analysis',
	['bbqsql', 'bed', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 'cisco-torch',
	'copy-router-config', 'doona', 'dotdotpwn', 'greenbone-security-assistant', 'hexorbase', 'jsql',
	'lynis', 'nmap', 'ohrwurm', 'openvas-administrator', 'openvas-cli', 'openvas-manager', 'openvas-scanner',
	'oscanner', 'powerfuzzer', 'sfuzz', 'sidguesser', 'siparmyknife', 'sqlmap', 'sqlninja', 'sqlsus',
	'thc-ipv6', 'tnscmd10g', 'unix-privesc-check', 'yersinia']
	],

	3:['wireless_attacks',
	['aircrack-ng', 'asleap', 'bluelog', 'blueranger', 'bluesnarfer', 'bully', 'cowpatty', 'crackle', 
	'eapmd5pass', 'fern-wifi-cracker', 'ghost-phisher', 'giskismet', 'gqrx', 'hostapd-wpe', 'kalibrate-rtl',
	'killerbee', 'kismet', 'mdk3', 'mfcuk', 'mfoc', 'mfterm', 'multimon-ng', 'pixiewps', 'reaver', 'redfang',
	'rtlsdr-scanner', 'spooftooph', 'wifi-honey', 'wifiphisher', 'wifitap', 'wifite']
	],

	4:['web_applications',
	['apache-users', 'arachni', 'bbqsql', 'blindelephant', 'burpsuite', 'cutycapt', 'davtest', 'deblaze', 
	'dirb', 'dirbuster', 'fimap', 'funkload', 'gobuster', 'grabber', 'jboss-autopwn', 'joomscan', 'jsql',
	'maltego-teeth', 'padbuster', 'paros', 'parsero', 'plecost', 'powerfuzzer', 'proxystrike', 'recon-ng',
	'skipfish', 'sqlmap', 'sqlninja', 'sqlsus', 'ua-tester', 'uniscan', 'vega', 'w3af', 'webscarab',
	'websploit', 'wfuzz', 'wpscan', 'xsser', 'zaproxy']
	],

	5:['sniffing_spoofing',
	['burpsuite', 'dnschef', 'fiked', 'hamster-sidejack', 'hexinject', 'iaxflood', 'inviteflood', 'ismtp',
	'isr-evilgrade', 'mitmproxy', 'ohrwurm', 'protos-sip', 'rebind', 'responder', 'rtpbreak', 'rtpinsertsound',
	'rtpmixsound', 'sctpscan', 'siparmyknife', 'sipp', 'sipvicious', 'sniffjoke', 'sslsplit', 'sslstrip',
	'thc-ipv6', 'voiphopper', 'webscarab', 'wifi-honey', 'wireshark', 'xspy', 'yersinia', 'zaproxy']
	],

	6:['maintaining_access',
	['cryptcat', 'cymothoa', 'dbd', 'dns2tcp', 'http-tunnel', 'httptunnel', 'intersect', 'nishang', 'polenum',
	'powersploit', 'pwnat', 'ridenum', 'sbd', 'u3-pwn', 'webshells', 'weevely', 'winexe']
	],

	7:['reporting_tools',
	['casefile', 'cutycapt', 'dos2unix', 'dradis', 'keepnote', 'magictree', 'metagoofil', 'nipper-ng', 'pipal']
	],

	8:['exploitation_tools',
	['armitage', 'backdoor-factory', 'beef-xss', 'cisco-auditing-tool', 'cisco-global-exploiter', 'cisco-ocs', 
	'cisco-torch', 'crackle', 'exploitdb', 'jboss-autopwn', 'linux-exploit-suggester', 'maltego-teeth', 'set', 
	'shellnoob', 'sqlmap', 'thc-ipv6', 'yersinia']
	],

	9:['forensics_tools',
	['binwalk', 'bulk-extractor', 'chntpw', 'cuckoo', 'dc3dd', 'ddrescue', 'python-distorm3', 'dumpzilla', 
	'volatility', 'xplico', 'foremost', 'galleta', 'guymager', 'iphone-backup-analyzer', 'p0f', 'pdf-parser', 
	'pdfid', 'pdgmail', 'peepdf', 'extundelete']
	],

	10:['stress_testing',
	['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 
	'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']
	],

	11:['password_attacks',
	['acccheck', 'burpsuite', 'cewl', 'chntpw', 'cisco-auditing-tool', 'cmospwd', 'creddump', 'crunch', 
	'findmyhash', 'gpp-decrypt', 'hash-identifier', 'hexorbase', 'hydra', 'john', 'johnny', 'keimpx', 
	'maltego-teeth', 'maskprocessor', 'multiforcer', 'ncrack', 'oclgausscrack', 'pack', 'patator', 'polenum', 
	'rainbowcrack', 'rcracki-mt', 'rsmangler', 'statsprocessor', 'thc-pptp-bruter', 'truecrack', 'webscarab', 
	'wordlists', 'zaproxy']
	],

	12:['reverse_engineering',
	['apktool', 'dex2jar', 'python-distorm3', 'edb-debugger', 'jad', 'javasnoop', 'smali', 'valgrind', 'yara']
	],

	13:['hardware_hacking',
	[	'android-sdk', 'apktool', 'arduino', 'dex2jar', 'sakis3g', 'smali']
	],

	14:['extra',
	['kali-linux', 'kali-linux-full', 'kali-linux-all', 'kali-linux-top10', 'kali-linux-forensic', 
	'kali-linux-gpu', 'kali-linux-pwtools', 'kali-linux-rfid', 'kali-linux-sdr', 'kali-linux-voip', 
	'kali-linux-web', 'kali-linux-wireless', 'squid3']
	]
}



class Menu():  # All menu of katoolin
	main = '''

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
'''
	
	#-------------------------------------------------------------------------------------------------------------------
	repository_menu1 = '''
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help

'''

	#-------------------------------------------------------------------------------------------------------------------
	repository_menu2 = '''
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file

'''

	#-------------------------------------------------------------------------------------------------------------------
	classic_menu = ''' 
ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.

It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.

Like the classic GNOME menu, it includes Wine games and applications if you have those installed.

For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/

'''

	
	#-------------------------------------------------------------------------------------------------------------------
	command_menu = ''' 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

'''


	#-------------------------------------------------------------------------------------------------------------------
	categories_menu = '''
\033[1;36m**************************** All Categories *****************************\033[1;m

1) Information Gathering			8) Exploitation Tools
2) Vulnerability Analysis			9) Forensics Tools
3) Wireless Attacks				10) Stress Testing
4) Web Applications				11) Password Attacks
5) Sniffing & Spoofing				12) Reverse Engineering
6) Maintaining Access				13) Hardware Hacking
7) Reporting Tools 				14) Extra
									
0) All

'''


	#-------------------------------------------------------------------------------------------------------------------
	info_gathering_menu = '''
\033[1;36m=+[ Information Gathering \033[1;m

 1) acccheck					30) lbd
 2) ace-voip					31) Maltego Teeth
 3) Amap					32) masscan
 4) Automater					33) Metagoofil
 5) bing-ip2hosts				34) Miranda
 6) braa					35) Nmap
 7) CaseFile					36) ntop
 8) CDPSnarf					37) p0f
 9) cisco-torch					38) Parsero
10) Cookie Cadger				39) Recon-ng
11) copy-router-config				40) SET
12) DMitry					41) smtp-user-enum
13) dnmap					42) snmpcheck
14) dnsenum					43) sslcaudit
15) dnsmap					44) SSLsplit
16) DNSRecon					45) sslstrip
17) dnstracer					46) SSLyze
18) dnswalk					47) THC-IPV6
19) DotDotPwn					48) theHarvester
20) enum4linux					49) TLSSLed
21) enumIAX					50) twofi
22) exploitdb					51) URLCrazy
23) Fierce					52) Wireshark
24) Firewalk					53) WOL-E
25) fragroute					54) Xplico
26) fragrouter					55) iSMTP
27) Ghost Phisher				56) InTrace
28) GoLismero					57) hping3
29) goofile

0) Install all Information Gathering tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	vul_analysis_menu = '''
\033[1;36m=+[ Vulnerability Analysis\033[1;m

 1) BBQSQL				18) Nmap
 2) BED					19)ohrwurm
 3) cisco-auditing-tool			20) openvas-administrator
 4) cisco-global-exploiter		21) openvas-cli
 5) cisco-ocs				22) openvas-manager
 6) cisco-torch				23) openvas-scanner
 7) copy-router-config			24) Oscanner
 8) commix				25) Powerfuzzer
 9) DBPwAudit				26) sfuzz
10) DoonaDot				27) SidGuesser
11) DotPwn				28) SIPArmyKnife
12) Greenbone Security Assistant 	29) sqlmap
13) GSD					30) Sqlninja
14) HexorBase				31) sqlsus
15) Inguma				32) THC-IPV6
16) jSQL				33) tnscmd10g
17) Lynis				34) unix-privesc-check
					35) Yersinia

0) Install all Vulnerability Analysis tools
				 
'''

	wireless_menu = '''
		\033[1;36m=+[ Wireless Attacks\033[1;m

 1) Aircrack-ng				17) kalibrate-rtl
 2) Asleap				18) KillerBee
 3) Bluelog				19) Kismet
 4) BlueMaho				20) mdk3
 5) Bluepot				21) mfcuk
 6) BlueRanger				22) mfoc
 7) Bluesnarfer				23) mfterm
 8) Bully				24) Multimon-NG
 9) coWPAtty				25) PixieWPS
10) crackle				26) Reaver
11) eapmd5pass				27) redfang
12) Fern Wifi Cracker			28) RTLSDR Scanner
13) Ghost Phisher			29) Spooftooph
14) GISKismet				30) Wifi Honey				31) Wifitap
16) gr-scan				32) Wifite 

0) Install all Wireless Attacks tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	web_apps_menu = '''
\033[1;36m=+[ Web Applications\033[1;m

 1) apache-users			21) Parsero
 2) Arachni				22) plecost
 3) BBQSQL				23) Powerfuzzer
 4) BlindElephant			24) ProxyStrike
 5) Burp Suite				25) Recon-ng
 6) commix				26) Skipfish
 7) CutyCapt				27) sqlmap
 8) DAVTest				28) Sqlninja
 9) deblaze				29) sqlsus
10) DIRB				30) ua-tester
11) DirBuster				31) Uniscan
12) fimap				32) Vega
13) FunkLoad				33) w3af
14) Grabber				34) WebScarab
15) jboss-autopwn			35) Webshag
16) joomscan				36) WebSlayer
17) jSQL				37) WebSploit
18) Maltego Teeth			38) Wfuzz
19) PadBuster				39) WPScan
20) Paros				40) XSSer
					41) zaproxy

0) Install all Web Applications tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	snif_spoof_menu = '''
\033[1;36m=+[ Sniffing & Spoofing\033[1;m

 1) Burp Suite				17) rtpmixsound
 2) DNSChef				18) sctpscan
 3) fiked				19) SIPArmyKnife
 4) hamster-sidejack			20) SIPp
 5) HexInject				21) SIPVicious
 6) iaxflood				22) SniffJoke
 7) inviteflood				23) SSLsplit
 8) iSMTP				24) sslstrip
 9) isr-evilgrade			25) THC-IPV6
10) mitmproxy				26) VoIPHopper
11) ohrwurm				27) WebScarab
12) protos-sip				28) Wifi Honey
13) rebind				29) Wireshark
14) responder				30) xspy
15) rtpbreak				31) Yersinia
16) rtpinsertsound			32) zaproxy 

0) Install all Sniffing & Spoofing tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	maintaining_accsess_menu = '''
\033[1;36m=+[ Maintaining Access\033[1;m

 1) CryptCat
 2) Cymothoa
 3) dbd
 4) dns2tcp
 5) http-tunnel	
 6) HTTPTunnel
 7) Intersect
 8) Nishang
 9) polenum
10) PowerSploit
11) pwnat
12) RidEnum
13) sbd
14) U3-Pwn
15) Webshells
16) Weevely

0) Install all Maintaining Access tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	reporting_tools_menu = '''
\033[1;36m=+[ Reporting Tools\033[1;m

1) CaseFile
2) CutyCapt
3) dos2unix
4) Dradis
5) KeepNote	
6) MagicTree
7) Metagoofil
8) Nipper-ng
9) pipal

0) Install all Reporting Tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	exploit_menu = '''
\033[1;36m=+[ Exploitation Tools\033[1;m

 1) Armitage
 2) Backdoor Factory
 3) BeEF
 4) cisco-auditing-tool
 5) cisco-global-exploiter	
 6) cisco-ocs
 7) cisco-torch
 8) commix
 9) crackle
10) jboss-autopwn
11) Linux Exploit Suggester
12) Maltego Teeth
13) SET
14) ShellNoob
15) sqlmap
16) THC-IPV6
17) Yersinia

0) Install all Exploitation Tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	forensics_menu = '''
\033[1;36m=+[ Forensics Tools\033[1;m

 1) Binwalk				11) extundelete
 2) bulk-extractor			12) Foremost
 3) Capstone				13) Galleta
 4) chntpw				14) Guymager
 5) Cuckoo				15) iPhone Backup Analyzer
 6) dc3dd				16) p0f
 7) ddrescue				17) pdf-parser
 8) DFF					18) pdfid
 9) diStorm3				19) pdgmail
10) Dumpzilla				20) peepdf
					21) RegRipper
					22) Volatility
					23) Xplico

0) Install all Forensics Tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	stress_testing_menu = '''
\033[1;36m=+[ Stress Testing\033[1;m

 1) DHCPig
 2) FunkLoad
 3) iaxflood
 4) Inundator
 5) inviteflood	
 6) ipv6-toolkit
 7) mdk3
 8) Reaver
 9) rtpflood
10) SlowHTTPTest
11) t50
12) Termineter
13) THC-IPV6
14) THC-SSL-DOS 		

0) Install all Stress Testing tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	password_attack_menu = '''
\033[1;36m=+[ Password Attacks\033[1;m

 1) acccheck				19) Maskprocessor
 2) Burp Suite				20) multiforcer
 3) CeWL				21) Ncrack
 4) chntpw				22) oclgausscrack
 5) cisco-auditing-tool			23) PACK
 6) CmosPwd				24) patator
 7) creddump				25) phrasendrescher
 8) crunch				26) polenum
 9) DBPwAudit				27) RainbowCrack
10) findmyhash				28) rcracki-mt
11) gpp-decrypt				29) RSMangler
12) hash-identifier			30) SQLdict
13) HexorBase				31) Statsprocessor
14) THC-Hydra				32) THC-pptp-bruter
15) John the Ripper			33) TrueCrack
16) Johnny				34) WebScarab 
17) keimpx				35) wordlists 
18) Maltego Teeth			36) zaproxy 

0) Install all Password Attacks tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	reverse_engineering_menu = '''
\033[1;36m=+[ Reverse Engineering\033[1;m

 1) apktool
 2) dex2jar
 3) diStorm3
 4) edb-debugger
 5) jad	
 6) javasnoop
 7) JD-GUI
 8) OllyDbg
 9) smali
10) Valgrind
11) YARA

0) Install all Reverse Engineering tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	hardware_hacking_manu = '''
\033[1;36m=+[ Hardware Hacking\033[1;m

 1) android-sdk
 2) apktool
 3) Arduino
 4) dex2jar
 5) Sakis3G	
 6) smali

0) Install all Hardware Hacking tools
				 
'''

	#-------------------------------------------------------------------------------------------------------------------
	extra_menu = '''
\033[1;36m=+[ Extra\033[1;m

1) Wifresti
2) Squid3
'''


if os.getuid() != 0:
	print ("Sorry. This script requires sudo privledges")
	sys.exit()

# TOOLS_DICT = {
	# 1: 
# }

def install_tool(key_category, indx_tool):
	try:
		os.system("apt-get install " + categories[int(key_category)][1][int(indx_tool) - 1])
	except KeyError:
		print("\033[1;32mNo such category\033[1;32m")
	except IndexError:
		print("\033[1;32mNo such tool\033[1;32m")
	except ValueError:
		print("\033[1;32mUncorrect type\033[1;32m")


def main():
	try:
		print(Menu.main)
		def inicio1():
			while True:
				print (Menu.repository_menu1)

				opcion0 = raw_input("\033[1;36mkat > \033[1;m")
			
				while opcion0 == "1":
					print (Menu.repository_menu2)
					repo = raw_input("\033[1;32mWhat do you want to do ?> \033[1;m")
					if repo == "1":
						cmd1 = os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print ("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "4":
						file = open('/etc/apt/sources.list', 'r')

						print (file.read())

					else:
						print ("\033[1;31mSorry, that was an invalid command!\033[1;m") 					
						
				def inicio():
					while opcion0 == "2":
						print (Menu.categories_menu)
						print ("\033[1;32mSelect a category or press (0) to install all Kali linux tools .\n\033[1;m")

						opcion1 = raw_input("\033[1;36mkat > \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "0":
							cmd = os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
						while opcion1 == "1":
							print (Menu.info_gathering_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "5":
								cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
							elif opcion2 == "36":
								print ('ntop is unavailable')
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()		
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")				
							else:
								install_tool(opcion1, opcion2)

						while opcion1 == "2":
							print (Menu.vul_analysis_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")

							if opcion2 == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "9":
								cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
							elif opcion2 == "13":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
							elif opcion2 == "15":
								print ("Please download inguma from : http://inguma.sourceforge.net")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")						
							else:
								install_tool(opcion1, opcion2)

						while opcion1 == "3":
							print (Menu.wireless_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
							elif opcion2 == "5":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
							elif opcion2 == "16":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()						
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "4":
							print (Menu.web_apps_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")

							
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "7":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "35":
								print ("Webshag is unavailable")
							elif opcion2 == "36":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")									
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()	
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")												
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "5":
							print (Menu.snif_spoof_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")  
							else:
								install_tool(opcion1, opcion2)

						while opcion1 == "6":
							print (Menu.maintaining_accsess_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "7":
							print (Menu.reporting_tools_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")  
							else:
								install_tool(opcion1, opcion2)

						while opcion1 == "8":
							print (Menu.exploit_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")

							if opcion2 == "8":
								cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")  						
							else:
								install_tool(opcion1, opcion2)

						while opcion1 == "9":
							print (Menu.forensics_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							
							if opcion2 == "3":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
							elif opcion2 == "8":
								print ('dff is unavailable')
							elif opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
							elif opcion2 == "21":
								print ("Regripper is unavailable")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")						
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "10":
							print (Menu.stress_testing_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "4":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/inundator.git")   				             										
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "11":
							print (Menu.password_attack_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "9":
								cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
							elif opcion2 == "14":
								cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
							elif opcion2 == "25":
								cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
							elif opcion2 == "30":
								print ("Sqldict is unavailable")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "12" :
							print (Menu.reverse_engineering_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "13" :
							print (Menu.hardware_hacking_manu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")

							if opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()   
							elif opcion2 == "0":
								cmd = os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
							else:
								install_tool(opcion1, opcion2)
						
						while opcion1 == "14" :
							print (Menu.extra_menu)
							print ("\033[1;32mInsert the number of the tool to install it .\n\033[1;m")
							opcion2 = raw_input("\033[1;36mkat > \033[1;m")
							if opcion2 == "1":
								cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
								print (" ")
							elif opcion2 == "2":
								cmd = os.system("apt-get install squid3")
								print (" ")
							elif opcion2 == "back":
								inicio()
							elif opcion2 == "gohome":
								inicio1()
				inicio()

				if opcion0 == "3":
					print(Menu.classic_menu)
					repo = raw_input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd = os.system("sudo apt-get install classicmenu-indicator")

				elif opcion0 == "4"	:
					repo = raw_input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("apt-get install kali-menu")
				
				elif opcion0 == "5":
					print (Menu.command_menu)

		inicio1()
	except KeyboardInterrupt:
		print ("Shutdown requested...Goodbye...")
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()
