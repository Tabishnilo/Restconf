import requests
import json
from pprint import pprint

device = {
    "ip" : "10.63.255.61",
    "username" : "admin",
    "password" : "admin",
    "port" : "443",

}

headers = {
    "Accept" : "application/yang-data+json",
    "content-type" : "application/yang-data+json",
}

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"


requests.packages.urllib3.disable_warnings()
response = requests.get(url,headers=headers,auth=(device['username'],device['password']), verify=False).json()


interfaces = response['ietf-interfaces:interfaces']
print (interfaces)
