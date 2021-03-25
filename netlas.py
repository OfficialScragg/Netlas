#Network Connection IP LookUp
#Author: 0xWraith
#Date: 24/03/2021
import psutil as ps
import time, requests, json
from geoip import geolite2

def main():
	results = ps.net_connections()
	count = 0
	while (True):
		new = ps.net_connections()
		if results != new:
			results = new
		for ip in results:
			if ip[4] != () and ip[4][0] != "::1" and ip[4][0] != "127.0.0.1":
				count+=1
				curr = str(ip[4][0])
				time.sleep(2)

				# USING API
				response = requests.get("http://ip-api.com/json/"+str(curr)+"?fields=status,country,city,query")
				if 'json' in response.headers.get('Content-Type'):
					details = response.json()
					if details["status"] == "success":
						if details["country"] == "South Africa":
							print(f"{bcolors.YELLOW}"+details["country"]+"("+details["city"]+"): "+str(curr))
						elif details["country"] == "United States": 
							print(f"{bcolors.OKCYAN}"+details["country"]+"("+details["city"]+"): "+str(curr))
						elif details["country"] == "France":
							print(f"{bcolors.OKGREEN}"+details["country"]+"("+details["city"]+"): "+str(curr))
						else: 
							print(f"{bcolors.RED}"+details["country"]+"("+details["city"]+"): "+str(curr))

				#USING GEOIP
				#match = geolite2.lookup(b'10.22.43.222')
				#if match is not None:
					#country = match.country
					#if country == "South Africa":
						#print(f"{bcolors.YELLOW}"+country+": "+str(curr)+"\n")
					#elif country == "United States": 
						#print(f"{bcolors.OKCYAN}"+country+": "+str(curr)+"\n")
					#elif country == "France":
						#print(f"{bcolors.OKGREEN}"+country+": "+str(curr)+"\n")
					#else: 
						#print(f"{bcolors.RED}"+country+": "+str(curr)+"\n")



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\u001b[33m'
    RED = '\u001b[31m'
    MAGENTA = '\u001b[35m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":
    main()