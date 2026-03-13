import os
import sys
from datetime import datetime

def scan_directory(directory):
    """
    Recursively scans the given directory for .exe and .dll files
    and prints their full paths along with file details.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.exe', '.dll')):
                full_path = os.path.join(root, file)
                try:
                    stat = os.stat(full_path)
                    size = stat.st_size
                    mtime = datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    print(f"Found: {full_path}")
                    print(f"  Size: {size} bytes")
                    print(f"  Last modified: {mtime}")
                    print()
                except OSError as e:
                    print(f"Error accessing {full_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fivem_scanner.py <directory>")
        print("Example: python fivem_scanner.py C:\\Users\\YourUser\\AppData\\Local\\FiveM")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        sys.exit(1)
    
    print(f"Scanning directory: {directory}")
    scan_directory(directory)
    print("Scan complete.")