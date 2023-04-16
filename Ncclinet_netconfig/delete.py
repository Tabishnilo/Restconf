from ncclient import manager

netconf_interface_template = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>Loopback1</name>
        </interface>
    </interfaces>
</config>"""





with manager.connect (
    host = "sandbox-iosxe-latest-1.cisco.com",
    username = "admin",
    password = "C1sco12345",
    hostkey_verify=False,
    port = 830 
) as m:
    netconf_connect = m.edit_config(netconf_interface_template, target = "running")
    
    print(netconf_connect)