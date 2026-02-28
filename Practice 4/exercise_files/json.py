import json

# JSON string (simulate your sample-data.json)
data = json.loads('''
{
    "imdata": [
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/33]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/34]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/35]", "descr": "", "speed": "inherit", "mtu": "9150"}}}
    ]
}
''')

# Table header
print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':20} {'Speed':7} {'MTU':6}")
print("-" * 80)

# Loop and print
imdata = data["imdata"]

for item in imdata:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "")
    mtu = attributes.get("mtu", "")
    
    print(f"{dn:50} {descr:20} {speed:7} {mtu:6}")
