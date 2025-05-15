# 🧪 Calin Coin Test Log

Vault Test Record – Version **c**  
Target Script: `calin_coin-c.py`  
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

| Test / Version      | a   | b   | c   |
| ------------------- | --- | --- | --- |
| Run                 | ✅   | ✅   | ✅   |
| Determination       | ✅   | ✅   | ✅   |
| Block Corruption    | ✅   | ✅   | ✅   |
| Invalid Transaction | ✅   | ✅   | ✅   |
| Manual Tamper       | ✅   | ✅   | ✅   |

---

## 🔬 Test Run Documentation

### 🧪 RUN TEST

**Command:**  
`python calin_coin-c.py`

**Output:**  
```python
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 39, 'Bob': 61}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: df606e997f859ec852f4946f7a849d0bb7093831d072ebe18fa18ca1df9a4c8d
```

**Conclusion:**  
✅ Script runs smoothly without syntax or runtime errors  
✅ Chain initializes and validates correctly  
✅ Genesis and first block hashes display as expected  
✅ Final state is computed and shown

---

### 🧪 DETERMINATION TEST

**Goal:** Confirm that output remains consistent across multiple runs.

**Output Sample:**  
```python
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 39, 'Bob': 61}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: df606e997f859ec852f4946f7a849d0bb7093831d072ebe18fa18ca1df9a4c8d
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 39, 'Bob': 61}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: df606e997f859ec852f4946f7a849d0bb7093831d072ebe18fa18ca1df9a4c8d
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 39, 'Bob': 61}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507
🔗 First Real Block Hash: df606e997f859ec852f4946f7a849d0bb7093831d072ebe18fa18ca1df9a4c8d
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 33, 'Bob': 67}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507  
🔗 First Real Block Hash: 974a00bd25c35bf9c3b11383e3c9dcb9e00a5f51655ffd9c026eff682f2b82fe
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> & C:/Users/Charlie/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/Charlie/OneDrive/Projets/Awesome Test/System/Awesome-Test-Vault/VAULT/Learnings/Blockchain/test_coin_calin-c.py"
🚀 Booting up Calin Coin educational blockchain...
✅ Calin Coin Chain Validated!
📦 Final Blockchain State: {'Alice': 33, 'Bob': 67}
🔗 Genesis Block Hash: 7c88a4312054f89a2b73b04989cd9b9e1ae437e1048f89fbb4e18a08479de507  
🔗 First Real Block Hash: 974a00bd25c35bf9c3b11383e3c9dcb9e00a5f51655ffd9c026eff682f2b82fe
PS C:\Users\Charlie\OneDrive\Projets\Awesome Test\System\Awesome-Test-Vault> 
```

**Conclusion:**  
- ✅ Same seed → consistent outputs (state and hashes)
- ✅ Different seeds → different but stable results
- ✅ Determinism confirmed

---

### 🧪 BLOCK CORRUPTION TEST

**Injected Code:**  
```python
# ⛔️ BLOCK CORRUPTION INJECTION
chain[1]['hash'] = "0000badc0ffee000deadbeefbabe0000decafbadbeadfeed0000c0de12345678"
```

**Output:**  
```python
🚀 Booting up Calin Coin educational blockchain...
Traceback (most recent call last):
  ...
ValueError: Block 1 hash mismatch
```

**Conclusion:**  
- ✅ The corrupted hash was **caught immediately**
- ✅ Exception `ValueError: Block 1 hash mismatch` was thrown as expected
- ✅ `validate_block_hash()` is functioning correctly
- 🔐 Chain integrity is **tamper-proof**
- 🛡️ Calin Coin version c is secure-by-design and corruption-aware

---

### 🧪 INVALID TRANSACTION TEST
**🎯 Goal:**  
Ensure that transactions violating the blockchain rules (e.g., imbalance or overspending) are **rejected** and **never added** to a block.

**Injected Transaction:**  
```python
txn_pool.insert(0, {'Alice': -999, 'Bob': 500})  # Invalid: total ≠ 0
```

**Debug Print Output:**  
```python
❌ INVALID: {'Alice': -999, 'Bob': 500}
```

**Conclusion:**  
✅ Transaction **was not** added to a block 
✅ System output confirmed rejection with a clear message
✅ Chain continued processing remaining valid transactions
🧱 The invalid transaction **did not crash** the system — it was gracefully skipped  
🔐 Blockchain input validation is solid and safely blocks malformed or malicious activity
✅ The `is_valid_transaction()` function is doing its job perfectly.

---

### 🧪 MANUAL TAMPER TEST

**🎯 Goal:** To verify that **modifying a transaction directly inside a block** triggers validation failure — even if the block's hash is correct.

**Manual Mutation:**  
Right before your final validation step in the script, insert:
```python
# 🧪 MANUAL TAMPER - Inject a stealthy transaction mutation
chain[1]["contents"]["txns"][0]["Alice"] = 5000
```
Insert this **after** block creation is done, and **before**:
```python
final_state = validate_chain(chain)
```


**Output:**  
```python
Traceback (most recent call last):
  ...
ValueError: Invalid transaction
```

**Conclusion:**  
✅ Tampering **inside** a block's transaction was immediately detected  
✅ Even though the hash remained untouched, the **business logic failed**  
✅ Validation re-runs all transaction rules on every block  
🔐 **Tamper-resistant** by both hash and logic — Calin Coin vC passes the audit

---
## 🔁 Next Steps

- [ ] Create automatic regression test harness (optional)
- [x] Complete version a tests
- [x] Complete version b tests
- [ ] Complete version b tests
- [ ] Add comparison summary across versions

---

*Filed under: `Calin Coin • Blockchain Security • Manual Audit`*
