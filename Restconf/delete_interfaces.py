import json
import requests
from pprint import pprint

devices = {
    'ip' : "10.63.255.61",
    'Username' : input("Enter the username"),
    "password": input("Enter the password"),
    "port" : "443",
}

headers = {
    "Accept" : "application/yang-data+json",
    "Content-Type" : "application/yang-data+json", 
}

module = "ietf-interfaces:interfaces"

url = f"https://{devices['ip']}:{devices['port']}/restconf/data/{module}/interface=Loopback10000"

requests.packages.urllib3.disable_warnings()
response = requests.delete(url,headers=headers, auth=(devices["Username"],devices["password"]),verify=False)

if response.status_code == 204:
    print("Deleted")

else:
    print("Unsuscfull")