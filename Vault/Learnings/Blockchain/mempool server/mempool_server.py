# 🧠 Calin Coin – Mempool Server
# Language: Python 3

import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, List
from ecdsa import VerifyingKey, SECP256k1
import random

# ------------------- 📦 In-Memory Mempool -------------------
mempool: List[Dict] = []

# ------------------- 💌 Affirmations & Errors -------------------
ACCEPT_MESSAGES = [
    "✅ Transaction accepted into the mempool! Sending digital hugs 💞",
    "🎉 Your transaction just entered the cuddle queue!",
    "💖 We've gently placed your transaction in the mempool basket.",
    "🌼 Verified and stored – your coin just made a new friend.",
    "📬 Mempool welcomes your transaction with warm vibes."
]

REJECT_MESSAGES = [
    "❌ Could not verify the transaction signature. Please try again 🕊️",
    "💔 Your transaction couldn’t be accepted right now – check the signature!",
    "⚠️ That transaction didn’t pass our hug filter. 🧸",
    "🧩 Something was off. Make sure your keys and data align.",
    "😢 Verification failed. But hey, we still believe in you."
]

# ------------------- 🔐 Signature Check -------------------
def verify_transaction_signature(txn: Dict) -> bool:
    try:
        signature = bytes.fromhex(txn.pop("signature"))
        message = json.dumps(txn, sort_keys=True).encode("utf-8")
        vk = VerifyingKey.from_string(bytes.fromhex(txn["sender"]), curve=SECP256k1)
        return vk.verify(signature, message)
    except Exception:
        return False

# ------------------- 🌐 HTTP Server Handler -------------------
class MempoolHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        raw_data = self.rfile.read(content_length)
        try:
            txn = json.loads(raw_data)
            if verify_transaction_signature(txn):
                mempool.append(txn)
                self.respond(200, {"message": random.choice(ACCEPT_MESSAGES)})
            else:
                self.respond(400, {"message": random.choice(REJECT_MESSAGES)})
        except Exception as e:
            self.respond(500, {"error": str(e)})

    def do_GET(self):
        self.respond(200, {"mempool": mempool})

    def respond(self, code: int, data: Dict):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

# ------------------- 🚀 Launch Server -------------------
def run_server(port: int = 8080):
    print(f"\n🚀 Mempool server listening on port {port}... ⛓️")
    server = HTTPServer(("", port), MempoolHandler)
    server.serve_forever()

if __name__ == "__main__":
    run_server()
