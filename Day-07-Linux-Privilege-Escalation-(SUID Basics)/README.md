# Day 07 — Linux Privilege Escalation (SUID Basics)

## 🔹 Objective
Demonstrate how misconfigured SUID binaries can lead to privilege escalation on Linux systems.

---

## 🔹 Lab Setup & Commands
```bash
# Create lab environment
mkdir lab
cd lab

# Create file and directory
touch testfile07
mkdir testdir

# Apply permissions
chmod 755 testfile07
chmod 700 testdir

# Create SUID-enabled binary
sudo cp /bin/bash ./bash_suid
sudo chmod 4755 bash_suid

# Verify permissions
ls -l

# Privilege escalation test
./bash_suid -p
```

---

## 🔹 Findings
- `bash_suid` was successfully created with the SUID bit (`-rwsr-xr-x`).
- Running `./bash_suid -p` launched a **root shell**, confirming privilege escalation.
- This demonstrates how attackers exploit insecure SUID binaries to gain elevated access.

---

## 🔹 Screenshots
- `ls -l` showing SUID bit  
- Root shell from `./bash_suid -p`  
- Lab folder structure  

---

## 🔹 Skills Gained
- Linux permission auditing  
- Understanding SUID/SGID behaviour  
- Identifying privilege escalation vectors  
- Secure configuration awareness  
