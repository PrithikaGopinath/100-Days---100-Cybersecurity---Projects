# 🔐 Day 42 – About Identity and Access Management (IAM)

## What is IAM?

**Identity and Access Management (IAM)** is the framework of policies, processes, and technologies that ensure the **right people** have access to the **right resources** at the **right time** — and nobody else.

In simple terms: **Who are you? What are you allowed to do?**

---

## Why IAM is Critical

- **80%+ of breaches involve compromised credentials**
- Insider threats (accidental and malicious) start with excessive access
- Compliance frameworks (GDPR, HIPAA, SOC 2) require access controls
- Remote work has massively expanded the identity attack surface
- Cloud environments have thousands of identities (users, apps, services)

---

## Core Concepts of IAM

### Authentication — "Who are you?"
Proving your identity before getting access.

| Factor | Examples |
|--------|---------|
| **Something you know** | Password, PIN, security question |
| **Something you have** | OTP app, hardware token, smart card |
| **Something you are** | Fingerprint, face scan, voice |

**MFA (Multi-Factor Authentication)** combines 2+ factors — dramatically reduces account takeover risk.

### Authorisation — "What can you do?"
Defining what an authenticated user is allowed to access.

### Accounting — "What did you do?"
Logging all access and actions for audit trails.

---

## Access Control Models

| Model | Description | Example |
|-------|-------------|---------|
| **DAC** – Discretionary | Owner decides who gets access | Linux file permissions |
| **MAC** – Mandatory | System enforces rules, users can't override | Military classifications |
| **RBAC** – Role-Based | Access based on job role | Admin, Editor, Viewer |
| **ABAC** – Attribute-Based | Access based on attributes (location, time, device) | "Only from UK, during work hours" |

---

## Principle of Least Privilege

> Give users **only the minimum access** they need to do their job — nothing more.

- Reduces blast radius if an account is compromised
- Limits insider threat damage
- Harder to implement but critical for security
- Review and revoke unused permissions regularly

---

## Key IAM Concepts

### SSO — Single Sign-On
One login grants access to multiple systems. Less password fatigue, centralised control.

### PAM — Privileged Access Management
Extra controls for admin/root accounts — most dangerous accounts in any organisation.

### Directory Services
Central store of user identities. Examples: **Active Directory** (Microsoft), **LDAP**, **Okta**.

### Federated Identity
Trust identities from external providers — "Login with Google" is federation.

---

## Common IAM Attacks

| Attack | Description |
|--------|-------------|
| **Credential stuffing** | Use leaked username/password combos at scale |
| **Password spraying** | Try one common password across many accounts |
| **Pass-the-hash** | Steal and reuse password hashes without cracking |
| **Privilege escalation** | Gain higher permissions than authorised |
| **Account takeover** | Compromise a legitimate account |

---

## IAM Tools & Platforms

- **Microsoft Entra ID** (formerly Azure AD) — enterprise identity platform
- **Okta** — cloud identity and SSO
- **CyberArk** — privileged access management
- **HashiCorp Vault** — secrets and credentials management
- **AWS IAM** — cloud resource access control

---

## 🔑 Key Takeaway

Identity is the new perimeter. Attackers rarely "hack in" — they **log in** using stolen or weak credentials. Strong IAM — especially MFA and least privilege — is your most effective defence against the majority of real-world attacks.

---

*Day 42 of 100 — 100 Days, 100 Cybersecurity Projects*

