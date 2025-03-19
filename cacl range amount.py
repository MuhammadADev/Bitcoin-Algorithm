# Define the start and end values in hexadecimal
start_hex = "8ffffffffffffffff"
end_hex = "fffffffffffffffff"

# Convert hexadecimal to decimal
start_int = int(start_hex, 16)
end_int = int(end_hex, 16)

# Calculate the total number of keys
total_keys = end_int - start_int + 1

print(f"Total number of possible keys in the range: {total_keys}")
