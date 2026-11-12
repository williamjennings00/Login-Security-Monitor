from datetime import datetime, timedelta
import json



def load_login_events(file_path: str) -> list[dict[str, str]]:
    
    with open(file_path, "logs.json", "r") as file:
        events = json.load(file)

    return events

def list_events_in_time_duration(
    events: list[dict[str, str]],
    seconds: int = 60
) -> list[dict[str, str]]:

    events_in_time_duration = []

    if not events:
        return events_in_time_duration

    latest_time = max(
        datetime.fromisoformat(event["timestamp"])
        for event in events
    )

    cutoff_time = latest_time - timedelta(seconds=seconds)

    for event in events:
        current_time = datetime.fromisoformat(event["timestamp"])

        if cutoff_time <= current_time <= latest_time:
            events_in_time_duration.append(event)

    return events_in_time_duration




def count_failed_logins(events: list[dict[str, str]]) -> dict[str, int]:
    ip_failed_occurrences = {}

    for event in events:
        ip = event["ip"]
        status = event["status"]

        if status == "FAILED":
            ip_failed_occurrences[ip] = ip_failed_occurrences.get(ip, 0) + 1

    return ip_failed_occurrences




def detect_suspicious_ips(
    failed_logins: dict[str, int],
    threshold: int = 3
) -> list[str]:
    
    suspicious_ips = []

    for ip, count in failed_logins.items():
        if count >= threshold:
            suspicious_ips.append(ip)

    return suspicious_ips




