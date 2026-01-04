# Day 03 — Suspicious IP Detector 🛡️

## 🔍 Project Goal  
Detect repeated failed login attempts in Linux authentication logs and flag suspicious IPs that may indicate brute-force attacks.

## 🛠️ What It Does  
- Parses `/var/log/auth.log` or a sample log file  
- Extracts IPs from failed login attempts  
- Counts attempts per IP  
- Flags IPs exceeding a threshold (default: 5)  
- Outputs a clean report of suspicious activity

## 🧠 Skills Practiced  
- Log analysis  
- Regex extraction  
- Threat detection logic  
- Python scripting  
- Linux security fundamentals

## 🚀 How to Run  
```bash
sudo python3 suspicious_ip_detector.py
