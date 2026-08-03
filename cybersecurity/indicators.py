def detect_indicators(features):
    """
    Detect suspicious cybersecurity indicators and
    return them with their corresponding risk points.
    """

    indicators = []

    # HTTP
    if features["scheme"] != "https":
        indicators.append({
            "message": "Uses HTTP instead of HTTPS",
            "points": 20
        })

    # IP Address
    if features["has_ip"]:
        indicators.append({
            "message": "Uses an IP address instead of a domain",
            "points": 30
        })

    # URL Length
    if features["url_length"] > 75:
        indicators.append({
            "message": "Excessively long URL",
            "points": 10
        })

    # Hyphens
    if features["hyphen_count"] >= 2:
        indicators.append({
            "message": "Multiple hyphens detected",
            "points": 8
        })

    # Digits
    if features["digit_count"] >= 3:
        indicators.append({
            "message": "High number of digits",
            "points": 5
        })

    # Subdomains
    if features["subdomain_count"] >= 2:
        indicators.append({
            "message": "Multiple subdomains",
            "points": 12
        })

    # Suspicious TLDs
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

    for tld in suspicious_tlds:
        if features["domain"].endswith(tld):
            indicators.append({
                "message": f"Suspicious top-level domain ({tld})",
                "points": 15
            })
            break

    # High Entropy
    if features["url_entropy"] >= 4.5:
        indicators.append({
            "message": "High URL entropy",
            "points": 15
        })
    elif features["url_entropy"] >= 4.0:
        indicators.append({
            "message": "Moderately high URL entropy",
            "points": 10
        })

    # Suspicious Keywords
    keywords = [
        "login",
        "secure",
        "verify",
        "update",
        "signin",
        "account",
        "bank",
        "password",
    ]

    url = features["full_url"].lower()

    for keyword in keywords:
        if keyword in url:
            indicators.append({
                "message": f"Suspicious keyword: {keyword}",
                "points": 10
            })

    return indicators