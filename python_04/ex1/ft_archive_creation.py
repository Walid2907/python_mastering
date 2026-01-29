data = ("{[}ENTRY 001{]} New quantum algorithm discovered \n"
        "{[}ENTRY 002{]} Efficiency increased by 347% \n"
        "{[}ENTRY 003{]} Archived by Data Archivist trainee\n")

print("Initializing new storage unit: new_discovery.txt")
print("Storage unit created successfully...\n")

print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
file = open("new_discovery.txt", "w")
file.write(data)

print("Inscribing preservation data...")
print(data)
print("Data inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")
file.close()
