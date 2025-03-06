# Define the input and output file names
input_file = "random_keys_with_addresses.txt"
output_file = "sorted_keys_with_addresses.txt"

# Read the addresses from the input file
with open(input_file, "r") as f:
    lines = f.readlines()

# Extract the private keys and addresses from the lines
addresses = []
for line in lines:
    # Split the line to get the private key and address
    parts = line.strip().split(", ")
    if len(parts) == 2:
        private_key = parts[0].split(": ")[1]  # Extract the private key
        address = parts[1].split(": ")[1]      # Extract the address
        addresses.append((private_key, address))

# Sort the addresses based on the private key (hexadecimal value)
sorted_addresses = sorted(addresses, key=lambda x: x[0])

# Write the sorted addresses to the output file
with open(output_file, "w") as f:
    for private_key, address in sorted_addresses:
        f.write(f"Private Key (Hex): {private_key}, Address: {address}\n")

print(f"Sorted addresses have been saved to {output_file}.")
