# 🧪 Calin Coin Test Log

Vault Test Record – Version **b**  
Target Script: `calin_coin-b.py`  
Test Environment: Python 3.13 on Windows 11  
Random Seeds: `random.seed(99)`  , `random.seed(42)`  

---

## ✅ Testing Checklist

- [x] **RUN TEST:** Does it run without syntax or logic errors?
- [x] **DETERMINATION TEST:** Is the output deterministic? (Alice and Bob totals always same)
- [x] **BLOCK CORRUPTION TEST:** Try corrupting a block hash — does `checkChain()` catch it?
- [x] **INVALID TRANSACTION TEST:** Try adding an invalid transaction manually — is it rejected?
- [x] **MANUAL TAMPER TEST:** Edit a transaction value directly and check if chain fails  
  `chain[1]['contents']['txns'][0]['Alice'] = 5000`

---

## 🧾 Version Matrix

| Test / Version         | a   | b   | c   |
| ---------------------- | --- | --- | --- |
| Run                    | ✅   | ✅   |     |
| Determination (RS: 99) | ✅   | ✅   |     |
| Block Corruption       | ✅   | ✅   |     |
| Invalid Transaction    | ✅   | ✅   |     |
| Manual Tamper          | ✅   | ✅   |     |

---

## 🔬 Test Run Documentation

### 🧪 RUN TEST

**Command:**  
`python calin_coin-b.py`

**Output:**  
```
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 33, 'Bob': 67}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: 974a00bd25c35bf9c3b11383e3c9dcb9e00a5f51655ffd9c026eff682f2b82fe
```

**Conclusion:**  
✅ Script executes without errors  
✅ Blockchain initializes and final state is printed  
✅ Block structure and hashes generate without issue

---

### 🧪 DETERMINATION TEST

**Goal:** Confirm that output remains consistent across multiple runs.

**Output Sample:**  
```
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 33, 'Bob': 67}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: 974a00bd25c35bf9c3b11383e3c9dcb9e00a5f51655ffd9c026eff682f2b82fe
```

**Conclusion:**  
✅ Consistent results across multiple runs **within the same seed**  
✅ Different seeds produce different but stable outputs

---

### 🧪 BLOCK CORRUPTION TEST

**Injected Code:**  
```python 
chain[1]['hash'] = "deadbeef0000000000000000000000000000000000000000000000000000000000"
```

**Output:**  
```
ValueError: Block 1 hash mismatch
```

**Conclusion:**  
✅ The corrupted hash was detected immediately  
✅ `validate_block_hash()` raised a `ValueError`  
✅ Chain integrity is fully enforced through hash linkage  
🛡️ No silent corruption — Calin Coin blocks are secure by design

---

### 🧪 INVALID TRANSACTION TEST

**Injected Transaction:**  
```python
txn_pool.insert(0, {"Alice": -999, "Bob": 500})  # Invalid: net ≠ 0
```

**Debug Print Output:**  
```
❌ INVALID: {'Alice': -999, 'Bob': 500}
```

**Conclusion:**  
✅ Transaction validation system correctly identified imbalance  
✅ Invalid transaction was skipped and not added to chain  
✅ Chain integrity maintained throughout  
🛡️ Rejection is silent and safe — blockchain is protected from bad input

---

### 🧪 MANUAL TAMPER TEST

**Manual Mutation:**  
```python
chain[1]['contents']['txns'][0]['Alice'] = 5000
```

**Output:**  
```
ValueError: Invalid transaction
```

**Conclusion:**  
✅ Manual mutation broke the transaction rules  
✅ Blockchain re-validated the logic — not just the hash  
✅ Chain failed on execution as intended  
🔐 Version b is resistant to stealth content edits



---

Last edit: 2025-05-12


*Filed under: `Calin Coin • Blockchain Security • Manual Audit`*
