
# 🧪 Calin Coin Test Log

Vault Test Record – Version **a**  
Target Script: `calin_coin-a.py`  
Test Environment: Python 3.13 on Windows 11  
Random Seeds: `random.seed(99)`  , `random.seed(42)`  

---

## ✅ Testing Checklist

- [x] **RUN TEST:** Does it run without syntax or logic errors?
- [x] **DETERMINATION TEST:** Is the output deterministic? (Alice and Bob totals always same)
- [x] **BLOCK CORRUPTION TEST:** Try corrupting a block hash — does `checkChain()` catch it?
- [x] **INVALID TRANSACTION TEST:** Try adding an invalid transaction manually — is it rejected?
- [x] **MANUAL TAMPER TEST:** Edit a transaction value directly and check if chain fails
  ```python
  chain[1]['contents']['txns'][0]['Alice'] = 5000
  ```

---

## 🧾 Version Matrix

| Test / Version         | a   | b   | c   |
| ---------------------- | --- | --- | --- |
| Run                    | ✅   |     |     |
| Determination (RS: 99) | ✅   |     |     |
| Block Corruption       | ✅   |     |     |
| Invalid Transaction    | ✅   |     |     |
| Manual Tamper          | ✅   |     |     |

---

## 🔬 Test Run Documentation

### 🧪 RUN TEST

**Command:**
```shell
python calin_coin-a.py
```

**Output:**
```
✅ Calin Coin chain successfully validated.
Final state: {'Alice': 72, 'Bob': 28}
Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
Block #1 Hash: 7a91fc8206c5351293fd11200b33b7192e87fad6545504068a51aba868bc6f72
```

**Conclusion:**  
Script runs without errors. Hashes and final state match expected behavior.

---

### 🧪 DETERMINATION TEST

**Goal:** Confirm that output remains consistent across multiple runs.

**Output Sample (x5 runs):**
```
Final state: {'Alice': 72, 'Bob': 28}
Block #1 Hash: 7a91fc8206c5351293fd11200b33b7192e87fad6545504068a51aba868bc6f72
```

**Conclusion:**  
Deterministic behavior confirmed with fixed seed (`random.seed(99)`).

---

### 🧪 BLOCK CORRUPTION TEST

**Injected Code:**
```python
chain[1]['hash'] = "badcafedeadbeef1234567890"
```

**Output:**
```
Exception: Hash does not match contents of block 1
```

**Conclusion:**  
Tampering with a block’s hash triggers an exception as expected.

---

### 🧪 INVALID TRANSACTION TEST

**Injected Transaction:**
```python
txnBuffer.insert(0, {'Alice': -5, 'Bob': 2})  # Invalid: net ≠ 0
```

**Debug Print Output:**
```
❌ Invalid transaction skipped: {'Alice': -5, 'Bob': 2}
✅ Calin Coin chain successfully validated.
```

**Conclusion:**  
Invalid transaction was detected and not included in the chain. Chain integrity preserved.

---

### 🧪 MANUAL TAMPER TEST

**🔍 GOAL**
Modify a transaction _after_ it’s been added to a block, and check if `checkChain()` detects the tampering.
```python
chain[1]['contents']['txns'][0]['Alice'] = 5000
```

**Results:**  
Exception: Invalid transaction in block 1: {'Alice': 5000, 'Bob': 2}
✅ Manual tampering was successfully detected.  
✅ Chain verification failed as designed — mutation rejected.  
✅ The system revalidates each block’s transactions, not just the hash.  
🔒 Calin Coin is tamper-aware and secure-by-default.


---

**Last updated:** 2025-05-12

---

*Filed under: `Calin Coin • Blockchain Security • Manual Audit`*
