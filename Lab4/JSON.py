# Python JSON parsing

import json

# 1. Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.

with open("sample-data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

for item in data:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else ""
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")
