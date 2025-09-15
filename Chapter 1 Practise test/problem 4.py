import os

# Specify the directory path (you can change this to any path you like)
directory_path = "/"

try:
    # List all entries in the directory
    contents = os.listdir(directory_path)
    
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
