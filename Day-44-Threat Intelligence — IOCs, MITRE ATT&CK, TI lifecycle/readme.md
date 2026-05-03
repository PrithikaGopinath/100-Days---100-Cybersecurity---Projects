# 🕵️ Day 44 – About Threat Intelligence

## What is Threat Intelligence?

**Threat Intelligence (TI)** is evidence-based knowledge about existing or emerging threats — including context, mechanisms, indicators, and actionable advice — that helps organisations make faster, smarter security decisions.

It answers: **Who is attacking? How? Why? And what do we do about it?**

---

## Intelligence vs Information

Raw data is not intelligence. Threat intelligence is:

```
DATA        →  IP address 45.33.32.156
INFORMATION →  This IP sent 10,000 login attempts
INTELLIGENCE → This IP belongs to a known ransomware group
               targeting healthcare — block it and alert SOC
```

Intelligence is **processed, contextualised, and actionable**.

---

## Types of Threat Intelligence

### Strategic Intelligence
- High-level, for executives and boards
- "Nation-state actors are increasingly targeting energy infrastructure"
- Helps with long-term security investments

### Tactical Intelligence
- TTPs — **Tactics, Techniques, and Procedures** used by attackers
- Helps defenders understand *how* attacks work
- Mapped to frameworks like **MITRE ATT&CK**

### Operational Intelligence
- Details about specific planned or ongoing attacks
- Timing, targets, infrastructure being used
- Often from closed sources, dark web monitoring

### Technical Intelligence
- Specific indicators: IP addresses, domains, file hashes, URLs
- Used directly in security tools (firewalls, SIEMs, EDR)
- Called **IOCs — Indicators of Compromise**

---

## Indicators of Compromise (IOCs)

| Type | Example |
|------|---------|
| **IP address** | Known C2 server IP |
| **Domain** | malware-c2.ru |
| **File hash (MD5/SHA)** | Hash of a known malware binary |
| **URL** | Phishing page URL |
| **Email address** | Sender of a phishing campaign |
| **Registry key** | Persistence mechanism used by malware |
| **Mutex** | Unique string created by malware |

---

## The Threat Intelligence Lifecycle

```
1. PLANNING      →  What do we need to know? Define requirements
2. COLLECTION    →  Gather data from sources
3. PROCESSING    →  Clean, normalise, deduplicate
4. ANALYSIS      →  Make sense of it — who, what, why
5. DISSEMINATION →  Share with the right teams
6. FEEDBACK      →  Improve the next cycle
```

---

## Threat Intelligence Sources

| Source | Examples |
|--------|---------|
| **Open Source (OSINT)** | VirusTotal, Shodan, AlienVault OTX, abuse.ch |
| **Commercial feeds** | Recorded Future, Mandiant, CrowdStrike |
| **Government / CERT** | CISA, NCSC, US-CERT |
| **ISACs** | Sector-specific sharing groups (FS-ISAC, H-ISAC) |
| **Dark web** | Forums, markets, paste sites |
| **Internal** | Your own logs, incidents, honeypots |

---

## MITRE ATT&CK Framework

The gold standard for threat intelligence — a **knowledge base of real attacker behaviours** organised into:
- **Tactics** — the attacker's goal (e.g. Initial Access, Persistence, Exfiltration)
- **Techniques** — how they achieve it (e.g. Spearphishing, Scheduled Task)
- **Sub-techniques** — specific variations

Used to map attacker behaviour, identify detection gaps, and compare threat groups.

---

## Threat Intelligence Platforms (TIPs)

| Tool | Description |
|------|-------------|
| **MISP** | Open-source TI sharing platform |
| **OpenCTI** | Open-source threat intel management |
| **Recorded Future** | Commercial, AI-powered TI platform |
| **ThreatConnect** | TI operations platform |
| **VirusTotal** | File/URL/IP reputation checking |

---

## 🔑 Key Takeaway

Threat intelligence turns reactive security into **proactive defence**. Instead of waiting to be attacked, you understand who your adversaries are, what they're doing right now, and block their tools before they reach you.

---

*Day 44 of 100 — 100 Days, 100 Cybersecurity Projects*

