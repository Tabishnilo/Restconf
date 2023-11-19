from netmiko import ConnectHandler
import os
os.chdir("/Users/predsidio/Documents/Bckp")


r1=ConnectHandler(ip='10.63.255.66',username='admin',password='cisco', secret='cisco', device_type= "cisco_ios")
r2=ConnectHandler(ip='10.63.255.64',username='admin',password='cisco', secret='cisco', device_type= "cisco_ios")

devices = [r1,r2]

n = 1

for dev in devices:
    dev.enable()
    print("Connect to the device")
    dev.send_command("terminal length 0")
    config=dev.send_command('show runn')
    with open ('R' + str(n) + '.cfg', "w") as temp:
        temp.write(config)
    dev.disconnect()

    n = n+1


