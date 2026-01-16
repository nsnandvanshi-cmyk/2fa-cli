import base64
import hashlib
from cryptography.fernet import Fernet

def _derive_key(password: str) -> bytes:
    """
    Derive a symmetric encryption key from password.
    """
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt(plaintext: str, password: str) -> str:
    key = _derive_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(plaintext.encode()).decode()

def decrypt(ciphertext: str, password: str) -> str:
    key = _derive_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(ciphertext.encode()).decode()

# crypto.py
import os, base64
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet

def derive_key(password: str, salt: bytes) -> bytes:
    return Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
    ).derive(password.encode())

def encrypt(data: bytes, key: bytes) -> bytes:
    return Fernet(base64.urlsafe_b64encode(key)).encrypt(data)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(base64.urlsafe_b64encode(key)).decrypt(token)
