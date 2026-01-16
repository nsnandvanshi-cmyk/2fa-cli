import json
import os
from typing import Dict
from .crypto import encrypt, decrypt

DB_PATH = os.path.expanduser("~/.2fa-cli.json")

def load_db(password: str) -> Dict[str, str]:
    if not os.path.exists(DB_PATH):
        return {}

    with open(DB_PATH, "r") as f:
        encrypted_data = json.load(f)

    data = {}
    for name, enc_secret in encrypted_data.items():
        data[name] = decrypt(enc_secret, password)

    return data

def save_db(data: Dict[str, str], password: str) -> None:
    encrypted_data = {}
    for name, secret in data.items():
        encrypted_data[name] = encrypt(secret, password)

    with open(DB_PATH, "w") as f:
        json.dump(encrypted_data, f, indent=2)

# storage.py
import json, os, base64
from .crypto import derive_key, encrypt, decrypt

DB_PATH = os.path.expanduser("~/.2fa.db")

def save_db(db: dict, password: str):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    encrypted = encrypt(json.dumps(db).encode(), key)

    with open(DB_PATH, "w") as f:
        json.dump({
            "v": 1,
            "salt": base64.b64encode(salt).decode(),
            "data": base64.b64encode(encrypted).decode(),
        }, f)

    os.chmod(DB_PATH, 0o600)

def load_db(password: str) -> dict:
    if not os.path.exists(DB_PATH):
        return {}

    with open(DB_PATH) as f:
        obj = json.load(f)

    key = derive_key(password, base64.b64decode(obj["salt"]))
    return json.loads(decrypt(base64.b64decode(obj["data"]), key))
