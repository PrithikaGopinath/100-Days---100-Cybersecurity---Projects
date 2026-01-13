#!/bin/bash

# Day 12 — Network Forensics Script

echo "[+] Active listeners:"
ss -tulnp

echo "[+] Mapping SSH PID:"
ps -p 1157 -o pid,ppid,user,cmd

echo "[+] Binary type:"
file /usr/sbin/sshd

echo "[+] Strings output:"
strings /usr/sbin/sshd | head
