# 🖥️ Day 45 – About Security Operations Center (SOC)

## What is a SOC?

A **Security Operations Center (SOC)** is a centralised team — and the facility or platform they use — responsible for **monitoring, detecting, analysing, and responding** to cybersecurity threats 24 hours a day, 7 days a week.

Think of it as the **nerve centre of an organisation's cyber defence**.

---

## What Does a SOC Do?

- Monitors security alerts across the entire organisation in real time
- Investigates suspicious events and determines if they're real threats
- Responds to confirmed incidents to contain and remediate damage
- Hunts for threats that automated tools may have missed
- Manages and improves security tools and processes
- Produces reports for management and compliance

---

## SOC Team Roles

### Tier 1 — Alert Analyst
- First responder to alerts
- Triages incoming alerts — real threat or false positive?
- Escalates confirmed threats to Tier 2
- Monitors dashboards 24/7

### Tier 2 — Incident Responder
- Deeper investigation of escalated alerts
- Determines scope and impact of incidents
- Coordinates containment and remediation
- Performs malware analysis

### Tier 3 — Threat Hunter / Senior Analyst
- Proactively hunts for threats that evaded detection
- Reverse engineers malware
- Develops new detection rules and playbooks
- Most experienced team members

### SOC Manager
- Oversees operations, staffing, and performance
- Reports to CISO
- Manages vendor relationships and tooling budget

---

## Core SOC Technologies

| Tool | Purpose |
|------|---------|
| **SIEM** | Aggregates and correlates logs from all sources |
| **SOAR** | Automates response playbooks |
| **EDR** | Endpoint monitoring and response |
| **Threat Intelligence Platform** | Enriches alerts with IOC context |
| **Vulnerability Scanner** | Identifies exposed weaknesses |
| **Network Traffic Analysis** | Detects anomalous traffic patterns |
| **Ticketing System** | Tracks incidents end-to-end |

---

## SIEM — The Heart of the SOC

**Security Information and Event Management** collects logs from:
- Firewalls
- Servers and endpoints
- Cloud environments
- Applications
- Network devices

It correlates events across all sources to spot attacks that span multiple systems.

Popular SIEMs: **Splunk**, **Microsoft Sentinel**, **IBM QRadar**, **Elastic SIEM**

---

## The SOC Incident Response Flow

```
ALERT TRIGGERED
      ↓
TIER 1 TRIAGE — Real or false positive?
      ↓
ESCALATE TO TIER 2 — How bad is it?
      ↓
CONTAINMENT — Stop the bleeding
      ↓
INVESTIGATION — What happened? How?
      ↓
REMEDIATION — Fix the root cause
      ↓
POST-INCIDENT REVIEW — Learn and improve
```

---

## Types of SOC Models

| Model | Description |
|-------|-------------|
| **In-house SOC** | Fully internal team — expensive but full control |
| **Virtual SOC** | Remote analysts, no physical facility |
| **Co-managed SOC** | Internal team + external MSSP support |
| **MSSP** | Fully outsourced to a Managed Security Service Provider |

---

## SOC Metrics That Matter

- **MTTD** — Mean Time to Detect (how fast do we spot attacks?)
- **MTTR** — Mean Time to Respond (how fast do we contain them?)
- **False positive rate** — too many = alert fatigue
- **Dwell time** — how long attackers lurk undetected

---

## SOC Analyst — Career Path

```
Tier 1 Analyst  →  Tier 2 Analyst  →  Tier 3 / Threat Hunter
                                              ↓
                                    Incident Response Lead
                                              ↓
                                         SOC Manager
                                              ↓
                                            CISO
```

Helpful certs: **CompTIA Security+**, **BTL1**, **SC-200**, **Splunk Core Certified**, **CySA+**

---

## 🔑 Key Takeaway

A SOC is not just a room full of monitors — it's a **living defence system** that combines skilled people, smart processes, and powerful technology. Without a SOC (or SOC-equivalent), most organisations are flying blind during an attack.

---

*Day 45 of 100 — 100 Days, 100 Cybersecurity Projects*

