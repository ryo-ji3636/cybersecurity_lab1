
import re
from collections import Counter, defaultdict
from pathlib import Path

LOG_FILE = Path("data/auth.log")
ALERT_THRESHOLD = 3

failed_by_ip = Counter()
users_by_ip = defaultdict(set)
successful_logins = []

failed_pattern = re.compile(
    r"Failed password for (?:invalid user |user )?"
    r"(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

success_pattern = re.compile(
    r"Accepted publickey for (\S+) from "
    r"(\d+\.\d+\.\d+\.\d+)"
)

if not LOG_FILE.exists():
    raise SystemExit(f"Log file not found: {LOG_FILE}")

with LOG_FILE.open(encoding="utf-8") as log_file:
    for line in log_file:
        failed_match = failed_pattern.search(line)
        success_match = success_pattern.search(line)

        if failed_match:
            username = failed_match.group(1)
            ip_address = failed_match.group(2)

            failed_by_ip[ip_address] += 1
            users_by_ip[ip_address].add(username)

        if success_match:
            username = success_match.group(1)
            ip_address = success_match.group(2)
            successful_logins.append((username, ip_address))

print("=== Failed Login Attempts ===")

for ip_address, count in failed_by_ip.most_common():
    users = ", ".join(sorted(users_by_ip[ip_address]))
    print(f"{ip_address}: {count} failures; users: {users}")

    if count >= ALERT_THRESHOLD:
        print("  [ALERT] Failed login threshold reached!")

print("\n=== Successful Public-Key Logins ===")

for username, ip_address in successful_logins:
    print(f"user={username}, ip={ip_address}")

print("\n=== Investigation Summary ===")
print(f"Unique IPs with failures: {len(failed_by_ip)}")
print(f"Total failed attempts: {sum(failed_by_ip.values())}")
print(f"Successful public-key logins: {len(successful_logins)}")
