hex_string = "68 65 6c 6c 6f 20 77 6f 72 6c 64 20 69 6e 20 74 68 65 20 73 65 72 69 61 6c 20 71 75 65 75 65 20 64 65 63 6f 64 65 64 20 77 69 74 68 20 6d 69 73 73 69 6e 67 20 70 69 65 63 65 73 2e"
bytes_representation = bytes.fromhex(hex_string)    
decoded_string = bytes_representation.decode("utf-8")
print(decoded_string)