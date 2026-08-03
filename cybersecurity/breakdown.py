def generate_score_breakdown(features):
    """
    Return a breakdown of the risk score.
    """

    breakdown = []

    if features["scheme"] != "https":
        breakdown.append(("Uses HTTP instead of HTTPS", 20))

    if features["has_ip"]:
        breakdown.append(("Uses an IP Address", 30))

    if features["url_length"] > 75:
        breakdown.append(("Long URL", 10))

    if features["hyphen_count"] >= 2:
        breakdown.append(("Multiple Hyphens", 8))

    if features["digit_count"] >= 3:
        breakdown.append(("High Digit Count", 5))

    if features["subdomain_count"] >= 2:
        breakdown.append(("Multiple Subdomains", 12))

    if features["url_entropy"] >= 4.5:
        breakdown.append(("High URL Entropy", 15))
    elif features["url_entropy"] >= 4.0:
        breakdown.append(("Moderately High URL Entropy", 10))

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
            breakdown.append((f"Suspicious TLD ({tld})", 15))
            break

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
            breakdown.append((f"Keyword: {keyword}", 10))

    return breakdown