# Day 01 – Linux Authentication Log Attack Detection

## Objective
Detect suspicious SSH login activity using Linux authentication logs.

## Tools Used
- Kali Linux
- Bash scripting
- journalctl, grep, awk

## What I Did
1. Simulated multiple failed SSH login attempts using incorrect credentials.
2. Queried system logs for failed authentication events.
3. Counted failed attempts per source to identify abnormal patterns.
4. Queried logs for successful logins to check if any followed failed attempts.
5. Created a Bash script to automatically detect brute-force behaviour.
6. Documented the findings in an incident report.

## Findings
- Multiple failed SSH login attempts were detected.
- Attempts targeted common usernames.
- Successful logins were observed after repeated failures, indicating possible brute-force behaviour.
- Activity pattern matched typical SSH attack reconnaissance.

## Recommendations
- Enable SSH key-based authentication.
- Configure fail2ban to block repeated failed attempts.
- Disable direct login for privileged accounts.
- Forward logs to a SIEM for continuous monitoring.

## Reflection
This project helped me understand how brute-force attacks appear in Linux logs and how to detect them using command-line tools and automation.

