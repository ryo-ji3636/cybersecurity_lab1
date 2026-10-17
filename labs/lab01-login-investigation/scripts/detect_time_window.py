import re
from collections import defaultdict, deque
from datetime import datetime, timedelta
from pathlib import Path

LOG_FILE = Path("data/test_auth.log")
ALERT_THRESHOLD = 3
WINDOW = timedelta(minutes=5)

failed_pattern = re.compile(
    r"Failed password for (?:invalid user |user )?"
    r"(\S+) from (\d+\.\d+\.\d+\.\d+)"
)

# Each IP has its own queue of failure timestamps.
failed_times = defaultdict(deque)

if not LOG_FILE.exists():
    raise SystemExit(f"Log file not found: {LOG_FILE}")

with LOG_FILE.open(encoding="utf-8") as log_file:
    for line in log_file:
        match = failed_pattern.search(line)

        if not match:
            continue

        username = match.group(1)
        ip_address = match.group(2)

        timestamp_text = " ".join(line.split()[:3])
        event_time = datetime.strptime(
            timestamp_text, "%b %d %H:%M:%S"
        ).replace(year=2026)

        timestamps = failed_times[ip_address]

        # Remove failures older than the 5-minute window.
        while timestamps and event_time - timestamps[0] > WINDOW:
            timestamps.popleft()

        # Add the current failure.
        timestamps.append(event_time)

        count = len(timestamps)

        print(
            f"time={event_time} "
            f"ip={ip_address} "
            f"user={username} "
            f"failures_in_5min={count}"
        )

        if count >= ALERT_THRESHOLD:
            print(
                f"  [ALERT] {ip_address} "
                f"reached {count} failures within 5 minutes!"
            )