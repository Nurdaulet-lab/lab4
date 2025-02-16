import json

# Load JSON file
with open("sample-data.json") as file:
    data = json.load(file)

# Print header
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")
print("-" * 80)

# Extract and print interface data
for item in data.get("imdata", []):
    attributes = item.get("l1PhysIf", {}).get("attributes", {})
    dn = attributes.get("dn", "N/A")
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "N/A")

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu:<6}")