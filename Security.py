from cryptography.fernet import Fernet

def generate_key_pair():
    private_key = Fernet.generate_key()
    public_key = Fernet.generate_key()
    return private_key, public_key

def encrypt(data, public_key):
    cipher_suite = Fernet(public_key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

def decrypt(encrypted_data, private_key):
    cipher_suite = Fernet(private_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return decrypted_data

