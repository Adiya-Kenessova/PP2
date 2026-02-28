import json

js = '''
{
    "imdata": [
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/33]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/34]", "descr": "", "speed": "inherit", "mtu": "9150"}}},
        {"l1PhysIf": {"attributes": {"dn": "topology/pod-1/node-201/sys/phys-[eth1/35]", "descr": "", "speed": "inherit", "mtu": "9150"}}}
    ]
}
'''

d = json.loads(js)

print("Interface Status")
print("="*79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-"*50, "-"*20, "-"*6, "-"*6)

for i in d["imdata"]:
    a = i["l1PhysIf"]["attributes"]
    print(f"{a['dn']:<50} {a.get('descr',''):<20} {a['speed']:<6} {a['mtu']:<6}")
