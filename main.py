assets = []

def add_asset():
    print("\n=== Add New Asset ===")

    hostname = input("Please enter the hostname: ")
    ip_address = input("Please enter the IP address: ")
    operating_system = input("Please enter the operating system: ")
    owner = input("Please enter the owner: ")
    location = input("Please enter the location: ")
    status = input("Please enter the status (active/inactive): ")

    asset = {
        "hostname": hostname,
        "ip_address": ip_address,
        "operating_system": operating_system,
        "owner": owner,
        "location": location,
        "status": status
    }

    assets.append(asset)

    print("\nAsset added successfully!")

def show_assets():
    print("\n=== Stored Assets ===")
    
    for asset in assets:
        print(asset)

print("=" * 40)
print("Cloud Asset Inventory")
print("=" * 40)

name = input("Please enter your name: ")

print(f"\nWelcome, {name}!")

while True:
    print("\n1. Add Asset")
    print("2. Show Assets")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_asset()
    
    if choice == "2":
        show_assets()

    if choice =="3":
        print("\nGoodbye!")
        break