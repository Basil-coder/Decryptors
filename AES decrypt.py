from cryptography.fernet import Fernet

# Read the encrypted data from a file
with open("encrypted_file.txt", "rb") as file:
    encrypted_data = file.read()

# Create a Fernet cipher using the generated key
cipher = Fernet(key)

# Decrypt the data
decrypted_data = cipher.decrypt(encrypted_data)

# Print the original and decrypted data
print("Original data: ", b"Sensitive data")
print("Decrypted data: ", decrypted_data)
