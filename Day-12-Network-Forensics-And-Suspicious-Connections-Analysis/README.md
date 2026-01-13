# Day 12 — Linux Network Forensics & Suspicious Connections Analysis

This module focuses on identifying and analysing active network listeners on a Linux system.  
The goal is to map open ports to running processes, investigate the associated binaries,  
and determine whether any suspicious or unauthorised services are present.

## Objectives
- Identify active and listening network ports
- Map ports to processes and users
- Analyse the binary behind the process
- Capture evidence for forensic documentation
- Assess whether the system shows signs of compromise

## Summary of Findings
Day 12 confirmed a clean system state.  
The only active listener was the SSH daemon (`sshd`) on port 22, running as root.  
Binary analysis showed no anomalies, and no persistence mechanisms or suspicious services were detected.

## Files
- `findings.md` — forensic summary and conclusions  
- `notes.md` — raw investigation notes and commands  
- `script.sh` — commands used during the analysis  
- `evidence/` — screenshots of command outputs  
