---
# 📄 Identity & Classification
id: encryption-basics-cheatsheet
title: "Encryption Basics Cheatsheet"
aliases: ["Encryption Cheatsheet"]
type: note
category: cybersecurity
section: science-and-technology
role: documentation
folder: cybersecurity
tags: [encryption, cheatsheet]
version: 1.0

# 📊 Status & Lifecycle
status: draft
visibility: public
created: <% today %>
updated: <% today %>

# 📚 Context & Description
summary: "Quick reference for common encryption concepts and commands."

# 🧱 Relationships
parent: "Cybersecurity"
children: []
friends: []
related: []
---

> [!nav] 🧱 Vault Navigation
<!-- Relative Nav Bars -->
<!-- Notes -->
<!-- Learnings -->
<!-- Libraries -->
<!-- System -->

## 🔐 Encryption Basics Cheatsheet

## 🔤 Quick Summary
Encryption transforms readable data (plaintext) into unreadable data (ciphertext) using algorithms and keys, protecting it from unauthorized access.

---

## 🧠 Core Concepts
- **Symmetric Encryption**: same key for encryption/decryption (e.g. AES)
- **Asymmetric Encryption**: public + private key pair (e.g. RSA)
- **Hashing**: one-way transformation for integrity (e.g. SHA-256)

---

## 📐 Examples

**Symmetric:**
```bash
openssl enc -aes-256-cbc -in file.txt -out file.enc
```

**Asymmetric (RSA Key Pair):**
```bash
openssl genrsa -out private.pem 2048
openssl rsa -in private.pem -pubout -out public.pem
```

### 🧰 Tools
- OpenSSL
- GPG (GNU Privacy Guard)
- Keybase

### 💡 Gotchas
- Hashing ≠ encryption
- Never hard-code keys in your source code
- Asymmetric is more secure, but slower

### 🔗 Related
- [[Public Key Infrastructure]]
- [[SSL/TLS]]
- [[Digital Signatures]]

---

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
