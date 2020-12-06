from datetime import datetime
from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json,re,sys,os
from bs4 import BeautifulSoup
import colorama
from colorama import Fore,Back,Style
import random
import threading
import itertools
import time
import sys,os
import requests
import socket
import json

def mengetik(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                sleep(random.random() * 0.5)
try:
   import requests
except:
   print ("\033[1;30m# \033[1;31mHmmm Sepertinya Modul Requests Dan Bs4 Belum Terinstall\n\033[1;30m# \033[1;31mTo install Please Type pip install requests and pip install bs4")
   sys.exit()

c = requests.Session()
#colors using colorama
colorama.init(autoreset=True)
green = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
carol = Style.RESET_ALL
white = Style.RESET_ALL+Style.BRIGHT+Fore.WHITE
magenta = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
red = Style.RESET_ALL+Style.BRIGHT+Fore.RED
blue = Style.RESET_ALL+Style.BRIGHT+Fore.BLUE
cyan = Style.RESET_ALL+Style.BRIGHT+Fore.CYAN
cols = [green,blue,yellow,magenta,red,white,cyan]
logo_a =(red+'                     *              ** *\n                    ***     *     *****\n                     **     **         *\n                    *** *    *         *\n                   ****       **       ******\n                  *****        ** *          **\n                 *****          **            * **\n               *****           *            *\n               ******         *          *\n               **********  *        *\n                 *********          *\n                   *******   ***\n'+green+'*******                 '+red+'**\n'+green+'*******               '+yellow+' *\n'+green+' ******                '+yellow+'* *\n'+green+'  ***    *             '+yellow+'**'+cyan+'   𝆑'+red+'ᵢ'+blue+'ₜ'+green+'ᵣ'+yellow+'ᵢ'+magenta+'ₙ'+green+'ₐ'+red+'ᵢ\n'+green+'             *         '+yellow+' *\n'+green+'         **** *       '+yellow+'*\n'+green+'      *******   *   '+yellow+'*\n'+green+'     *******      '+yellow+'*\n'+green+'     *****        '+yellow+'*\n'+green+'     **           '+yellow+'*\n'+green+'     *           '+yellow+' ** *'+magenta+'    Author  : '+cyan+'Fitrinai')
logo_b =(':=====================================================:\n|Script version: 1.0\t\t       \tby Fitrinai   |\n|======================multibot=======================|\n|      Github: https://www.github.com/g1ng3rb1t3      |\n:======================Channels=======================:\n')

if not os.path.exists("session"):
    os.makedirs("session")
os.system('clear')
sleep(1)
print (logo_a)
sleep(1)
print(f'{random.choice(cols)}{logo_b}')
sleep(1)
if len(sys.argv)<2:
   print ("\n\n\n\033[1;32mUsage : python main.py +62")
   sys.exit(1)

def password():
  c = requests.Session()

  if not os.path.exists(".password"):
      os.makedirs(".password")

  print("\033[1;32mSilahkan Ambil Password Pada Link Di Bawah Ini\033[1;0m\nhttps://duit.cc/WfRU4g")
  pw = c.get("https://pastebin.com/raw/pahqEdgG")
  if not os.path.exists(".password/password.txt"):
      f = open(".password/password.txt", "w+")
      f.write("wkwkwkwkw")
      f.close()

  for i in range(99):
      f = open(".password/password.txt", "r")
      if f.readlines()[0] == pw.text:
          sys.stdout.write('\r                                                \r')
          sys.stdout.write('\r\033[1;32mUsing Exiting Password....!')
          break
      pwin = input("\033[1;32mEnter Password \033[1;30m:\033[1;0m ")
      if pwin == pw.text:
          f = open(".password/password.txt", "w+")
          f.write(pwin)

          f.close()
          break
      else:
          print("\033[1;31mPassword Salah...!")
          if i > 1:
              print("\033[1;33mSilahkan Check Password Pada Link Di Bawah Ini\n\033[1;0mhttps://duit.cc/WfRU4g")
              sys.exit()

def tunggu(x):
    sys.stdout.write("\r")
    sys.stdout.write("                                                               ")
    for remaining in range(x, 0, -1):
       sys.stdout.write("\r")
       sys.stdout.write("\x1b[1;34m[\x1b[1;33m+\x1b[1;34m]\x1b[1;33m{:2d} \x1b[1;32mseconds remaining".format(remaining))
       sys.stdout.flush()
       sleep(1)

ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
page = requests.get("https://pastebin.com/raw/pahqEdgG")
print('\x1b[1;36mSalin teks dibawah ini untuk password selanjutnya!')
print("\x1b[1;36mCopy setelah b' sampai sebelum tanda'")
print('\x1b[1;33m', page.content)
#print(page.content)
sleep(10)
password()
sleep(2)
os.system('clear')
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'
phone_number = sys.argv[1]

client = TelegramClient("session/"+phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
  try:
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('\033[1;0mEnter Your Code : '))
  except SessionPasswordNeededError:
   passw = input("\033[1;0mYour 2fa Password : ")
   me = client.start(phone_number,passw)
myself = client.get_me()
auth = ('\x1b[5;33;5m╔\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;36;5m═⋯⇋⭐️⇌⋯\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;36;5m═\x1b[5;33;5m╗\n\x1b[5;31;5m║\t\t\x1b[5;36;5mUser \x1b[5;33;5m: \x1b[5;32m'+myself.username+'\t\t   \x1b[5;32;5m║\n\x1b[5;35;5m║\t\t\x1b[5;30;5m-------------\t\t   \x1b[5;34;5m║\n\x1b[5;33;5m╚\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;36;5m═⋯⋯⋯⋯⋯⋯\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;33;5m═\x1b[5;36;5m═\x1b[5;31;5m═\x1b[5;95;5m═\x1b[5;32;5m═\x1b[5;34;5m═\x1b[5;36;5m═\x1b[5;33;5m╝')
print (logo_a)
sleep(1)
#print ("\033[1;32mWelcome To TeleBot",myself.username,"\n\033[1;32mBot Ini Di Gunakan Untuk Menuyul Doge Click Bot")
print(auth+'\n')

done = False

#animasi loading
def animate():
    for c in itertools.cycle(['\x1b[1;91m|', '\x1b[1;92m/', '\x1b[1;93m-', '\x1b[1;94m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[5;36;5mM\x1b[5;31;5me\x1b[5;33;5mm\x1b[5;34;5mu\x1b[5;32;5ma\x1b[5;35;5mt \x1b[5;33;5md\x1b[5;36;5ma\x1b[5;31;5mt\x1b[5;34;5ma\x1b[1;0m..' + c)
        sys.stdout.flush()
        sleep(0.06)
#    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

sleep(7)
done = True
print('\n')
color = ['\x1b[5;36;5m','\x1b[5;31;5m','\x1b[5;32;5m','\x1b[5;33;5m','\x1b[5;34;5m','\x1b[5;35;5m','\x1b[5;37;5m']
col = random.choice(color)
localtime = col+time.asctime(time.localtime(time.time()))
print('\x1b[5;36;5mW\x1b[5;31;5ma\x1b[5;32;5mk\x1b[5;33;5mt\x1b[5;34;5mu \x1b[5;35;5mS\x1b[5;37;5me\x1b[5;36;5mk\x1b[5;31;5ma\x1b[5;32;5mr\x1b[5;33;5ma\x1b[5;34;5mn\x1b[5;35;5mg \x1b[5;33;5m: ', localtime)
print('\n')

mengetik("Starting Bot...")
try:
 channel_entity=client.get_entity("@Dogecoin_click_bot")
 channel_username="@Dogecoin_click_bot"
 for i in range(5000000):
  sys.stdout.write("\r")
  sys.stdout.write("                                                              ")
  sys.stdout.write("\r")
  sys.stdout.write("\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \033[1;33mM\x1b[5;36;5me\x1b[5;31;5mn\x1b[5;32;5mg\x1b[5;33;5ma\x1b[5;34;5mm\x1b[5;35;5mb\x1b[5;37;5mi\x1b[5;36;5ml \x1b[5;31;5mU\x1b[5;32;5mr\x1b[5;33;5ml\x1b[5;34;5m.\x1b[5;35;5m.\x1b[5;37;5m.")
  sys.stdout.flush()
  client.send_message(entity=channel_entity,message="/visit")
  sleep(3)
  posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
  if posts.messages[0].message.find("Sorry, there are no new ads available") != -1:
     print ("\n\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;31mIklan Sudah Habis Coba Lagi Besok\n")
     client.send_message(entity=channel_entity,message="\xf0\x9f\x92\xb0 Balance")
     sleep(5)
     posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
     message = posts.messages[0].message
     print (message)
     sys.exit()
  else:
    try:
     url = posts.messages[0].reply_markup.rows[0].buttons[0].url
     sys.stdout.write("\r")
     sys.stdout.write("\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;33mVisit "+url)
     sys.stdout.flush()
     id = posts.messages[0].id
     r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
     soup = BeautifulSoup(r.content,"html.parser")
     if soup.find("div",class_="g-recaptcha") is None and soup.find('div', id="headbar") is None:
        sleep(2)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("\r\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;32m"+messageres+"\n")
        else:
           pass

#\x1b[5;36;5m\x1b[5;31;5m\x1b[5;32;5m\x1b[5;33;5m\x1b[5;34;5m\x1b[5;35;5m\x1b[5;37;5m\x1b[5;36;5m\x1b[5;31;5m\x1b[5;32;5m\x1b[5;33;5m\x1b[5;34;5m\x1b[5;35;5m\x1b[5;37;5m
     elif soup.find('div', id="headbar") is not None:
        for dat in soup.find_all('div',class_="container-fluid"):
            code = dat.get('data-code')
            timer = dat.get('data-timer')
            tokena = dat.get('data-token')
            tunggu(int(timer))
            r = c.post("https://dogeclick.com/reward",data={"code":code,"token":tokena}, headers=ua, timeout=15, allow_redirects=True)
            js = json.loads(r.text)
            sys.stdout.write("\r\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;32mK\x1b[5;36;5ma\x1b[5;31;5mm\x1b[5;32;5mu \x1b[5;33;5mM\x1b[5;34;5me\x1b[5;35;5mn\x1b[5;37;5md\x1b[5;36;5ma\x1b[5;31;5mp\x1b[5;36;5ma\x1b[5;31;5mt\x1b[1;33m"+js[' reward']+" \x1b[5;31;5mD\x1b[5;32;5mo\x1b[5;33;5mg\x1b[5;34;5me \x1b[5;35;5mD\x1b[5;37;5ma\x1b[5;36;5mr\x1b[5;31;5mi \x1b[5;36;5mV\x1b[5;31;5mi\x1b[5;32;5ms\x1b[5;33;5mi\x1b[5;34;5mt \x1b[5;35;5mS\x1b[5;37;5mi\x1b[5;36;5mt\x1b[5;31;5me!\n")
     else:
        sys.stdout.write("\r")
        sys.stdout.write("                                                                ")
        sys.stdout.write("\r")
        sys.stdout.write("\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;31mCaptcha Detected")
        sys.stdout.flush()
        sleep(2)
        client(GetBotCallbackAnswerRequest(
        channel_username,
        id,
        data= posts.messages[0].reply_markup.rows[1].buttons[1].data
        ))
        sys.stdout.write("\r\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;31mSkip Captcha...!       \n")
        sleep(2)
    except:
        sleep(3)
        posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
        message = posts.messages[0].message
        if posts.messages[0].message.find("You must stay") != -1 or posts.messages[0].message.find("Please stay on") != -1:
           sec = re.findall( r'([\d.]*\d+)', message)
           tunggu(int(sec[0]))
           sleep(1)
           posts = client(GetHistoryRequest(peer=channel_entity,limit=2,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
           messageres = posts.messages[1].message
           sleep(2)
           sys.stdout.write("\r\x1b[1;34m[\x1b[1;33m+\x1b[1;34m] \x1b[1;32m"+messageres+"\n")
        else:
           pass
finally:
   client.disconnect()

