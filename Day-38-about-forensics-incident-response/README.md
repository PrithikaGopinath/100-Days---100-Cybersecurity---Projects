# 🔍 Forensics & Incident Response

> **Domain:** Digital Forensics & Incident Response (DFIR)  
> **Difficulty:** Intermediate → Advanced  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is DFIR?

**Digital Forensics** is the process of collecting, preserving, and analyzing digital evidence to understand what happened during a security incident.

**Incident Response** is the structured approach to handling and managing the aftermath of a security breach or attack to limit damage and recover quickly.

Together, DFIR answers: *What happened? How? Who did it? What did they take or damage?*

---

## 🧱 Core Concepts

### 1. The Incident Response Lifecycle (NIST)

```
  ┌──────────┐    ┌──────────────┐    ┌──────────────────┐    ┌──────────────┐
  │Preparation│───▶│ Detection &  │───▶│  Containment,    │───▶│Post-Incident │
  │          │    │  Analysis    │    │  Eradication &   │    │   Activity   │
  └──────────┘    └──────────────┘    │    Recovery      │    └──────────────┘
                                      └──────────────────┘
```

#### Phase 1: Preparation
- Build an incident response plan
- Set up logging, SIEM, and monitoring
- Train the team
- Create playbooks for common incident types

#### Phase 2: Detection & Analysis
- Identify indicators of compromise (IOCs)
- Determine scope and severity
- Collect and preserve evidence
- Build a timeline of events

#### Phase 3: Containment, Eradication & Recovery
- Isolate affected systems (network block, shutdown)
- Remove malware and backdoors
- Patch vulnerabilities
- Restore from clean backups

#### Phase 4: Post-Incident Activity
- Write an incident report
- Lessons learned / root cause analysis
- Update detection rules and playbooks

---

### 2. Evidence Collection Principles

**The Golden Rule: Preserve before you analyze.**

#### Order of Volatility
Collect the most volatile evidence first — it disappears when the system restarts.

```
1. CPU registers, cache            ← Most volatile
2. RAM / Running processes
3. Network connections
4. Running processes + open files
5. Disk contents
6. Remote logging / monitoring
7. Physical configuration          ← Least volatile
```

#### Chain of Custody
Document every person who touches evidence:
- Who collected it, when, where
- How it was stored and transferred
- Ensure evidence hasn't been tampered with
- Critical for legal proceedings

#### Write Blocking
Use hardware/software write blockers to prevent modifying evidence when making disk images.

---

### 3. Memory Forensics

RAM contains processes, network connections, encryption keys, passwords, and more — even after malware tries to hide.

**Key artifacts in memory:**
- Running processes (including hidden ones)
- Open network connections
- Loaded DLLs
- Command history
- Browser artifacts
- Encryption keys in use

**Volatility commands:**
```bash
# List running processes
vol -f memory.dmp windows.pslist

# Show process tree (detects injections)
vol -f memory.dmp windows.pstree

# Network connections
vol -f memory.dmp windows.netstat

# Detect injected code in processes
vol -f memory.dmp windows.malfind

# Dump a suspicious process
vol -f memory.dmp windows.dumpfiles --pid 1234
```

---

### 4. Disk Forensics

Analyzing file systems, deleted files, and artifacts on storage media.

**Creating a forensic image (never analyze original):**
```bash
# Create bit-for-bit copy
dd if=/dev/sda of=/evidence/disk.img bs=4M status=progress

# With verification hash
dcfldd if=/dev/sda of=/evidence/disk.img hash=sha256 hashlog=/evidence/hash.txt
```

**Key locations on Windows:**

| Artifact                  | Location                                          |
|---------------------------|---------------------------------------------------|
| User files                | `C:\Users\<username>\`                            |
| Recycle Bin               | `C:\$Recycle.Bin\`                                |
| Browser history           | AppData\Roaming\Browser folders                   |
| Event logs                | `C:\Windows\System32\winevt\Logs\`                |
| Prefetch files            | `C:\Windows\Prefetch\` (programs recently run)    |
| Registry hives            | `C:\Windows\System32\config\`                     |
| Amcache                   | Evidence of program execution                     |
| Shellbags                 | Evidence of folder browsing                       |
| LNK files                 | Recently opened files                             |
| $MFT                      | Master File Table — records all NTFS file metadata|

---

### 5. Log Analysis

Logs are the primary source of evidence in most investigations.

**Key Windows Event Log IDs:**

| Event ID | Description                                  |
|----------|----------------------------------------------|
| 4624     | Successful logon                             |
| 4625     | Failed logon                                 |
| 4634     | Logoff                                       |
| 4648     | Logon with explicit credentials (runas)      |
| 4688     | Process created                              |
| 4698     | Scheduled task created                       |
| 4720     | User account created                         |
| 7045     | New service installed                        |
| 1102     | Audit log cleared (suspicious!)              |

**Linux log locations:**
```
/var/log/auth.log     → Authentication events
/var/log/syslog       → General system log
/var/log/apache2/     → Web server logs
/var/log/kern.log     → Kernel messages
~/.bash_history       → Command history (often cleared by attackers)
```

---

### 6. Network Forensics

Analyzing captured network traffic to reconstruct events.

**What to look for in PCAP files:**
- Unusual connections to external IPs
- DNS queries to suspicious domains
- Large data transfers (exfiltration)
- C2 beaconing patterns (regular intervals)
- Plaintext credentials

```bash
# Read a pcap
tcpdump -r capture.pcap

# Filter by IP
tshark -r capture.pcap -Y "ip.addr == 192.168.1.5"

# Extract HTTP objects (files)
tshark -r capture.pcap --export-objects http,/output/folder
```

---

### 7. Timeline Analysis

Building a unified timeline correlates events across systems.

```
2024-01-15 09:14:22  - Phishing email received (Exchange logs)
2024-01-15 09:18:47  - User clicked attachment (endpoint logs)
2024-01-15 09:18:51  - Malware execution started (Sysmon Event 1)
2024-01-15 09:19:03  - PowerShell launched (Event ID 4688)
2024-01-15 09:19:15  - Outbound connection to 185.x.x.x (firewall logs)
2024-01-15 09:22:00  - Lateral movement via SMB to DC (Event 4624 Type 3)
```

**Tool:** Plaso / log2timeline for automated timeline creation

---

### 8. Common Attack Artifacts to Hunt

| Attack Type         | What to Look For                                         |
|---------------------|----------------------------------------------------------|
| Phishing            | Email headers, attachment hashes, clicked URLs           |
| Ransomware          | Mass file renames, new extensions, ransom note           |
| Credential Theft    | LSASS memory access, Event 4648, unusual logons          |
| Lateral Movement    | Event 4624 Type 3, PsExec artifacts, WMI activity        |
| Exfiltration        | Large DNS queries, unusual outbound traffic volumes      |
| Persistence         | New scheduled tasks, services, Run keys, startup items   |

---

## 🛠️ Tools to Know

| Tool              | Purpose                                          |
|-------------------|--------------------------------------------------|
| Volatility 3      | Memory forensics framework                       |
| Autopsy           | GUI-based disk forensics                         |
| FTK Imager        | Disk imaging and evidence collection             |
| Wireshark/tshark  | Network packet analysis                          |
| Plaso/log2timeline| Timeline creation from multiple sources          |
| Velociraptor      | Endpoint forensics and live response             |
| KAPE              | Fast artifact collection from Windows endpoints  |
| Chainsaw          | Hunt through Windows event logs                  |
| ELK Stack         | Log aggregation and analysis (SIEM)              |
| Splunk            | Enterprise SIEM                                  |

---

## 📚 Key Terms Glossary

| Term           | Meaning                                                         |
|----------------|-----------------------------------------------------------------|
| IOC            | Indicator of Compromise — hash, IP, domain, file name          |
| TTPs           | Tactics, Techniques, Procedures — attacker's methods            |
| SIEM           | Security Information and Event Management                       |
| PCAP           | Packet capture file                                             |
| Artifact       | Any digital trace left by a user or program                     |
| Triage         | Quick assessment to prioritize what to investigate              |
| Forensic Image | Exact bit-for-bit copy of a storage medium                      |
| Pivot          | Moving from one finding to related evidence                     |

---

## 🔗 Resources

- [SANS DFIR Resources](https://www.sans.org/dfir/)
- [Volatility Foundation](https://volatilityfoundation.org/)
- [BlueTeamLabs Online](https://blueteamlabs.online/) ← Hands-on IR challenges
- [CyberDefenders](https://cyberdefenders.org/) ← Blue team CTFs
- [MITRE ATT&CK Framework](https://attack.mitre.org/) ← TTPs reference
- [Eric Zimmerman Tools](https://ericzimmerman.github.io/) ← Free forensics tools

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*
