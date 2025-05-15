# 💖 Calin Coin – CLI Wallet Interface
# Language: Python 3

import time
import hashlib
import json
import random
from typing import Dict, Any
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# ------------------- 💌 Affirmations & UX Touches --------------------
SUCCESS_MESSAGES = [
    "✅ Signature is valid! Your transaction is wrapped in a cosmic hug 🧸✨",
    "🌈 Everything checks out! Calin Coin vibes are strong 💖",
    "🥳 Transaction verified! The universe approves 💫",
    "✨ Your signature sparkled through verification!",
    "🌻 Signed, sealed, and joyfully verified!"
]

FAILURE_MESSAGES = [
    "❌ Oops... That signature didn’t pass the Calin cuddle check 😿",
    "🧩 Verification failed – something’s not quite right. Try again 💭",
    "⚠️ Signature didn’t match. Breathe. Double-check your inputs 🕊️",
    "💔 The signature couldn’t be validated. Let’s gently investigate 💡",
    "😶 Hmm... we hit a bump verifying the signature. Still proud of you!"
]

# ------------------- ✨ Transaction Creation --------------------
def make_transaction(sender: str, recipient: str, amount: float, fee: float, nonce: int, sk: SigningKey) -> Dict[str, Any]:
    txn = {
        "type": "transfer",
        "timestamp": int(time.time()),
        "sender": sender,
        "recipient": recipient,
        "amount": amount,
        "fee": fee,
        "nonce": nonce
    }
    message = json.dumps(txn, sort_keys=True).encode("utf-8")
    signature = sk.sign(message).hex()
    txn["signature"] = signature
    return txn

# ------------------- 🔎 Signature Verification -------------------
def is_transaction_signature_valid(txn: Dict[str, Any], vk: VerifyingKey) -> bool:
    try:
        txn_copy = {k: v for k, v in txn.items() if k != "signature"}
        message = json.dumps(txn_copy, sort_keys=True).encode("utf-8")
        return vk.verify(bytes.fromhex(txn["signature"]), message)
    except Exception as e:
        print(random.choice(FAILURE_MESSAGES))
        print("📎 Debug info:", e)
        return False

# ------------------- 🧠 Calin Wallet CLI -------------------
def wallet_cli():
    print("\n🌸 Welcome to your Calin Coin CLI Wallet")
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()

    sender = input("👤 Your wallet address: ")
    recipient = input("🎁 Recipient wallet address: ")
    amount = float(input("💰 Amount to send: "))
    fee = float(input("🧂 Transaction fee: "))
    nonce = int(input("🔢 Transaction nonce: "))

    txn = make_transaction(sender, recipient, amount, fee, nonce, sk)
    print("\n📤 Transaction Created:")
    print(json.dumps(txn, indent=2))

    print("\n🔐 Verifying signature...")
    if is_transaction_signature_valid(txn, vk):
        print(random.choice(SUCCESS_MESSAGES))
    else:
        print("❗ Verification failed. Try again!")

# ------------------- 🚀 Launch --------------------
if __name__ == "__main__":
    wallet_cli()
# 💖 Calin Coin – CLI Wallet Interface


