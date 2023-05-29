
from Crypto.Cipher import DES

# Define the key (8 bytes)
key = b'secretke'
# Create a DES cipher object
cipher = DES.new(key, DES.MODE_ECB)

# Define the plaintext (must be a multiple of 8 bytes)
plaintext = b'This is a secret'

# Pad the plaintext to a multiple of 8 bytes
padding_length = 8 - (len(plaintext) % 8)
plaintext += bytes([padding_length]) * padding_length

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decrypted_plaintext = cipher.decrypt(ciphertext)  

# Remove the padding from the decrypted plaintext
padding_length = decrypted_plaintext[-1]
decrypted_plaintext = decrypted_plaintext[:-padding_length]

# Print the results
print("Original text:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_plaintext)
