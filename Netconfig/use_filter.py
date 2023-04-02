from ncclient import manager
import xmltodict
import xml.dom.minidom

m = manager.connect(host="10.63.255.63",port=830,username="admin",password="admin")

netconf_filter = """
<filter>
   <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
         <name>GigabitEthernet1</name>
      </interface>
   </interfaces>
</filter>
"""

running_config = m.get_config("running", netconf_filter)

running_config_xml = xmltodict.parse(running_config.xml)["rpc-reply"]["data"]
print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())



