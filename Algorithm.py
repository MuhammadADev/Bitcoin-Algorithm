import random
import bitcoin

# Define the range for the private keys
start_int = int("100000000000000000", 16)  # Starting value in decimal
end_int = int("1fffffffffffffffff", 16)    # Ending value in decimal

# Define the output file
output_file = "random_keys_with_addresses.txt"

# Number of random keys to generate
num_keys_to_generate = 100000000000000000  # You can change this to generate more or fewer keys

# Generate random keys and save them to the file
with open(output_file, "w") as f:
    for _ in range(num_keys_to_generate):
        # Generate a random integer within the specified range
        random_private_key_int = random.randint(start_int, end_int)
        
        # Convert the integer to a hexadecimal string
        random_private_key_hex = hex(random_private_key_int)[2:].zfill(64)  # Ensure it's 64 characters long
        
        # Generate the public key from the private key
        public_key = bitcoin.privkey_to_pubkey(random_private_key_hex)

        # Generate the compressed public key
        if public_key[-1] in ['0', '2', '4', '6', '8', 'A', 'C', 'E']:  # Check if y-coordinate is even
            compressed_public_key = '02' + public_key[2:66]  # Prefix with 0x02 and take the x-coordinate
        else:
            compressed_public_key = '03' + public_key[2:66]  # Prefix with 0x03 and take the x-coordinate

        # Generate the Bitcoin address from the compressed public key
        address = bitcoin.pubkey_to_address(compressed_public_key)

        # Write the private key and address to the file
        f.write(f"Private Key (Hex): {random_private_key_hex}, Address: {address}\n")

print(f"Generated {num_keys_to_generate} random private keys and their corresponding addresses, saved to {output_file}.")
