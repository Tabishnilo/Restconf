import os
import sys

def ip_list_valid():

 ip_list = input(" Enter the file path that contatians valid \n such as example (C/D:\\MyApps\\myfile.txt):-")

#ip_list = '/Users/predsidio/Documents/Bckp/ip-list.txt'

 #Checking if the file exists 

 if os.path.isfile(ip_list) == True:
    print("\n* IP file is valid :)\n")
 else:
    print ("\n* File {} does not exist :( Please check and try again.\n" .format (ip_list))
    sys.exit()


#Open user selected file for reading (IP addresses file)



 with open(ip_list, 'r' ) as selected_ip_file:
    ip_line = selected_ip_file.readlines()
    print(ip_line)
