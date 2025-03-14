import hashlib
import hmac
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

class EncryptionHandler:
    def __init__(self, key=None):
        self.key = key or os.urandom(32)  

    def encrypt(self, plaintext):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext  

    def decrypt(self, ciphertext):
        iv, ciphertext = ciphertext[:16], ciphertext[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return (unpadder.update(decrypted_padded) + unpadder.finalize()).decode()

class HMACSigner:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def sign_transaction(self, data):
        return hmac.new(self.secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

    def verify_signature(self, data, signature):
        expected_sig = self.sign_transaction(data)
        return hmac.compare_digest(expected_sig, signature)
