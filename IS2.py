# Define the substitution cipher
substitution_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm',
    ' ': ' '
}

# Define the encryption function
def encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        # Check if the character is in the substitution dictionary
        if char.lower() in substitution_dict:
            # If yes, substitute the character
            ciphertext += substitution_dict[char.lower()]
        else:
            # If not, leave it as is
            ciphertext += char
    return ciphertext

# Define the decryption function
def decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        # Check if the character is in the inverse substitution dictionary
        if char.lower() in [v.lower() for v in substitution_dict.values()]:
            # If yes, substitute the character
            for k, v in substitution_dict.items():
                if v.lower() == char.lower():
                    plaintext += k
                    break
        else:
            # If not, leave it as is
            plaintext += char
    return plaintext

# Test the functions
plaintext = "Lalit Pawar"
ciphertext = encrypt(plaintext)
decrypted_plaintext = decrypt(ciphertext)

print("Original text:", plaintext)
print("Encrypted text:", ciphertext)
print("Decrypted text:", decrypted_plaintext)
