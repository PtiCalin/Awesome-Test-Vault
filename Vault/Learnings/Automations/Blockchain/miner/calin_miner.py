# 💎 Calin Coin – Miner Node
# Language: Python 3

import time
import json
import hashlib
import threading
import requests
from typing import List, Dict, Any
from http.server import HTTPServer, BaseHTTPRequestHandler

MEMPOOL_URL = "http://localhost:8080/"
MINING_INTERVAL = 10  # seconds
BLOCKCHAIN_FILE = "calin_chain.json"

# --------------------------- 🔗 Hashing ---------------------------
def hash_block(block: Dict[str, Any]) -> str:
    block_string = json.dumps(block, sort_keys=True).encode("utf-8")
    return hashlib.sha256(block_string).hexdigest()

# ------------------------ ⛓️ Block Creation ------------------------
def create_block(transactions: List[Dict[str, Any]], parent_hash: str, block_number: int) -> Dict[str, Any]:
    block_contents = {
        "blockNumber": block_number,
        "parentHash": parent_hash,
        "txnCount": len(transactions),
        "txns": transactions,
        "timestamp": int(time.time())
    }
    block_hash = hash_block(block_contents)
    return {"hash": block_hash, "contents": block_contents}

# ---------------------- 🧱 Blockchain State ------------------------
def load_chain() -> List[Dict[str, Any]]:
    try:
        with open(BLOCKCHAIN_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("🌱 No chain found, creating genesis block...")
        genesis_state = {"Alice": 50, "Bob": 50}
        genesis_block = create_block([genesis_state], "0" * 64, 0)
        save_chain([genesis_block])
        return [genesis_block]


def save_chain(chain: List[Dict[str, Any]]) -> None:
    with open(BLOCKCHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=2)

# ---------------------- ⛏️ Mining Loop ------------------------
def mine_block():
    while True:
        time.sleep(MINING_INTERVAL)
        try:
            resp = requests.get(MEMPOOL_URL)
            transactions = resp.json()
        except Exception as e:
            print("❌ Error fetching mempool:", e)
            continue

        if not transactions:
            print("😴 No transactions to mine.")
            continue

        chain = load_chain()
        new_block = create_block(
            transactions=transactions,
            parent_hash=chain[-1]["hash"],
            block_number=chain[-1]["contents"]["blockNumber"] + 1
        )
        chain.append(new_block)
        save_chain(chain)
        print(f"✅ Mined new block #{new_block['contents']['blockNumber']} with {len(transactions)} txns")

# --------------------- 🧠 Miner Node CLI ------------------------
if __name__ == "__main__":
    print("🪨 Calin Miner Node is running... Mining with love 💗")
    threading.Thread(target=mine_block).start()
    print("🌐 Listening for transactions...")