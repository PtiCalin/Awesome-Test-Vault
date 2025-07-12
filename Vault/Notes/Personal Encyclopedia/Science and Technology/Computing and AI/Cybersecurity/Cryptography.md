---
id: cryptography
title: Cryptography
aliases: []
tags: []
author(s): PtiCalin
version: 1.3
status: draft
visibility: public
created: 2025-06-08
updated: 2025-06-08
summary: ""
element: Notes
type: "Personal Encyclopedia"
category: "Science and Technology"
section: "Computing and AI"
topic: Cybersecurity
parent: Cybersecurity
children: []
siblings: []
friends: []
---
# Cryptography

## Summary
Cryptography is the science of securing communication and data through encoding methods that make information unreadable to unauthorized parties. It is the backbone of digital privacy, authentication, and trust—used everywhere from encrypted messaging to blockchain.

## Core Concepts
| Term | Description |
| --- | --- |
| Plaintext | Original, readable message/data |
| Ciphertext | Encrypted, unreadable version of plaintext |
| Key | A string used to encrypt or decrypt data |
| Algorithm | A formula or procedure for encryption/decryption |
| Encryption | Turning plaintext into ciphertext |
| Decryption | Reversing ciphertext back into plaintext |

## Categories of Cryptography
### Symmetric Cryptography
- Same key used to encrypt and decrypt
- Fast and efficient
- Example: AES, DES

### Asymmetric Cryptography (Public Key)
- Public key to encrypt, private key to decrypt
- Enables secure communication between strangers
- Example: RSA, ECC

### Hash Functions
- One-way operations
- Used for integrity, digital fingerprints
- Example: SHA-256, MD5 (deprecated)

### Post-Quantum Cryptography
- Designed to resist quantum computer attacks
- Ongoing field of research
- Example: Lattice-based schemes, NTRU

## Historical Snapshot
- Caesar Cipher (Shift cipher) — Ancient Rome
- Enigma Machine — WWII German encryption device
- Diffie-Hellman — First public key exchange (1976)
- RSA — Groundbreaking asymmetric algorithm (1977)
- AES — Current global standard for encryption

## Common Algorithms
| Algorithm | Type | Notes |
| --- | --- | --- |
| AES | Symmetric | Fast and secure for data-at-rest |
| RSA | Asymmetric | Secure key exchange & digital signatures |
| SHA-256 | Hash | One-way hashing (Bitcoin, SSL certs) |
| ECC | Asymmetric | Efficient with smaller keys |
| Blowfish | Symmetric | Fast but older |
| PBKDF2 | Key Derivation | Used in password hashing |

## Real-World Applications
- HTTPS & SSL certificates
- Encrypted emails (PGP, S/MIME)
- End-to-End encrypted messaging (Signal, WhatsApp)
- Cryptocurrency wallets and transactions
- Secure health and legal records
- Encrypted file systems and drives

## Risks & Limitations
- Poor key management
- Algorithm backdoors or vulnerabilities
- Deprecated algorithms (e.g., MD5, SHA-1)
- Social engineering & phishing bypass crypto
- Quantum threats to RSA & ECC in the future

## Related Topics
- [[Encryption in Computing]]
- [[Authentication vs Authorization]]
- [[Public Key Infrastructure (PKI)]]
- [[Cryptanalysis]]
- [[Digital Signatures and Certificates]]

## 🔗 Related Notes

> [!info] 🧠 Relationships
> This note is part of a larger structure. Below are its connections:

```dataview
table
  parent as "Parent",
  children as "Subpages",
  friends as "Friends",
  related as "Related"
from ""
where file.link = this.file.link
```
