import json
import requests
from pprint import pprint

device = {
    'ip' : '10.63.255.61',
    'username' : 'cisco',
    'password' : 'cisco',
    'port' : '443',

}

headers = {
    "Accept" :  "application/yang-data+json ",
    "content-type" : "application/yang-data+json "
}

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"

print(url)

payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.0.2.60",
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  ]
 }


requests.packages.urllib3.disable_warnings()
# response = requests.post(url,headers=headers,data=json.dumps(payload),auth=(device['username'],device['password']), verify=False)
response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify=False)


