# Day 09 – Linux Log Tampering And Forensic Recovery

## Objective
Simulate log tampering on a Linux system and attempt forensic recovery to understand how attackers erase traces and how defenders detect or respond when logs are missing.

## Key Concepts
- Log tampering and deletion
- Forensic recovery limitations
- Importance of audit logging and log redundancy
- Behaviour of systems with incomplete logging

## Tools Used
- grep
- strings
- tee
- rm
- (Optional) extundelete, foremost

## Lab Tasks
1. Create and delete `/var/log/auth.log` to simulate attacker log wiping.
2. Attempt to recover deleted log fragments using `strings` and `grep`.
3. Check for audit logs or alternate logs (`audit.log`, `syslog`).
4. Document the results and assess forensic readiness.

## Outcome
The system allowed log deletion with no audit trail and no recoverable fragments. This demonstrates how attackers can erase evidence on systems without proper logging or monitoring enabled.
