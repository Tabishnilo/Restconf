import requests
import json
from pprint import pprint


devices = {
    'ip' : '10.63.255.61',
    'username' : 'cisco',
    'password' : 'cisco',
    'port' : '443'
}

headers = {
    "Accept" : "application/yang-data+json",
    "content-type" : "application/yang-data+json",
}

module = "ietf-interfaces:interfaces"

url = f"https://{devices['ip']}:{devices['port']}/restconf/data/{module}/interface=Loopback10000"

payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000 - changed",
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
response = requests.put (url,headers=headers,data=json.dumps(payload), auth=(devices["username"],devices["password"]),verify=False)


if response.status_code == 204:
    print("succesfully created")
else:
    print("sorry!")