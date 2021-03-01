from cryptography.fernet import Fernet
import json


class DataCipher:
    def __init__(self, key=None):
        if key is None:
            key = Fernet.generate_key()

        if isinstance(key, str):
            key_bytes = key.encode()
        else:
            key_bytes = key

        self.cipher = Fernet(key=key_bytes)

    def encrypt(self, data):
        utf_encoded_str = json.dumps(data).encode("utf-8")
        return self.cipher.encrypt(bytes(utf_encoded_str))

    def decrypt(self, encrypted_data):
        if isinstance(encrypted_data, str):
            encrypted_data = bytes(encrypted_data, "utf-8")

        json_str = self.cipher.decrypt(encrypted_data)
        return json.loads(json_str)
