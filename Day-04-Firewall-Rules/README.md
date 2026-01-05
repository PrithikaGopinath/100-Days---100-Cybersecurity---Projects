# Day 04 – Firewall Rule Setup (UFW on Kali Linux)

## 🔐 Objective
Configure and test a secure firewall rule set using UFW on Kali Linux to control incoming and outgoing traffic.

## 🧩 Skills Demonstrated
- Linux system hardening on Kali
- UFW firewall configuration
- Network traffic control (incoming vs outgoing)
- Log monitoring and basic verification

## ⚙️ Commands Used
```bash
sudo apt update
sudo apt install ufw
sudo ufw allow 22/tcp
sudo ufw enable
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw delete allow 22/tcp
sudo ufw allow from 192.168.64.2 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw status numbered
sudo ufw logging on
sudo tail -n 50 /var/log/ufw.log
sudo nmap localhost
