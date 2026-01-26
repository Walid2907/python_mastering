print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

print("SECURE EXTRACTION:")
with open("../data-generator-tools/classified_data.txt", "r") as file:
    data = file.read()
print(data)

print("\nSECURE PRESERVATION:")
to_add = "{[}CLASSIFIED{]} New security protocols archived\n"
with open("../data-generator-tools/classified_data.txt", "a") as file:
    file.write(to_add)

print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
