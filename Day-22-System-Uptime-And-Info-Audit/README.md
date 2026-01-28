# Day 23 – System Uptime & Info Audit

## 🔍 Objective
Use basic Linux commands to check system uptime, kernel version, and memory usage.  
This helps analysts quickly assess system health and environment.

---

## 🧪 Commands Used

### 1. Check system uptime
```bash
uptime
```

### 2. Check system info
```bash
uname -a
```

### 3. Check memory usage
```bash
free -h
```

---

## 📋 What I Found

### 🕒 Uptime
- System has been running for 20 minutes  
- 1 user logged in  
- Load average: 0.32, 0.18, 0.08 (low usage)

### 🧠 System Info
- OS: Kali Linux  
- Kernel: 6.12.25-arm64  
- Architecture: aarch64  
- Build date: 2025-04-30

### 💾 Memory Usage
- Total RAM: 3.8 GiB  
- Used: 770 MiB  
- Free: 1.7 GiB  
- Swap: 3.3 GiB (unused)

---

## ⚠️ Why This Matters
These commands help analysts:

- Detect system uptime for forensic timelines  
- Identify kernel version for vulnerability checks  
- Monitor memory usage for performance or compromise indicators

---

## 📸 Screenshots
- Output of `uptime`  
- Output of `uname -a`  
- Output of `free -h`  

Screenshots are included in this folder as proof of execution.

---

## ✅ Summary
This task helped me:

- Learn basic system profiling  
- Understand how uptime and memory relate to system health  
- Practice quick reconnaissance commands used in real investigations  

