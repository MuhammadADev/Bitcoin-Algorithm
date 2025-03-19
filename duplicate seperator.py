import os

# Define the input files
file1 = "Addresses_f_range_2.txt"  # Replace with your actual file names
file2 = "Addresses f range 2.txt"
file3 = "Addresses f range 1.txt"

# Define the output files for unique entries and duplicates
unique_output_file = "unique_addresses.txt"
duplicates_output_file = "duplicates.txt"

# Set to store unique keys and addresses
unique_entries = set()
# Set to store duplicates
duplicate_entries = set()

# Function to read a file and add its entries to the unique set
def read_file(file_name):
    with open(file_name, "r") as f:
        for line in f:
            # Split the line into private key and address
            parts = line.strip().split(", ")
            if len(parts) == 2:
                private_key_hex = parts[0].split(": ")[1]
                address = parts[1].split(": ")[1]
                entry = (private_key_hex, address)

                # Check if the entry is already in unique_entries
                if entry in unique_entries:
                    duplicate_entries.add(entry)  # Add to duplicates if already seen
                else:
                    unique_entries.add(entry)  # Add to unique entries

# Read all three files
read_file(file1)
read_file(file2)
read_file(file3)

# Write unique entries to the output file
with open(unique_output_file, "w") as f:
    for private_key_hex, address in unique_entries:
        f.write(f"Private Key (Hex): {private_key_hex}, Address: {address}\n")

# Write duplicates to the duplicates output file
with open(duplicates_output_file, "w") as f:
    for private_key_hex, address in duplicate_entries:
        f.write(f"Private Key (Hex): {private_key_hex}, Address: {address}\n")

print(f"Unique entries have been written to {unique_output_file}.")
print(f"Duplicates have been written to {duplicates_output_file}.")
