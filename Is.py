# Define the input string
input_string = "Swanand Kulkarni"

# Initialize the result strings
and_result = ""
xor_result = ""

# Loop through each character in the input string
for char in input_string:
    # Apply the AND operation with 127
    and_value = ord(char) & 127
    # Apply the XOR operation with 127
    xor_value = ord(char) ^ 127
    
    # Append the result to the appropriate string
    and_result += chr(and_value)
    xor_result += chr(xor_value)

# Print the results
print("Input string:", input_string)
print("AND result:", and_result)
print("XOR result:", xor_result)
