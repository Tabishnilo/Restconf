from ncclient import manager
from pprint import pprint
import xml
import xml.dom.minidom

m = manager.connect(host="10.63.255.63",port=830,username="admin",password="admin")

running = m.get_config("running").xml
print(xml.dom.minidom.parseString(running).toprettyxml())


