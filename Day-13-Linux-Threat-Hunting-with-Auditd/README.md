# 🔍 Day 13 — Linux Threat Hunting with Auditd

## 📌 Overview
Today’s focus was on using **auditd**, a powerful Linux auditing framework, to detect suspicious system activity.  
I created audit rules to monitor execution of sensitive binaries such as `chmod`, `chown`, and `sudo`, and then simulated activity to generate logs for analysis.

This exercise builds real-world Blue Team skills:
- Detecting unauthorized permission changes
- Monitoring privileged command execution
- Understanding Linux syscall-level logging
- Performing forensic analysis using ausearch & aureport

---

## 🛠️ Tools Used
- Kali Linux
- auditd
- ausearch
- aureport

---

## 📁 Files in This Folder
- `rules.txt` → Audit rules used today  
- `analysis.md` → Explanation of logs and findings  
- `commands.txt` → Commands executed during the exercise  
- `screenshots/` → Terminal screenshots (optional)

---

## 🧪 What I Did Today
1. Installed and enabled auditd  
2. Added rules to monitor:
   - `/etc/passwd` modifications  
   - Execution of `chmod`, `chown`, and `sudo`  
3. Reloaded audit rules  
4. Simulated suspicious activity  
5. Analyzed logs using `ausearch` and `aureport`

---

## 🧠 Key Learning
Auditd provides deep visibility into system-level events.  
This is essential for:
- Threat hunting  
- Incident response  
- Detecting privilege escalation  
- Monitoring insider threats  

---

## ✅ Status
✔️ Completed  
