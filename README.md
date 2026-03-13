# prex-cehck

This is a simple Python script to scan a directory (e.g., FiveM installation folder) for all .exe and .dll files and report their locations.

## Usage

Run the script with Python 3:

```bash
python fivem_scanner.py <path_to_directory>
```

For example, on Windows:

```bash
python fivem_scanner.py C:\Users\YourUsername\AppData\Local\FiveM
```

The script will recursively scan the directory and print the paths of all found .exe and .dll files.

## Requirements

- Python 3.x

## Note

This script lists all .exe and .dll files in the specified directory. It does not determine if they were "ever used" as that would require additional system logs or monitoring, which is beyond the scope of this simple scanner.