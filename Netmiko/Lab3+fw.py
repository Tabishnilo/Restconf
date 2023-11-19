from netmiko import ConnectHandler
import os
os.chdir("/Users/predsidio/Documents/Bckp")


r1=ConnectHandler(ip='10.63.255.66',username='admin',password='cisco', secret='cisco', device_type= "cisco_ios")
r2=ConnectHandler(ip='10.63.255.64',username='admin',password='cisco', secret='cisco', device_type= "cisco_ios")
fw1=ConnectHandler(ip='10.63.255.63', username= 'admin',password = 'cisco',secret='cisco', device_type="cisco_asa")


devices = [r1,r2,fw1]

def nodes(dev):
    dev.enable()
    hostname = dev.send_command(" show run | i hostname ").split()[1]
    print(f"connecting to the devices  {hostname}")
    if "fw" in hostname.lower():
        dev.send_command("terminal pager 0")
    else:
        dev.send_command("terminal length 0")
    print(f"taking the backup of  {hostname}")
    temp = dev.send_command("show runn")
    with open(f"{hostname} .cfg" , 'w') as dev_file:
        dev_file.write(temp)


    dev.disconnect()



for items in devices:
    nodes(items)



