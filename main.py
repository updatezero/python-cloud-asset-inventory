def add_asset():
    print("\n=== Add New Asset ===")

    hostname = input("Please enter the hostname: ")
    ip_address = input("Please enter the IP address: ")
    operating_system = input("Please enter the operating system: ")
    owner = input("Please enter the the owner: ")
    location = input("Please enter the location: ")
    status = input("Please enter the status (active/inactive): ")

    print("\nAsset Information")
    print(f"Hostname: {hostname}")
    print(f"IP Address: {ip_address}")
    print(f"Operating System: {operating_system}")
    print(f"Owner: {owner}")
    print(f"Location: {location}")
    print(f"Status: {status}")





print("=" * 40)
print("Cloud Asset Inventory")
print("=" * 40)

name = input("Please enter your name: ")

print(f"\nWelcome, {name}!")
print("\n1. Add Asset")
print("2. Show Assets")
print("3. Exit")
choice = input("\nChoose an option: ")

if choice == "1":
    add_asset()
    

