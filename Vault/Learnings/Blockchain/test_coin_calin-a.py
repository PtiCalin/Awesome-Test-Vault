
# 🪙 Calin Coin – A Minimal Blockchain Implementation in Python

import hashlib, json, sys, random, copy

# === Step 1: Helper hash function ===
def hashMe(msg=""):
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)
    return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()

# === Step 2: Transaction creation ===
random.seed(99)
def makeTransaction(maxValue=3):
    sign = int(random.getrandbits(1)) * 2 - 1
    amount = random.randint(1, maxValue)
    alicePays = sign * amount
    bobPays = -1 * alicePays
    return {'Alice': alicePays, 'Bob': bobPays}

txnBuffer = [makeTransaction() for _ in range(30)]

# 🔥 Add an invalid transaction that doesn't balance (sum ≠ 0)
txnBuffer.insert(0, {'Alice': -5, 'Bob': 2})  # Invalid: net -3

# === Step 3: State management ===
def updateState(txn, state):
    state = state.copy()
    for key in txn:
        state[key] = state.get(key, 0) + txn[key]
    return state

def isValidTxn(txn, state):
    if sum(txn.values()) != 0:
        return False
    for key in txn:
        if state.get(key, 0) + txn[key] < 0:
            return False
    return True

# === Step 4: Genesis block ===
state = {'Alice': 50, 'Bob': 50}
genesisBlockTxns = [state]
genesisBlockContents = {
    'blockNumber': 0,
    'parentHash': None,
    'txnCount': 1,
    'txns': genesisBlockTxns
}
genesisHash = hashMe(genesisBlockContents)
genesisBlock = {'hash': genesisHash, 'contents': genesisBlockContents}
chain = [genesisBlock]

# === Step 5: Block creation function ===
def makeBlock(txns, chain):
    parentBlock = chain[-1]
    blockNumber = parentBlock['contents']['blockNumber'] + 1
    blockContents = {
        'blockNumber': blockNumber,
        'parentHash': parentBlock['hash'],
        'txnCount': len(txns),
        'txns': txns
    }
    blockHash = hashMe(blockContents)
    return {'hash': blockHash, 'contents': blockContents}

# === Step 6: Process transactions into blocks ===
blockSizeLimit = 5
while txnBuffer:
    txnList = []
    while txnBuffer and len(txnList) < blockSizeLimit:
        newTxn = txnBuffer.pop()
        if isValidTxn(newTxn, state):
            print("✅ Valid transaction added:", newTxn)
            txnList.append(newTxn)
            state = updateState(newTxn, state)
        else:
            print("❌ Invalid transaction skipped:", newTxn)
    if txnList:
        chain.append(makeBlock(txnList, chain))

# === Step 7: Blockchain verification functions ===
def checkBlockHash(block):
    if block['hash'] != hashMe(block['contents']):
        raise Exception(f"Hash does not match contents of block {block['contents']['blockNumber']}")

def checkBlockValidity(block, parent, state):
    if block['contents']['blockNumber'] != parent['contents']['blockNumber'] + 1:
        raise Exception("Block number error")
    if block['contents']['parentHash'] != parent['hash']:
        raise Exception("Parent hash mismatch")
    for txn in block['contents']['txns']:
        if isValidTxn(txn, state):
            state = updateState(txn, state)
        else:
            raise Exception(f"Invalid transaction in block {block['contents']['blockNumber']}: {txn}")
    checkBlockHash(block)
    return state
# 💣 Tamper with a transaction value AFTER block is created
chain[1]['contents']['txns'][0]['Alice'] = 5000

def checkChain(chain):
    if type(chain) == str:
        try:
            chain = json.loads(chain)
        except:
            return False
    elif type(chain) != list:
        return False
    state = {}
    for txn in chain[0]['contents']['txns']:
        state = updateState(txn, state)
    checkBlockHash(chain[0])
    parent = chain[0]
    for block in chain[1:]:
        state = checkBlockValidity(block, parent, state)
        parent = block
    return state

# === Output Final Chain Info ===
if __name__ == "__main__":
    # 💣 Tamper with a block AFTER creation
    chain[1]['contents']['txns'][0]['Alice'] = 5000

    # ⛓️ Validate the (now tampered) chain
    final_state = checkChain(chain)
    print("✅ Calin Coin chain successfully validated.")
    print(f"Final state: {final_state}")
    print(f"Genesis Block Hash: {chain[0]['hash']}")
    print(f"Block #1 Hash: {chain[1]['hash']}")

