
#!/usr/bin/python

#Name          : Basic GeoIP
#Writer(s)     : svnyasin | yasinseven.com
#Description   : Basic GeoIP is a very simple ip geo tracker tool.


import urllib3
import mechanize
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style, init
init(autoreset=True)

print ("\r")

print(Fore.YELLOW + """
██████╗░░█████╗░░██████╗██╗░█████╗░  ░██████╗░███████╗░█████╗░██╗██████╗░
██╔══██╗██╔══██╗██╔════╝██║██╔══██╗  ██╔════╝░██╔════╝██╔══██╗██║██╔══██╗
██████╦╝███████║╚█████╗░██║██║░░╚═╝  ██║░░██╗░█████╗░░██║░░██║██║██████╔╝
██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗  ██║░░╚██╗██╔══╝░░██║░░██║██║██╔═══╝░
██████╦╝██║░░██║██████╔╝██║╚█████╔╝  ╚██████╔╝███████╗╚█████╔╝██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░  ░╚═════╝░╚══════╝░╚════╝░╚═╝╚═╝░░░░░""")

print ("\r")
print ("\r")
print ("\r")
print ("\r")

def send():
	url = "https://www.ultratools.com/tools/geoIp"
	browser.open(url)
	browser.select_form(name = "geoIpForm")
	ip = input("What Is Your Target IP : ")
	browser["ipAddress"] = ip
	res = browser.submit()
	#print("Form Submitted.")
	data = res.read()
	html = data
	parsed_html = BeautifulSoup(html, "html.parser")
	geo= parsed_html.body.find('div', attrs={'class':'tool-results'}).text.split()
	print ("\r")
	print(" IP           :  " + ip)
	print(" City         :  " + geo[21])
	print(" State        :  " + geo[12])
	print(" Country Code :  " + geo[6])
	print(" Country      :  " + geo[3])
	print(" Continent    :  " + geo[1])
	print(" Time Zone    :  " + geo[25])
	print(" Latitude     :  " + geo[-3])
	print(" Longitude    :  " + geo[-1])
	print ("\r")

browser = mechanize.Browser()

while True: 
	send()