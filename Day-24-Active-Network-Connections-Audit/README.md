# Day 24 – Active Network Connections Audit

## 🔍 Objective
Identify who is currently logged into the system and analyze all active network connections.  
This helps detect unauthorized access, suspicious remote connections, and unusual network activity.

---

## 🧪 Commands Used

### 1. Check logged‑in users
```bash
who
```

### 2. View all active network connections
```bash
ss -tunap
```

**Flags explained:**
- `t` → TCP  
- `u` → UDP  
- `n` → numeric ports  
- `a` → all connections  
- `p` → show process using the connection  

---

## 📋 What I Found

### 👤 Logged‑in Users
The `who` command showed the currently active user session(s).  
No unexpected or unauthorized users were present.

### 🌐 Active Network Connections
The `ss -tunap` output displayed:

- Listening services  
- Established connections  
- Local and remote IP addresses  
- Associated processes  

No suspicious remote IPs or unknown processes were detected.

---

## ⚠️ Why This Matters
Monitoring active sessions and network connections helps analysts:

- Detect unauthorized access  
- Identify malware communicating externally  
- Spot unusual ports or processes  
- Understand system activity in real time  

This is a core skill in incident response and threat hunting.

---

## 📸 Screenshots
- Output of `who`  
- Output of `ss -tunap`  

Screenshots are included in this folder as proof of execution.

---

## ✅ Summary
This task helped me:

- Learn how to check active user sessions  
- Understand how to inspect real‑time network connections  
- Practice basic threat‑hunting techniques  
