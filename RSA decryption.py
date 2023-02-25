from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Read the encrypted data from a file
with open("encrypted_file.txt", "rb") as file:
    encrypted_data = file.read()

# Read the private key from a file
with open("private_key.pem", "rb") as file:
    private_pem = file.read()

# Load the private key
private_key = load_pem_private_key(
    private_pem,
    password=None
)

# Decrypt the data using the private key
decrypted_data = private_key.decrypt(
    encrypted_data,
   
