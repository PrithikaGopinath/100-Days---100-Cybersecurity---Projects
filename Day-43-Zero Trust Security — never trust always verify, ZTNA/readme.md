# 🚫 Day 43 – About Zero Trust Security

## What is Zero Trust?

**Zero Trust** is a security model built on one core principle:

> **"Never trust, always verify."**

Traditional security assumed everything inside the network was safe. Zero Trust assumes **nothing is trusted by default** — not users, not devices, not applications — even if they're already inside the network.

---

## Why Zero Trust Was Born

The old model — **"castle and moat"** — built a hard perimeter and trusted everything inside:

```
INTERNET  →  [FIREWALL]  →  Trusted Internal Network
```

This fell apart because:
- Employees work from home, cafes, airports
- Cloud apps sit outside the corporate network
- One phishing email gives attackers access to everything inside
- Insider threats are impossible to detect once inside

Zero Trust says: **the perimeter is dead. Verify everything, everywhere.**

---

## The 3 Core Principles of Zero Trust

### 1. Verify Explicitly
Always authenticate and authorise based on **all available signals**:
- Who is the user?
- What device are they on?
- Where are they connecting from?
- What time is it?
- Is this behaviour normal?

### 2. Use Least Privilege Access
- Grant minimum permissions needed
- Use Just-In-Time (JIT) access — grant access only when needed
- Limit blast radius if an account is compromised

### 3. Assume Breach
- Design as if attackers are already inside
- Segment networks to limit lateral movement
- Monitor everything, log everything
- Be ready to respond fast

---

## Zero Trust Architecture

```
User/Device
     ↓
[Identity Verification + MFA]
     ↓
[Device Health Check]
     ↓
[Policy Engine — Allow or Deny?]
     ↓
[Encrypted Access to Specific Resource]
     ↓
[Continuous Monitoring]
```

Every request is evaluated — no blanket trust.

---

## Zero Trust vs Traditional Security

| | Traditional | Zero Trust |
|-|-------------|------------|
| **Trust model** | Trust the network | Trust nothing by default |
| **Perimeter** | Hard outer wall | No perimeter — verify everywhere |
| **Lateral movement** | Easy once inside | Blocked by segmentation |
| **Remote access** | VPN | Identity + device-aware access |
| **Monitoring** | At the boundary | Continuous, everywhere |

---

## Key Technologies that Enable Zero Trust

| Technology | Role |
|-----------|------|
| **MFA** | Verify user identity strongly |
| **EDR** | Verify device health |
| **Microsegmentation** | Limit lateral movement |
| **SASE / ZTNA** | Secure remote access without VPN |
| **UEBA** | Detect anomalous behaviour |
| **SIEM** | Centralised logging and monitoring |
| **PAM** | Control privileged accounts |

---

## ZTNA — Zero Trust Network Access

**ZTNA** replaces the traditional VPN:
- Users connect to **specific applications**, not the whole network
- Access is granted per-session based on identity + device
- Examples: **Cloudflare Access**, **Zscaler Private Access**, **Google BeyondCorp**

---

## Real-World Example: Google BeyondCorp

Google migrated its entire workforce to Zero Trust after the 2009 Operation Aurora attack. Employees access internal apps from any device, anywhere — **no VPN** — because trust is verified per-request, not per-network.

---

## 🔑 Key Takeaway

Zero Trust is not a product you buy — it's a **philosophy and architecture** you adopt. In a world where attackers are already inside most networks, assuming breach and verifying everything is the only rational security model.

---

*Day 43 of 100 — 100 Days, 100 Cybersecurity Projects*

