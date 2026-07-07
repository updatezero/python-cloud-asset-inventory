# Python Cloud Asset Inventory

A simple command-line asset inventory tool for cloud and infrastructure environments.

This project is built with Python and focuses on practical automation concepts that are useful for Cloud Engineering, Azure administration, and Cloud Security workflows.

## Features

- Add cloud or infrastructure assets
- Show all stored assets
- Search assets by hostname
- Edit existing assets
- Delete assets by number
- Save inventory data persistently in JSON
- Load inventory data automatically on startup
- Export inventory data to CSV
- Show basic inventory statistics

## Asset Fields

Each asset contains the following information:

- Hostname
- IP address
- Operating system
- Owner
- Location
- Status

## Requirements

- Python 3

No external Python packages are required. The project only uses Python standard library modules:

- `json`
- `csv`

## Installation

Clone the repository:

```bash
git clone https://github.com/recica/python-cloud-asset-inventory.git
cd python-cloud-asset-inventory
```

Run the application:

```bash
python3 main.py
```

## Usage

After starting the tool, choose an option from the menu:

```text
1. Add Asset
2. Show Assets
3. Search Asset
4. Delete Asset
5. Edit Asset
6. Export Assets to CSV
7. Show Statistics
8. Exit
```

## Example Output

```text
=== Stored Assets ===

Asset #1
----------------------------------------
Hostname: VM_LAB01_Art
IP Address: 10.10.10.10
Operating System: Linux
Owner: Art
Location: switzerland_north
Status: active
```

## CSV Export

The CSV export creates an `inventory.csv` file with the following columns:

```text
hostname,ip_address,operating_system,owner,location,status
```

This makes the inventory easier to use in Excel, reports, or future automation workflows.

## Statistics

The statistics view shows a quick overview of the current inventory:

```text
=== Inventory Statistics ===
Total Assets: 3
Linux: 1
Windows: 0
Other OS: 2
Active: 1
Inactive: 0
Other Status: 2
```

## Project Structure

```text
python-cloud-asset-inventory/
|-- main.py
|-- inventory.json
|-- .gitignore
`-- README.md
```

## Learning Goals

This project practices Python concepts that are useful for real automation work:

- Functions
- Lists and dictionaries
- Loops
- Conditional logic
- User input
- JSON persistence
- CSV export
- Basic CLI application structure

## Roadmap

Possible future improvements:

- Validate IP addresses
- Validate asset status values
- Add asset categories or cloud provider fields
- Add automated tests
- Add command-line arguments
- Export reports in additional formats
