# Incident Report – SSH Brute Force Activity

## Summary
Unusual SSH authentication activity was detected, involving repeated failed login attempts followed by successful authentication events.

## Indicators of Compromise
- Multiple failed SSH login attempts within a short time window.
- Attempts targeting common or default usernames.
- Successful authentication occurring shortly after repeated failures.

## Analysis
The pattern of activity is consistent with brute-force or credential-stuffing behaviour. The attacker may have attempted multiple password combinations before eventually gaining access.

## Recommendations
- Implement fail2ban or similar intrusion prevention tools.
- Enforce SSH key-based authentication.
- Disable password authentication where possible.
- Restrict SSH access to trusted networks.
- Forward authentication logs to a SIEM for alerting and correlation.

## Conclusion
The activity indicates a likely brute-force attempt that requires further monitoring and hardening of SSH access controls.


