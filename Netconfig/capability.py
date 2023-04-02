
from ncclient import manager



m =  manager.connect(host='10.63.255.63', port=830, username='admin', password='admin')


for capability in m.server_capabilities:
   print('*'* 50)
   print(capability)