# 🐧 Linux Commands Every Cybersecurity Student Should Know (46–60)

These commands strengthen  skills in networking, system auditing, permissions, and troubleshooting.

---

## 🔹 `uptime` — System load & uptime  
Shows how long the system has been running and current load.  
**Example:**  
uptime

---

## 🔹 `dmesg` — Kernel messages  
Useful for hardware, driver, and boot troubleshooting.  
**Example:**  
dmesg | tail

---

## 🔹 `journalctl` — Systemd logs  
View detailed logs for services and the system.  
**Example:**  
sudo journalctl -u ssh

---

## 🔹 `htop` — Interactive process viewer  
Improved version of `top` with colors and navigation.  
**Example:**  
htop

---

## 🔹 `passwd` — Change user password  
Used for account security and resets.  
**Example:**  
passwd username

---

## 🔹 `adduser` — Create new user  
Common in system administration and lab setups.  
**Example:**  
sudo adduser analyst

---

## 🔹 `deluser` — Remove user  
Deletes user accounts safely.  
**Example:**  
sudo deluser analyst

---

## 🔹 `groupadd` — Create a new group  
Useful for permission management.  
**Example:**  
sudo groupadd security

---

## 🔹 `crash` — Analyze kernel crash dumps  
Used in advanced forensics.  
**Example:**  
crash /var/crash/vmcore

---

## 🔹 `lsof` — List open files  
Great for spotting suspicious processes or ports.  
**Example:**  
sudo lsof -i :22

---

## 🔹 `chmod +x` — Make a script executable  
Essential for running tools and scripts.  
**Example:**  
chmod +x script.sh

---

## 🔹 `md5sum` — Generate MD5 hash  
Used for integrity checks and malware analysis.  
**Example:**  
md5sum file.bin

---

## 🔹 `sha256sum` — Generate SHA‑256 hash  
More secure hashing for verification.  
**Example:**  
sha256sum image.iso

---

## 🔹 `traceroute` — Trace network path  
Shows the route packets take across the network.  
**Example:**  
traceroute google.com

---

## 🔹 `dig` — DNS lookup  
Great for DNS enumeration and troubleshooting.  
**Example:**  
dig microsoft.com
