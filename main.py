import csv
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


def search_asset():
    print("\n=== Search Asset ===")

    if not assets:
        print("No assets found.")
        return

    search = input("Enter hostname to search: ").lower()

    found = False

    for asset in assets:
        if search in asset["hostname"].lower():
            print("\n----------------------------------------")
            print(f"Hostname: {asset['hostname']}")
            print(f"IP Address: {asset['ip_address']}")
            print(f"Operating System: {asset['operating_system']}")
            print(f"Owner: {asset['owner']}")
            print(f"Location: {asset['location']}")
            print(f"Status: {asset['status']}")
            found = True

    if not found:
        print("\nNo matching asset found.")


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


def edit_asset():
    print("\n=== Edit Asset ===")

    if not assets:
        print("No assets found.")
        return

    show_assets()

    try:
        asset_number = int(input("\nEnter asset number to edit: "))

        if 1 <= asset_number <= len(assets):
            asset = assets[asset_number - 1]

            print("\nPress Enter to keep the current value.")

            hostname = input(f"Hostname [{asset['hostname']}]: ")
            ip_address = input(f"IP Address [{asset['ip_address']}]: ")
            operating_system = input(f"Operating System [{asset['operating_system']}]: ")
            owner = input(f"Owner [{asset['owner']}]: ")
            location = input(f"Location [{asset['location']}]: ")
            status = input(f"Status [{asset['status']}]: ")

            if hostname:
                asset["hostname"] = hostname
            if ip_address:
                asset["ip_address"] = ip_address
            if operating_system:
                asset["operating_system"] = operating_system
            if owner:
                asset["owner"] = owner
            if location:
                asset["location"] = location
            if status:
                asset["status"] = status

            save_assets()

            print(f"\nUpdated asset: {asset['hostname']}")
        else:
            print("\nInvalid asset number.")

    except ValueError:
        print("\nPlease enter a valid number.")


def export_assets_to_csv():
    print("\n=== Export Assets to CSV ===")

    if not assets:
        print("No assets found.")
        return

    fieldnames = [
        "hostname",
        "ip_address",
        "operating_system",
        "owner",
        "location",
        "status"
    ]

    with open("inventory.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(assets)

    print("\nAssets exported successfully to inventory.csv")


def show_statistics():
    print("\n=== Inventory Statistics ===")

    if not assets:
        print("No assets found.")
        return

    total_assets = len(assets)
    linux_assets = 0
    windows_assets = 0
    active_assets = 0
    inactive_assets = 0

    for asset in assets:
        operating_system = asset["operating_system"].lower()
        status = asset["status"].lower()

        if "linux" in operating_system:
            linux_assets += 1
        elif "windows" in operating_system:
            windows_assets += 1

        if status == "active":
            active_assets += 1
        elif status == "inactive":
            inactive_assets += 1

    other_os_assets = total_assets - linux_assets - windows_assets
    other_status_assets = total_assets - active_assets - inactive_assets

    print(f"Total Assets: {total_assets}")
    print(f"Linux: {linux_assets}")
    print(f"Windows: {windows_assets}")
    print(f"Other OS: {other_os_assets}")
    print(f"Active: {active_assets}")
    print(f"Inactive: {inactive_assets}")
    print(f"Other Status: {other_status_assets}")


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
    print("3. Search Asset")
    print("4. Delete Asset")
    print("5. Edit Asset")
    print("6. Export Assets to CSV")
    print("7. Show Statistics")
    print("8. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_asset()

    elif choice == "2":
        show_assets()

    elif choice == "3":
        search_asset()

    elif choice == "4":
        delete_asset()

    elif choice == "5":
        edit_asset()

    elif choice == "6":
        export_assets_to_csv()

    elif choice == "7":
        show_statistics()

    elif choice == "8":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option. Please try again.")
