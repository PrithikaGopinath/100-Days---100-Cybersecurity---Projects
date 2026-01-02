# Day 1 – Linux Authentication Log Attack Detection

## Objective
Detect suspicious SSH login activity using Linux authentication logs.

## Tools Used
- Linux
- Bash
- grep, awk
- journalctl

## What I Did
- Analyzed authentication logs
- Identified failed SSH login attempts
- Learned how brute-force attacks appear in logs

## Detection Logic
More than 5 failed login attempts from the same IP indicates suspicious activity.

## Mitigation Steps
- Enable fail2ban
- Disable root SSH login
- Use SSH key authentication
