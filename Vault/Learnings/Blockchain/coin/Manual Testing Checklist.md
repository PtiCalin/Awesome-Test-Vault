# Manual Testing Checklist


## Blockchain 

- [ ] **RUN TEST:** Does it run without syntax or logic errors?
- [ ] **DETERMINATION TEST:** Is the output deterministic? (Alice and Bob totals always same)
- [ ] **BLOCK CORRUPTION TEST:** Try corrupting a block hash — does `checkChain()` catch it?
- [ ] **INVALID TRANSACTION TEST:** Try adding an invalid transaction manually — is it rejected?
- [ ] **MANUAL TAMPER TEST:** Manual Tamper Test Edit a block manually in any file and re-run it:
```python
	chain[1]['contents']['txns'][0]['Alice'] = 5000	
```



