from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

KEY = b'securefileaes128'  # exactly 16 characters

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def encrypt_file(file_data):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(file_data))
    return cipher.iv + ciphertext

def decrypt_file(encrypted_data):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return cipher.decrypt(ciphertext).rstrip(b' ')
