from netmiko import ConnectHandler
import os
os.chdir("/Users/predsidio/Documents/Bckp")

R1 = ConnectHandler(ip= '10.63.255.66', username = 'admin', password= 'cisco', device_type= "cisco_ios" )

print ("Connected to the device")
R1.enable()
R1.send_command("terminal length 0")
r1_config= R1.send_command('show run')

with open ("R1.cfg", "w") as temp:
    temp.write(r1_config)

R1.disconnect()


