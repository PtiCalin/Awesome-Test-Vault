import time
import hashlib
import json
from typing import Dict, Any
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# ------------------- ✨ Transaction Creation --------------------
def make_transaction(sender: str, recipient: str, amount: float, fee: float, nonce: int, sk: SigningKey) -> Dict[str, Any]:
    """
    Create a cozy Calin Coin transaction and sign it with your private key.
    """
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
        # Copy only the transaction body (no signature)
        txn_copy = {k: v for k, v in txn.items() if k != "signature"}
        message = json.dumps(txn_copy, sort_keys=True).encode("utf-8")
        return vk.verify(bytes.fromhex(txn["signature"]), message)
    except Exception as e:
        print("⚠️ Signature validation failed:", e)
        return False

# ------------------- 🧪 Test Transaction --------------------
if __name__ == "__main__":
    print("\n💌 Let's make a gentle Calin Coin transfer")
    
    # Generate temporary keys for demo
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()

    sender = "CAL1abc123"
    recipient = "CAL1xyz789"
    amount = 5.0
    fee = 0.01
    nonce = 1

    txn = make_transaction(sender, recipient, amount, fee, nonce, sk)
    print("\n📤 Transaction Created:", json.dumps(txn, indent=2))

    print("\n🔐 Verifying signature...")
    if is_transaction_signature_valid(txn, vk):
        print("✅ Signature is valid! 🥳")
    else:
        print("❌ Signature check failed")