# Findings – Day 09

## 1. Tampering Evidence
- `/var/log/auth.log` was created and deleted successfully.
- No audit logs were present (`/var/log/audit/audit.log` missing).
- No system logs were present (`/var/log/syslog` missing).
- No fragments were recoverable using `strings` or `grep`.

## 2. Recovery Attempts
### Commands Used
- `strings /var/log/syslog | grep -i 'auth'`
- `grep -i 'sshd' /var/log/syslog`
- Both returned: file not found.

### Result
- No log fragments recovered.
- No alternate logs available.
- No audit trail of the deletion.

## 3. Integrity Assessment
- The system had **no active audit logging**.
- Log deletion left **zero forensic footprint**.
- Demonstrates a realistic scenario where attackers wipe logs and defenders cannot recover evidence.

## 4. Key Takeaway
Without:
- auditd  
- syslog  
- log backups  
- immutable logging  

…a system becomes blind to tampering.
