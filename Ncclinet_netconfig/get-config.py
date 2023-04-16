from ncclient import manager
import xmltodict
import xml.dom.minidom


netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

with manager.connect (
    host = "sandbox-iosxe-latest-1.cisco.com",
    username = "admin",
    password = "C1sco12345",
    hostkey_verify=False,
    port = 830 
) as m:
    

    netconfig_reply = m.get_config(source = 'running', filter = netconf_filter)


print(xml.dom.minidom.parseString(netconfig_reply.xml).toprettyxml())

netconf_data = xmltodict.parse(netconfig_reply.xml)["rpc-reply"]["data"]

print (netconf_data)

#Create a list of interfaces
interfaces = netconf_data["interfaces"]["interface"]


for interface in interfaces:
    print("Interface {} enabled status is {}".format(
            interface["name"],
            interface["enabled"]
            )
        )
  

    