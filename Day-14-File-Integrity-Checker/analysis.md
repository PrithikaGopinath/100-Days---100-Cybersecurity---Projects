# 🔎 Day 14 Analysis — File Integrity Checker

## 1. Purpose
File integrity monitoring is used to detect:
- Malware modifying system files
- Unauthorized changes
- Insider attacks
- Tampering during incident response

This script demonstrates the core concept using SHA‑256 hashing.

---

## 2. What I Did
1. Created a test file  
2. Generated a baseline hash  
3. Modified the file  
4. Ran the script again  
5. The script detected the change successfully  

---

## 3. Why This Matters
This is the same technique used by:
- Tripwire
- OSSEC
- Wazuh
- SIEM tools
- Forensic investigators

It’s a fundamental skill for Blue Team and SOC analysts.

---

## 4. Conclusion
Day‑14 helped me understand:
- How hashing works  
- How integrity monitoring detects tampering  
- How to automate detection using Python  

This is a practical and essential cybersecurity skill.
