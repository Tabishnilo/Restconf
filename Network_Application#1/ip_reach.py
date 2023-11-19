import sys
import os

#def ip_reachable(iplist):

ip_list = ['6.7.8.9']

for ip in ip_list:
        ip = ip.rstrip('\n')
        response = os.popen(f"ping -c 4 {ip} ").read()

        if("Request timeout " or "unreachable") in response:
            print("Network device is down")
            continue

        else:
            print("Life is good ! ")
            sys.exit()
        