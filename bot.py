import urllib
import os,sys,time,random,string,colorama
from time import sleep
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

app_link = "https://app.a123456b.com"
html = urlopen(app_link).read()
soup = BeautifulSoup(html,'html.parser')
print(soup)

find_div = soup.find('input' , {'id':'username'})
for each in find_div.findAll('user'):
	print(each.text)
