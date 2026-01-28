# Day 21 – Open Ports Audit with `ss`

## 🔍 Objective
Identify open ports and listening services on a Linux system using the `ss` command.  
This helps detect exposed services and potential attack surfaces.

---

## 🧪 Command Used
```bash
sudo ss -tulnp
```

### Flags Explained:
- `-t` → TCP  
- `-u` → UDP  
- `-l` → Listening sockets  
- `-n` → Show port numbers  
- `-p` → Show process using the port

---

## 📋 What I Found
The system showed:

- Port 22 (SSH) open on both IPv4 and IPv6  
- Listening process: `sshd` with PID 1138  
- No unexpected services were running

This is normal for a Kali Linux system with SSH enabled.

---

## ⚠️ Why This Matters
Open ports expose services to the network.  
Auditing them helps:

- Detect unauthorized services  
- Harden the system  
- Understand what’s accessible externally

---

## 📸 Screenshots
- Terminal output of the `ss -tulnp` command

Screenshot included in this folder as proof of execution.

---

## ✅ Summary
This task helped me:

- Learn how to audit open ports  
- Understand which services are listening  
- Practice basic host-level reconnaissance  
