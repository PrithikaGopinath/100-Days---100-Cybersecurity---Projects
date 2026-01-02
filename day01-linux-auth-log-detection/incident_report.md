# Incident Report – SSH Brute Force Activity

## Summary
Multiple failed SSH login attempts were detected from a single IP address.

## Indicators of Compromise
- Repeated failed SSH authentication attempts
- Targeted common usernames such as root and admin

## Recommendations
- Configure fail2ban
- Disable root SSH login
- Use SSH key-based authentication
