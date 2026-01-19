# 🐧 Linux Commands Every Cybersecurity Student Should Know (61–75)

These commands expand capabilities in networking, system auditing, compression, permissions, and troubleshooting.

---

## 🔹 `nc` — Netcat  
Swiss‑army knife for networking, scanning, and data transfer.  
**Example:**  
nc -lvnp 4444

---

## 🔹  `tcpdump` — Packet capture  
Captures and analyzes network traffic from the terminal.  
**Example:**  
sudo tcpdump -i eth0

---

## 🔹 `arp` — View ARP table  
Useful for detecting spoofing or network anomalies.  
**Example:**  
arp -a

---

## 🔹 `route` — View routing table  
Shows how traffic is routed through the system.  
**Example:**  
route -n

---

## 🔹 `hostnamectl` — Manage hostname settings  
Displays or changes system hostname and metadata.  
**Example:**  
hostnamectl status

---

## 🔹 `stat` — Detailed file information  
Shows permissions, size, timestamps, and inode data.  
**Example:**  
stat /etc/passwd

---

## 🔹`file` — Identify file type  
Useful in forensics and malware analysis.  
**Example:**  
file suspicious.bin

---

## 🔹 `strings` — Extract readable text  
Pulls ASCII strings from binaries or memory dumps.  
**Example:**  
strings malware.exe

---

## 🔹 `cut` — Extract columns from text  
Great for log parsing and automation.  
**Example:**  
cut -d':' -f1 /etc/passwd

---

## 🔹 `sort` — Sort lines of text  
Used in data cleanup and analysis.  
**Example:**  
sort users.txt

---

## 🔹 `uniq` — Remove duplicate lines  
Often paired with `sort` for clean output.  
**Example:**  
sort users.txt | uniq

---

## 🔹 `awk` — Pattern scanning & processing  
Powerful for log analysis and automation.  
**Example:**  
awk '{print $1}' access.log

---

## 🔹 `sed` — Stream editor  
Used for search, replace, and text manipulation.  
**Example:**  
sed 's/root/admin/g' /etc/passwd

---

## 🔹 `tee` — Output to file + screen  
Useful for logging command output.  
**Example:**  
ls -la | tee output.txt

---

## 🔹 `uptime -p` — Pretty uptime  
Shows system uptime in a human‑friendly format.  
**Example:**  
uptime -p
