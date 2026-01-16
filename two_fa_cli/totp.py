import pyotp

def generate_totp(secret: str) -> str:
    """
    Generate a 30-second TOTP code.
    """
    totp = pyotp.TOTP(secret)
    return totp.now()
