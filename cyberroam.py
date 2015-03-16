# Developed by shuchit gandhi

cyberroamIP = "10.100.56.55" #The IP of the Cyberroam site.
cyberroamPort = "8090" #Set to "" if not using.
sleeptime = 7100 #Seconds to sleep

import getpass
from time import strftime
import urllib, time, sys


passwd = "your_password"
#username="201301441@da-iict.org"
username="your_username"
cyberroamAddress = cyberroamIP
if cyberroamPort != "":
	cyberroamAddress = cyberroamAddress+":"+cyberroamPort

while True:
	try:
		f = urllib.urlopen("http://"+cyberroamAddress+"/httpclient.html","mode=191&username="+username+"&password="+passwd+"&btnSubmit=Login")	
		data = f.read()
		print "Message from server: "+data[data.rfind("""display:none">""")+14:-27]
		time.sleep(sleeptime)
	except KeyboardInterrupt:
		f = urllib.urlopen("http://"+cyberroamAddress+"/httpclient.html","mode=193&username="+username+"&password="+passwd+"&btnSubmit=Logout")
		data = f.read()
		print "Message from server: "+data[data.rfind("""display:none">""")+14:-27]
		sys.exit(0)
		
