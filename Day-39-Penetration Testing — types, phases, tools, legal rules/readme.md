# 🛡️ Day 39 – About Penetration Testing

## What is Penetration Testing?

Penetration Testing (or **Pen Testing**) is an authorised, simulated cyberattack on a system, network, or application — performed to find security weaknesses before real attackers do.

Think of it as **hiring a thief to test your locks**.

---

## Why is it Important?

- Finds real vulnerabilities before attackers exploit them
- Validates that security controls actually work
- Required by compliance standards (PCI-DSS, ISO 27001, HIPAA)
- Helps prioritise what to fix first
- Builds confidence in your defences

---

## Types of Penetration Testing

| Type | Description |
|------|-------------|
| **Black Box** | Tester has zero knowledge of the system (simulates an outsider) |
| **White Box** | Tester has full knowledge — source code, architecture, credentials |
| **Grey Box** | Partial knowledge — simulates a malicious insider or contractor |
| **External** | Attacks from outside the network (internet-facing systems) |
| **Internal** | Attacks from inside the network (simulates insider threat) |
| **Social Engineering** | Targets humans — phishing, vishing, pretexting |
| **Physical** | Attempts to gain physical access to premises or hardware |

---

## The 5 Phases of Penetration Testing

```
1. RECONNAISSANCE  →  Gather information about the target
2. SCANNING        →  Discover open ports, services, vulnerabilities
3. EXPLOITATION    →  Attempt to breach the system
4. POST-EXPLOITATION → Maintain access, escalate privileges, pivot
5. REPORTING       →  Document findings with risk ratings & fixes
```

---

## Common Pen Testing Tools

| Tool | Purpose |
|------|---------|
| **Nmap** | Network scanning & port discovery |
| **Metasploit** | Exploitation framework |
| **Burp Suite** | Web application testing |
| **Wireshark** | Packet capture & analysis |
| **Hydra** | Brute-force login attacks |
| **SQLmap** | Automated SQL injection |
| **Nikto** | Web server vulnerability scanner |
| **John the Ripper** | Password cracking |

---

## Pen Testing vs Vulnerability Assessment

| | Pen Testing | Vulnerability Assessment |
|-|------------|--------------------------|
| **Goal** | Actively exploit weaknesses | Identify and list weaknesses |
| **Depth** | Deep — proves impact | Broad — covers more surface |
| **Risk** | Higher (active exploitation) | Lower (mostly passive) |
| **Output** | Proof of compromise | List of vulnerabilities |

---

## Legal & Ethical Rules

> ⚠️ **Never** perform a pen test without written authorisation.

- Always have a **signed scope of work** and **rules of engagement**
- Define what is **in scope** and **out of scope** clearly
- Have an **emergency contact** in case something breaks
- Follow responsible disclosure for any findings

---

## Key Certifications in Pen Testing

- **CEH** – Certified Ethical Hacker
- **OSCP** – Offensive Security Certified Professional (most respected)
- **PNPT** – Practical Network Penetration Tester
- **eJPT** – eLearnSecurity Junior Penetration Tester (great starter)

---

## 🔑 Key Takeaway

Penetration testing is not about breaking things — it's about **proving what's broken before the bad guys do**. It's one of the most in-demand and well-paid roles in cybersecurity.

---

*Day 39 of 100 — 100 Days, 100 Cybersecurity Projects*

