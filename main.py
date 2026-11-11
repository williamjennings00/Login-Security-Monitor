
events = [
    {
        "timestamp": "2026-11-11T14:30:00",
        "ip": "192.168.1.10",
        "status": "FAILED"
    },
    {
        "timestamp": "2026-11-11T14:30:15",
        "ip": "192.168.1.10",
        "status": "FAILED"
    },
    {
        "timestamp": "2026-11-11T14:30:20",
        "ip": "10.0.0.5",
        "status": "SUCCESS"
    },
    {
        "timestamp": "2026-11-11T14:30:35",
        "ip": "192.168.1.10",
        "status": "FAILED"
    },
    {
        "timestamp": "2026-11-11T14:35:00",
        "ip": "10.0.0.5",
        "status": "FAILED"
    }
]



def count_failed_logins(events: list[dict]) -> dict:
    ip_failed_occurrences = {}

    for event in events:
        ip = event["ip"]
        status = event["status"]

        if status == "FAILED":
            ip_failed_occurrences[ip] = ip_failed_occurrences.get(ip, 0) + 1

    return ip_failed_occurrences




def detect_suspicious_ips(failed_logins: dict, threshold: int = 3) -> list:
    suspicious_ips = []

    for ip, count in failed_logins.items():
        if count >= threshold:
            suspicious_ips.append(ip)

    return suspicious_ips

