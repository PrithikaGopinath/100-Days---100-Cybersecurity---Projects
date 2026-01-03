#!/bin/bash

LOG="/var/log/auth.log"
THRESHOLD=5

echo "Suspicious IPs with more than $THRESHOLD failed login attempts:"
grep "Failed password" $LOG \
| awk '{print $(NF-3)}' \
| sort \
| uniq -c \
| awk -v t=$THRESHOLD '$1 > t {print $2 " = " $1 " attempts"}'
