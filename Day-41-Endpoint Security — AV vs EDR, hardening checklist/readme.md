# 💻 Day 41 – About Endpoint Security

## What is Endpoint Security?

**Endpoint security** is the practice of securing end-user devices — laptops, desktops, mobile phones, tablets, and servers — that connect to a network.

Every device that touches your network is a potential door for attackers. Endpoint security is about **locking every door**.

---

## Why Endpoints are the #1 Attack Target

- Employees click phishing links on their laptops
- USB drives introduce malware directly
- Personal devices on corporate networks bypass controls
- Remote workers operate outside the corporate perimeter
- **Over 70% of breaches originate at the endpoint**

---

## Key Components of Endpoint Security

### 1. Antivirus / Anti-malware
- Detects and removes known malicious software
- Signature-based (known threats) + heuristic (unknown threats)

### 2. EDR — Endpoint Detection & Response
- Monitors endpoint behaviour in real time
- Detects suspicious activity even without known signatures
- Allows security teams to investigate and respond remotely
- Examples: CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne

### 3. DLP — Data Loss Prevention
- Prevents sensitive data from leaving the device
- Blocks uploads to personal cloud storage, USB transfers, etc.

### 4. Application Control / Whitelisting
- Only allows approved applications to run
- Blocks unknown or unauthorised executables

### 5. Full Disk Encryption
- Encrypts the entire drive so stolen devices reveal nothing
- Examples: BitLocker (Windows), FileVault (Mac)

### 6. Patch Management
- Ensures OS and applications are always up to date
- Unpatched software is the most common attack vector

---

## EDR vs Traditional Antivirus

| | Antivirus | EDR |
|-|-----------|-----|
| **Detection** | Signature-based | Behaviour-based |
| **Response** | Quarantine file | Isolate device, kill process, investigate |
| **Visibility** | Limited | Full process tree, network connections |
| **Threat types** | Known malware | Known + unknown + fileless attacks |

---

## Common Endpoint Threats

| Threat | Description |
|--------|-------------|
| **Ransomware** | Encrypts files and demands payment |
| **Keyloggers** | Record keystrokes to steal credentials |
| **Trojans** | Disguise as legitimate software |
| **Fileless malware** | Runs in memory — leaves no files |
| **Spyware** | Silently monitors and exfiltrates data |
| **Rootkits** | Hides deep in the OS to avoid detection |

---

## Endpoint Hardening Checklist

- [ ] Enable full disk encryption
- [ ] Enable firewall on all devices
- [ ] Disable USB ports where not needed
- [ ] Remove unused software and services
- [ ] Enforce strong password policies
- [ ] Enable auto-lock after inactivity
- [ ] Deploy EDR solution
- [ ] Keep OS and software patched
- [ ] Enable audit logging

---

## 🔑 Key Takeaway

The perimeter is dead — employees work from everywhere. **Every endpoint is the new perimeter.** Securing endpoints with a layered approach (AV + EDR + encryption + patching) is non-negotiable in modern cybersecurity.

---

*Day 41 of 100 — 100 Days, 100 Cybersecurity Projects*

