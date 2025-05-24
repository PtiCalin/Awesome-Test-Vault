
"""
🪙 Calin Coin – Educational Blockchain Demo in Python
Author: PtiCalin ✨

This educational blockchain simulates:
- Transactions between accounts (Alice & Bob)
- Validated, immutable blocks
- A fully linked and hash-verified chain

This system demonstrates:
✅ State tracking
✅ Transaction validation
✅ Block creation
✅ Blockchain verification
"""

import hashlib, json, sys, random, copy
from typing import Dict, List, Any, Union

# ============================== 🔒 HASHING ==============================
def hash_object(obj: Union[str, Dict]) -> str:
    """
    Computes a consistent SHA-256 hash of a JSON-like object.
    """
    if not isinstance(obj, str):
        obj = json.dumps(obj, sort_keys=True)
    return hashlib.sha256(obj.encode("utf-8")).hexdigest()

# =========================== 💸 TRANSACTIONS ===========================

def create_transaction(max_value: int = 3) -> Dict[str, int]:
    sign = random.choice([-1, 1])
    amount = random.randint(1, max_value)
    return {"Alice": sign * amount, "Bob": -sign * amount}

def generate_transaction_pool(size: int = 30) -> List[Dict[str, int]]:
    random.seed(42)
    return [create_transaction() for _ in range(size)]

# ============================ 📊 STATE ============================

def update_state(txn: Dict[str, int], current_state: Dict[str, int]) -> Dict[str, int]:
    updated = current_state.copy()
    for account, delta in txn.items():
        updated[account] = updated.get(account, 0) + delta
    return updated

def is_valid_transaction(txn: Dict[str, int], state: Dict[str, int]) -> bool:
    if sum(txn.values()) != 0:
        return False
    for account, change in txn.items():
        if state.get(account, 0) + change < 0:
            return False
    return True

# =========================== ⛓️ BLOCK CREATION ===========================

def create_genesis_block() -> (Dict[str, Any], Dict[str, int]):
    state = {"Alice": 50, "Bob": 50}
    contents = {
        "blockNumber": 0,
        "parentHash": None,
        "txnCount": 1,
        "txns": [state]
    }
    return {"hash": hash_object(contents), "contents": contents}, state

def create_block(txns: List[Dict[str, int]], chain: List[Dict[str, Any]]) -> Dict[str, Any]:
    parent = chain[-1]
    number = parent["contents"]["blockNumber"] + 1
    contents = {
        "blockNumber": number,
        "parentHash": parent["hash"],
        "txnCount": len(txns),
        "txns": txns
    }
    return {"hash": hash_object(contents), "contents": contents}

# =========================== ✅ VALIDATION ============================

def validate_block_hash(block: Dict[str, Any]) -> None:
    if block["hash"] != hash_object(block["contents"]):
        raise ValueError(f"Block {block['contents']['blockNumber']} hash mismatch")

def validate_block(block, parent, state):
    if block["contents"]["blockNumber"] != parent["contents"]["blockNumber"] + 1:
        raise ValueError("Block number error")
    if block["contents"]["parentHash"] != parent["hash"]:
        raise ValueError("Parent hash mismatch")
    for txn in block["contents"]["txns"]:
        if not is_valid_transaction(txn, state):
            raise ValueError("Invalid transaction")
        state = update_state(txn, state)
    validate_block_hash(block)
    return state

def validate_chain(chain_data: Union[str, List[Dict[str, Any]]]) -> Dict[str, int]:
    if isinstance(chain_data, str):
        chain_data = json.loads(chain_data)
    state = {}
    for txn in chain_data[0]["contents"]["txns"]:
        state = update_state(txn, state)
    validate_block_hash(chain_data[0])
    parent = chain_data[0]
    for block in chain_data[1:]:
        state = validate_block(block, parent, state)
        parent = block
    return state

# ============================ 🚀 RUN SYSTEM =============================

if __name__ == "__main__":
    print("🚀 Booting up Calin Coin educational blockchain...")
    txn_pool = generate_transaction_pool()
    chain = []
    genesis, state = create_genesis_block()
    chain.append(genesis)
    BLOCK_SIZE = 5

    while txn_pool:
        batch = []
        while txn_pool and len(batch) < BLOCK_SIZE:
            txn = txn_pool.pop()
            if is_valid_transaction(txn, state):
                batch.append(txn)
                state = update_state(txn, state)
        if batch:
            chain.append(create_block(batch, chain))

    final_state = validate_chain(chain)
    print("✅ Calin Coin Chain Validated!")
    print("📦 Final Blockchain State:", final_state)
    print("🔗 Genesis Block Hash:", chain[0]["hash"])
    print("🔗 First Real Block Hash:", chain[1]["hash"])
