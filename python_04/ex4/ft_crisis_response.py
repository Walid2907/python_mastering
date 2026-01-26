print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
# try to open a non-existing  file
try:
    with open("lost_archive.txt", "r") as file:
        file.read()
except FileNotFoundError:
    print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
# try to open a non-allowed file
# will need to use os here for easy use
# by creating file then os.chmod("readonly.txt", 0o444)  # Make file read-only
# and then try to write to it again
try:
    with open("classified_vault.txt", "w") as file:
        file.write("bamoos")
except PermissionError:
    print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
# try to open an exiting file, but we secured it using try except
try:
    with open("standard_archive.txt", "r") as file:
        data = file.read()
except PermissionError:
    print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")
    print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")
except FileNotFoundError:
    print("CRISIS ALERT: Attempting access to 'standard_archive.txt'...")
    print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable\n")
else:
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    print(f"SUCCESS: Archive recovered - ``{data}''")
    print("STATUS: Normal operations resumed\n")

print("All crisis scenarios handled successfully. Archives secure.")
