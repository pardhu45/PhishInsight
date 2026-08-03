import math
from collections import Counter

import ipaddress
from urllib.parse import urlparse


from urllib.parse import urlparse


def is_valid_url(url):
    """
    Check whether a URL is syntactically valid.
    """

    parsed = urlparse(url)

    return (
        parsed.scheme in ["http", "https"]
        and parsed.netloc != ""
        and "." in parsed.netloc
    )

def is_ip_address(domain):
    """
    Check whether the domain is an IP address.
    """

    try:
        ipaddress.ip_address(domain.split(":")[0])
        return True
    except ValueError:
        return False


def calculate_entropy(text):
    """
    Calculate Shannon entropy of a string.
    """

    if not text:
        return 0

    counts = Counter(text)
    length = len(text)

    entropy = 0

    for count in counts.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return round(entropy, 2)

def extract_basic_features(url):
    """
    Extract basic URL features.
    """

    parsed = urlparse(url)

    return {
        "full_url": url,
        "url_length": len(url),
        "domain": parsed.netloc,
        "path": parsed.path,
        "scheme": parsed.scheme,
        "dot_count": url.count("."),
        "hyphen_count": url.count("-"),
        "digit_count": sum(c.isdigit() for c in url),
        "subdomain_count": (
            0
            if is_ip_address(parsed.netloc)
            else max(parsed.netloc.count(".") - 1, 0)
        ),
        "has_ip": is_ip_address(parsed.netloc),
        "special_char_count": sum(
            not c.isalnum() and c not in [":", "/", ".", "-"]
            for c in url
        ),
        "query_count": len(parsed.query.split("&")) if parsed.query else 0,
        "port": parsed.port,
        "url_entropy": calculate_entropy(url),
    }

def score_https(features):
    """
    Score based on HTTP/HTTPS usage.
    """
    return 20 if features["scheme"] != "https" else 0


def score_url_length(features):
    """
    Score based on URL length.
    """

    if features["url_length"] > 100:
        return 15

    elif features["url_length"] > 75:
        return 10

    elif features["url_length"] > 50:
        return 5

    return 0

def calculate_risk_score(features):
    """
    Calculate a cybersecurity risk score based on URL features.
    """

    score = 0

    score += score_https(features)

    if features["scheme"] != "https":
        score += 20

    score += score_url_length(features)

    if features["hyphen_count"] >= 2:
        score += 8

    if features["dot_count"] >= 3:
        score += 5

    if features["digit_count"] >= 3:
        score += 5

    if features["subdomain_count"] >= 2:
        score += 12
    suspicious_tlds = [
    ".xyz",
    ".top",
    ".tk",
    ".gq",
    ".ml",
    ".cf",
    ".click",
    ".work",
    ".zip",
    ]

    if any(features["domain"].endswith(tld) for tld in suspicious_tlds):
        score += 15

    return min(score, 100)