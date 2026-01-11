# Day 10 – Analyse Suspicious Cron Jobs

## Overview
This task focuses on analysing cron jobs on a Linux system to detect potential persistence mechanisms or malicious automation. Cron jobs are commonly used for legitimate system maintenance, but attackers may abuse them to maintain access or execute payloads automatically.

## Objectives
- Enumerate user and root cron jobs
- Inspect system-wide cron directories
- Review `/etc/crontab` for scheduled tasks
- Identify any unusual or suspicious entries
- Document findings and commands used

## Tools Used
- `crontab`
- `ls`
- `cat`
- `grep`
- `awk`

## Outcome Summary
All inspected cron locations contained only default system scripts. No unexpected or suspicious cron jobs were identified during the analysis.
