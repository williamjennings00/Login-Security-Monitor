
events = [
    ("192.168.1.10", "FAILED"),
    ("192.168.1.10", "FAILED"),
    ("10.0.0.5", "SUCCESS"),
    ("192.168.1.10", "FAILED"),
    ("10.0.0.5", "FAILED")
]


def count_failed_logins(events: list):
    ip_failed_occurrences = {}

    for ip, status in events:
        if status == "FAILED":
            ip_failed_occurrences[ip] = ip_failed_occurrences.get(ip, 0) + 1

    return ip_failed_occurrences



def detect_suspicious_ips(failed_logins: dict, threshold: int = 3) -> list:
    suspicious_ips = []

    for ip, count in failed_logins.items():
        if count >= threshold:
            suspicious_ips.append(ip)

    return suspicious_ips

