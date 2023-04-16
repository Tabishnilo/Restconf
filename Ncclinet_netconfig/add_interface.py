from ncclient import manager
import xml
import xml.dom.minidom

netconf_interface_template = """
 <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
             <interface>
                     <name>{int_name}</name>
                     <description>{int_desc}</description>
                     <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                     <enabled>true</enabled>
                     <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                             <address>
                                     <ip>{ip_address}</ip>
                                     <netmask>{subnet_mask}</netmask>
                             </address>
                     </ipv4>
             </interface>
     </interfaces>
</config>
"""
# Build the XML Configuration to Send
netconf_payload = netconf_interface_template.format(int_name="Loopback1",
                                          int_desc="RSTForum NETCONF created Loopback",
                                          ip_address="2.2.2.2",
                                          subnet_mask="255.255.255.0"
                                          )
# Ask for the Interface Details to Add

print (netconf_payload)

with manager.connect (
    host = "sandbox-iosxe-latest-1.cisco.com",
    username = "admin",
    password = "C1sco12345",
    hostkey_verify=False,
    port = 830 
) as m:
    
      netconf_reply = m.edit_config(netconf_payload, target="running")




print(netconf_reply)