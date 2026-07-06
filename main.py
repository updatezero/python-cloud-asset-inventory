import json

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
    save_assets()

    print("\nAsset added successfully!")


def show_assets():
    print("\n=== Stored Assets ===")

    if not assets:
        print("No assets found.")
        return

    for index, asset in enumerate(assets, start=1):
        print(f"\nAsset #{index}")
        print("----------------------------------------")
        print(f"Hostname: {asset['hostname']}")
        print(f"IP Address: {asset['ip_address']}")
        print(f"Operating System: {asset['operating_system']}")
        print(f"Owner: {asset['owner']}")
        print(f"Location: {asset['location']}")
        print(f"Status: {asset['status']}")


def delete_asset():
    print("\n=== Delete Asset ===")

    if not assets:
        print("No assets found.")
        return

    show_assets()

    try:
        asset_number = int(input("\nEnter asset number to delete: "))

        if 1 <= asset_number <= len(assets):
            deleted_asset = assets.pop(asset_number - 1)
            save_assets()
            print(f"\nDeleted asset: {deleted_asset['hostname']}")
        else:
            print("\nInvalid asset number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def save_assets():
    with open("inventory.json", "w") as file:
        json.dump(assets, file, indent=4)


def load_assets():
    global assets

    try:
        with open("inventory.json", "r") as file:
            assets = json.load(file)

    except FileNotFoundError:
        assets = []


print("=" * 40)
print("Cloud Asset Inventory")
print("=" * 40)

name = input("Please enter your name: ")

load_assets()

print(f"\nWelcome, {name}!")

while True:
    print("\n1. Add Asset")
    print("2. Show Assets")
    print("3. Delete Asset")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_asset()

    elif choice == "2":
        show_assets()

    elif choice == "3":
        delete_asset()

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option. Please try again.")