# Day 24 – Recently Modified Files Audit

## 🔍 Objective
Identify files that were modified recently on the system.  
This helps detect unexpected changes, potential tampering, or suspicious activity.

---

## 🧪 Commands Used

### 1. Find files modified in the last 24 hours
```bash
sudo find / -type f -mtime -1 -ls 2>/dev/null
```

### 2. (Optional) Check for modified files in /etc
```bash
sudo find /etc -type f -mtime -1 -ls 2>/dev/null
```

---

## 📋 What I Found
The command listed files that were modified within the last day.  
These typically include:

- System logs  
- Cache files  
- Temporary files  
- Application updates  
- User‑generated files  

No suspicious or unexpected modifications were observed.

---

## ⚠️ Why This Matters
Attackers often modify or drop files during:

- Privilege escalation  
- Persistence setup  
- Log tampering  
- Malware installation  

Monitoring recently modified files helps analysts:

- Detect unauthorized changes  
- Build forensic timelines  
- Identify compromised components  

---

## ✅ Summary
This task helped me:

- Learn how to track recent file changes  
- Understand how attackers hide or modify files  
- Practice basic forensic investigation techniques  
