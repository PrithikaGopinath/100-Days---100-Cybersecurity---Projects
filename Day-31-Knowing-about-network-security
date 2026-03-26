# 🌐 Network Security

> **Domain:** Network Security  
> **Difficulty:** Beginner → Advanced  
> **Part of:** 100 Days - 100 Cybersecurity Projects

---

## 📌 What is Network Security?

Network Security is the practice of protecting computer networks and the data traveling across them from unauthorized access, misuse, modification, or denial. It covers everything from how data is transmitted, how devices communicate, to how attackers intercept or disrupt those communications.

---

## 🧱 Core Concepts

### 1. The OSI Model (Why it matters in security)
Every network attack maps to a layer of the OSI model. Understanding this helps you know *where* an attack happens.

| Layer | Name         | Attack Examples                        |
|-------|--------------|----------------------------------------|
| 7     | Application  | SQL Injection, XSS, HTTP attacks       |
| 6     | Presentation | SSL stripping, encoding attacks        |
| 5     | Session      | Session hijacking                      |
| 4     | Transport    | TCP SYN flood, port scanning           |
| 3     | Network      | IP spoofing, ICMP flood                |
| 2     | Data Link    | ARP poisoning, MAC spoofing            |
| 1     | Physical     | Cable tapping, hardware tampering      |

---

### 2. Key Protocols and Their Weaknesses

| Protocol | Purpose             | Known Weakness                            |
|----------|---------------------|-------------------------------------------|
| HTTP     | Web traffic         | Plaintext — anyone can sniff              |
| HTTPS    | Encrypted web       | Weak certs / SSL stripping attacks        |
| DNS      | Domain resolution   | DNS spoofing / cache poisoning            |
| ARP      | IP-to-MAC mapping   | ARP spoofing (no authentication)          |
| FTP      | File transfer       | Credentials sent in plaintext             |
| Telnet   | Remote access       | Fully unencrypted — obsolete              |
| SSH      | Secure remote access| Brute force if misconfigured              |
| ICMP     | Ping / diagnostics  | Used in flood attacks, OS fingerprinting  |

---

### 3. Common Attack Types

#### 🔹 Passive Attacks
Attacker listens without altering traffic.
- **Sniffing / Eavesdropping** — Capturing packets on the network
- **Traffic Analysis** — Inferring info from patterns without reading content

#### 🔹 Active Attacks
Attacker modifies, injects, or disrupts traffic.
- **Man-in-the-Middle (MitM)** — Intercepting and possibly altering communication between two parties
- **ARP Poisoning** — Sending fake ARP replies to associate attacker's MAC with a legitimate IP
- **DNS Spoofing** — Returning fraudulent DNS responses to redirect users
- **DoS / DDoS** — Flooding a target to make it unavailable
- **Port Scanning** — Probing open ports to discover services (recon phase)
- **IP Spoofing** — Forging the source IP address in packets

---

### 4. Firewalls

A firewall filters incoming and outgoing traffic based on rules.

| Type                     | How it works                                          |
|--------------------------|-------------------------------------------------------|
| Packet Filtering         | Checks IP, port, protocol — no context               |
| Stateful Inspection      | Tracks connection state — smarter filtering          |
| Application Layer (WAF)  | Understands HTTP, blocks app-level attacks           |
| Next-Gen Firewall (NGFW) | DPI + IDS/IPS + App awareness                        |

---

### 5. IDS vs IPS

| Feature     | IDS (Intrusion Detection)     | IPS (Intrusion Prevention)         |
|-------------|-------------------------------|------------------------------------|
| Action      | Detects and alerts            | Detects and blocks                 |
| Placement   | Out of band (monitoring only) | Inline (in traffic path)           |
| Risk        | No false-positive blocking    | Can block legit traffic            |
| Tools       | Snort (detect mode), Zeek     | Snort (inline), Suricata           |

---

### 6. VPNs and Tunneling

- **VPN (Virtual Private Network):** Encrypts traffic between you and a server, masking your real IP and protecting data on public networks.
- **Tunneling protocols:** IPSec, OpenVPN, WireGuard, L2TP
- **Split Tunneling:** Only some traffic goes through the VPN — potential leak risk

---

### 7. Network Scanning & Recon (Attacker's Perspective)

Understanding how attackers map a network:

```bash
# Ping sweep — find live hosts
nmap -sn 192.168.1.0/24

# Port scan
nmap -sV -p 1-1000 <target>

# OS detection
nmap -O <target>

# Full aggressive scan
nmap -A <target>
```

---

### 8. Defensive Measures

- **Network Segmentation** — Divide the network into zones (DMZ, internal, guest)
- **Zero Trust Architecture** — Never trust, always verify — even internal traffic
- **802.1X / NAC** — Authenticate devices before granting network access
- **VLAN** — Logically separate network traffic
- **SSL/TLS** — Encrypt data in transit
- **Rate Limiting** — Prevent brute force and DoS
- **Honeypots** — Decoy systems to detect and study attackers

---

## 🛠️ Tools to Know

| Tool       | Purpose                             |
|------------|-------------------------------------|
| Wireshark  | Packet capture and analysis         |
| Nmap       | Port scanning and host discovery    |
| Netcat     | Networking Swiss Army knife         |
| tcpdump    | CLI packet capture                  |
| Scapy      | Python packet crafting library      |
| Metasploit | Exploitation framework              |
| Snort      | IDS/IPS                             |
| Zeek       | Network traffic analysis            |

---

## 📚 Key Terms Glossary

| Term            | Meaning                                                       |
|-----------------|---------------------------------------------------------------|
| Subnet          | A subdivided segment of a larger network                      |
| CIDR            | Notation for IP ranges (e.g., 192.168.0.0/24)                 |
| NAT             | Translates private IPs to public IPs                          |
| Bandwidth       | Maximum data transfer rate of a connection                    |
| Latency         | Time for a packet to travel from source to destination        |
| Packet          | Unit of data transmitted over a network                       |
| Payload         | The actual data content inside a packet                       |
| Encapsulation   | Wrapping data with protocol headers at each OSI layer         |

---

## 💡 Real-World Scenarios

1. **Coffee Shop Attack** — Attacker on the same WiFi runs ARP poisoning to intercept unencrypted traffic from other users.
2. **DNS Hijacking** — ISP or attacker poisons DNS cache, redirecting users from legitimate sites to fake ones.
3. **SYN Flood** — Attacker sends thousands of TCP SYN packets without completing handshakes, exhausting server resources.

---

## 🔗 Resources

- [Cisco Networking Basics](https://www.netacad.com/)
- [Nmap Official Docs](https://nmap.org/book/)
- [Wireshark User Guide](https://www.wireshark.org/docs/)
- [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)
- [TryHackMe — Pre-Security Path](https://tryhackme.com/path/outline/presecurity)

---

*Part of the 100 Days - 100 Cybersecurity Projects challenge by [@PrithikaGopinath](https://github.com/PrithikaGopinath)*

