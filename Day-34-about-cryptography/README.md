# 🔐 Cryptography

> **Domain:** Cryptography  
> **Difficulty:** Beginner → Advanced  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is Cryptography?

Cryptography is the science of securing information by transforming it into an unreadable format for unauthorized users. It's the backbone of nearly every security system — from HTTPS to password storage to digital signatures. Understanding cryptography helps you know *why* certain implementations are secure, and *how* attackers break weak ones.

---

## 🧱 Core Concepts

### 1. The CIA of Cryptography

Cryptography primarily addresses:

| Goal               | Description                                              | Mechanism                      |
|--------------------|----------------------------------------------------------|--------------------------------|
| **Confidentiality**| Only authorized parties can read the data               | Encryption                     |
| **Integrity**      | Data hasn't been altered in transit                      | Hashing, MACs, Digital Sigs    |
| **Authentication** | Verifying the identity of the sender                     | Digital Signatures, Certs      |
| **Non-repudiation**| Sender cannot deny sending the message                   | Digital Signatures             |

---

### 2. Types of Encryption

#### 🔹 Symmetric Encryption
Same key used to encrypt and decrypt.

```
Plaintext → [Encrypt with Key K] → Ciphertext → [Decrypt with Key K] → Plaintext
```

| Algorithm | Key Size     | Notes                                      |
|-----------|--------------|--------------------------------------------|
| AES       | 128/192/256  | Current gold standard. Fast and secure     |
| DES       | 56-bit       | Broken — do not use                        |
| 3DES      | 112/168-bit  | Deprecated — slow, mostly legacy           |
| ChaCha20  | 256-bit      | Used in TLS 1.3, great for mobile          |

**Modes of operation matter:**
- **ECB** — Insecure (same plaintext = same ciphertext)
- **CBC** — Better, but vulnerable to padding oracle attacks
- **GCM** — Authenticated encryption — recommended

---

#### 🔹 Asymmetric Encryption
Two keys: a **public key** (encrypt/verify) and a **private key** (decrypt/sign).

```
Sender encrypts with recipient's Public Key
Recipient decrypts with their own Private Key
```

| Algorithm | Use Case                                    |
|-----------|---------------------------------------------|
| RSA       | Encryption, digital signatures              |
| ECC       | Smaller keys, faster — used in TLS, Bitcoin |
| Diffie-Hellman | Key exchange (never directly encrypts) |
| DSA       | Digital signatures only                     |

---

### 3. Hashing

A one-way function that maps data to a fixed-size digest. **You cannot reverse a hash.**

```
"password123" → SHA-256 → ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f
```

| Algorithm | Output Size | Notes                                          |
|-----------|-------------|------------------------------------------------|
| MD5       | 128-bit     | Broken — collision attacks exist. Don't use    |
| SHA-1     | 160-bit     | Deprecated — collision found in 2017           |
| SHA-256   | 256-bit     | Standard. Used in TLS, Bitcoin, certificates   |
| SHA-3     | Variable    | New standard, different design from SHA-2      |
| bcrypt    | 60 chars    | Designed for passwords — slow by design        |
| Argon2    | Variable    | Winner of Password Hashing Competition         |

**Why slow hashing for passwords?**  
Attackers use GPUs to crack millions of hashes/second. Slow algorithms like bcrypt/Argon2 make brute-forcing impractical.

---

### 4. Digital Signatures

Provide authenticity and non-repudiation.

```
Sender:    Sign(message, Private Key)  → Signature
Receiver:  Verify(message, Signature, Public Key) → Valid / Invalid
```

Used in:
- Code signing (verifying software hasn't been tampered)
- SSL/TLS certificates
- Email (S/MIME, PGP)
- Blockchain transactions

---

### 5. Public Key Infrastructure (PKI)

The system that manages digital certificates and public keys.

```
Certificate Authority (CA)
    ↓ signs
Website Certificate (contains: domain, public key, validity, CA signature)
    ↓ presented to
Browser (verifies signature using CA's public key in trust store)
```

**Certificate chain:** Root CA → Intermediate CA → End-entity cert

**What happens when it breaks:**
- Self-signed certs → Browser warning
- Expired certs → Connection refused
- Compromised CA → MitM possible (DigiNotar 2011 incident)

---

### 6. TLS/SSL — Cryptography in Practice

TLS (Transport Layer Security) is how HTTPS works.

**TLS 1.3 Handshake (simplified):**
```
Client → ClientHello (supported ciphers, random nonce)
Server → ServerHello + Certificate + Public Key
Client → Verifies cert, generates session keys via ECDHE
Both   → Derive symmetric keys for the session
Both   → Communicate using AES-GCM
```

**Deprecated/Weak:**
- SSL 2.0, SSL 3.0 — completely broken
- TLS 1.0, 1.1 — deprecated (POODLE, BEAST attacks)
- TLS 1.2 — still acceptable if properly configured
- **TLS 1.3** — Current standard, use this

---

### 7. Common Cryptographic Attacks

| Attack                  | Target           | Description                                          |
|-------------------------|------------------|------------------------------------------------------|
| Brute Force             | Any encryption   | Try all possible keys                                |
| Dictionary Attack       | Password hashes  | Try common passwords against hashes                  |
| Rainbow Table           | Unsalted hashes  | Precomputed hash-to-plaintext table                  |
| Birthday Attack         | Hash functions   | Find two inputs with same hash (collision)            |
| Padding Oracle          | CBC mode         | Recover plaintext via padding error responses        |
| Replay Attack           | Protocols        | Re-use captured valid messages                       |
| Side-Channel Attack     | Implementation   | Leak keys via timing, power consumption, EM signals  |
| Meet-in-the-Middle      | Double encryption| Halve the work of brute forcing two keys             |

---

### 8. Salting

Adding a random value (salt) to passwords before hashing to prevent rainbow table attacks.

```python
import bcrypt

password = b"mypassword"
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
# Each hash is unique even for the same password
```

---

## 🛠️ Tools to Know

| Tool       | Purpose                                          |
|------------|--------------------------------------------------|
| OpenSSL    | Swiss army knife for certs, keys, TLS            |
| Hashcat    | GPU-accelerated password/hash cracking           |
| John the Ripper | Hash cracking                              |
| CyberChef  | Encode/decode/encrypt/decrypt in browser         |
| GPG        | File encryption and email signing                |
| PyCryptodome | Python cryptography library                   |

---

## 📚 Key Terms Glossary

| Term         | Meaning                                                     |
|--------------|-------------------------------------------------------------|
| Plaintext    | Original readable data                                      |
| Ciphertext   | Encrypted, unreadable data                                  |
| Key          | Secret value used in the crypto algorithm                   |
| IV / Nonce   | Random value used once to prevent repeated patterns         |
| Salt         | Random value added to passwords before hashing              |
| MAC          | Message Authentication Code — integrity + authenticity      |
| HMAC         | Hash-based MAC using a secret key                           |
| Entropy      | Measure of randomness — more entropy = harder to guess      |

---

## 💡 Classic Cipher Examples (Historical)

```
Caesar Cipher:  A → D, B → E (shift by 3)
Vigenere:       Polyalphabetic, keyword-based shift
ROT13:          Caesar with shift of 13 (self-inverse)
```

These are completely insecure today but great for learning the fundamentals of substitution and transposition.

---

## 🔗 Resources

- [CryptoHack](https://cryptohack.org/) ← Hands-on crypto challenges
- [Cryptography I — Stanford (Coursera)](https://www.coursera.org/learn/crypto)
- [The Joy of Cryptography (free textbook)](https://joyofcryptography.com/)
- [CyberChef](https://gchq.github.io/CyberChef/)
- [NIST Cryptographic Standards](https://csrc.nist.gov/)

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*
