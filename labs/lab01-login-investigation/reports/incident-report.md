# SSH Login Investigation Report

## 1. Objective

The objective was to analyze SSH authentication logs and identify suspicious login activity.

## 2. Findings

- Total failed login attempts: 7
- IP addresses with failed attempts: 2
- Successful public-key logins: 2

### Suspicious Activity

**IP address: 203.0.113.25**
- Failed login attempts: 4
- Usernames: admin and alice
- Assessment: This IP is suspicious because it attempted to log in using multiple usernames.

**IP address: 198.51.100.40**
- Failed login attempts: 3
- Username: root
- Assessment: Repeated attempts to log in as root should be investigated.

## 3. Successful Logins

- alice from 192.0.2.10
- bob from 192.0.2.15

The log shows successful public-key authentication for these two accounts. The available data does not establish whether the logins were authorized.

## 4. Limitations

These logs are synthetic training data. The IP addresses are reserved for documentation and examples. This investigation does not prove that a real attack occurred or that any account was compromised.

## 5. Recommendations

1. Review the failed login attempts and check whether the activity is expected.
2. Verify that successful logins were authorized.
3. Monitor repeated failures and attempts involving privileged accounts such as root.
4. Use an appropriate alert threshold and review it regularly.

## 6. Conclusion

The analysis identified two IP addresses with repeated failed login attempts. The results indicate activity worth investigating, but more evidence would be needed to determine whether the activity was malicious.
