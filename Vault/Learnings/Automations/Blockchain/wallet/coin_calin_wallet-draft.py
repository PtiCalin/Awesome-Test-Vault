# 🔐 Calin Coin Wallet Onboarding – Password + 2FA (TOTP)

"""
This system securely generates a cryptographic key pair from a user-provided password and a TOTP code (2FA).
It avoids mnemonic phrases and uses a hardened key derivation + identity abstraction model.
"""

import os
import time
import base64
import hashlib
import hmac
from getpass import getpass
from typing import Tuple
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from ecdsa import SigningKey, SECP256k1
import pyotp

# ------------------------- ⚙️ Config ----------------------------
KDF_SALT_BYTES = 16
KDF_PARAMS = {"length": 32, "n": 2**14, "r": 8, "p": 1}  # Secure but fast for demo
TOTP_ISSUER = "CalinCoin"

# ---------------------- 🔑 Derive Private Key ---------------------
def derive_private_key(password: str, totp_code: str, salt: bytes) -> bytes:
    """
    Derives a private key using password + TOTP (2FA) input via scrypt.
    """
    secret = f"{password}:{totp_code}".encode("utf-8")
    kdf = Scrypt(
        salt=salt,
        length=KDF_PARAMS["length"],
        n=KDF_PARAMS["n"],
        r=KDF_PARAMS["r"],
        p=KDF_PARAMS["p"]
    )
    return kdf.derive(secret)

# --------------------- 🪙 Generate Key Pair -----------------------
def generate_key_pair(private_key_bytes: bytes) -> Tuple[str, str]:
    sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
    vk = sk.get_verifying_key()
    return sk.to_string().hex(), vk.to_string().hex()

# ------------------- 📱 TOTP Setup Helper ------------------------
def setup_totp(user_email: str) -> str:
    totp = pyotp.TOTP(pyotp.random_base32())
    uri = totp.provisioning_uri(name=user_email, issuer_name=TOTP_ISSUER)
    print("\n📱 Add to your 2FA app (Google Authenticator, Aegis, etc):")
    print(uri)
    return totp.secret

# ------------------------- 🚀 Demo Flow --------------------------
if __name__ == "__main__":
    print("\n🔐 Calin Coin Wallet Setup")
    email = input("Enter your email address (for 2FA setup): ")
    secret = setup_totp(email)

    print("\n✅ Now let's derive your wallet keys")
    password = getpass("Enter a strong password: ")
    time.sleep(1)
    totp_code = input("Enter your current TOTP code (from 2FA app): ")

    salt = os.urandom(KDF_SALT_BYTES)
    priv_bytes = derive_private_key(password, totp_code, salt)
    priv_key, pub_key = generate_key_pair(priv_bytes)

    print("\n🔐 Private Key:", priv_key)
    print("📬 Public Key:", pub_key)
    print("🧂 Salt (save this!):", salt.hex())
    print("\n🔑 Your wallet is ready! Keep your keys and salt safe."
          )