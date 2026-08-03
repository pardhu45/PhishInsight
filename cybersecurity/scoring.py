from pyexpat import features


def score_https(features):
    """
    Assign risk points if the URL uses HTTP instead of HTTPS.
    """

    return 20 if features["scheme"] != "https" else 0


def score_url_length(features):
    """
    Assign risk points based on URL length.
    """

    if features["url_length"] > 100:
        return 15

    elif features["url_length"] > 75:
        return 10

    elif features["url_length"] > 50:
        return 5

    return 0

def calculate_risk_score(features):
    score = 0

    

    score += score_https(features)
    score += score_url_length(features)
    score += score_keywords(features)
    score += score_ip_address(features)
    score += score_special_characters(features)
    score += score_query_parameters(features)
    score += score_port(features)
    score += score_entropy(features)
    score += score_tld(features)
    score += score_digits(features)

    return min(score, 100)

def score_keywords(features):
    """
    Assign risk points based on suspicious keywords.
    """

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

    score = 0

    url = features["full_url"].lower()

    for keyword in keywords:
        if keyword in url:
            score += 10

    return min(score, 60)

def score_ip_address(features):
    """
    Assign risk points if the URL uses an IP address.
    """

    if features["has_ip"]:
        return 30

    return 0

def score_special_characters(features):
    """
    Assign risk points for excessive special characters.
    """

    if features["special_char_count"] >= 8:
        return 10

    elif features["special_char_count"] >= 5:
        return 5

    return 0

def score_query_parameters(features):
    """
    Assign risk points for excessive query parameters.
    """

    if features["query_count"] >= 5:
        return 10

    elif features["query_count"] >= 2:
        return 5

    return 0


def score_port(features):
    """
    Assign risk points for uncommon ports.
    """

    if features["port"] and features["port"] not in [80, 443]:
        return 10

    return 0

def score_entropy(features):
    """
    Assign risk points based on URL entropy.
    """

    entropy = features["url_entropy"]

    if entropy >= 4.5:
        return 15

    elif entropy >= 4.0:
        return 10

    elif entropy >= 3.5:
        return 5

    return 0

def score_tld(features):
    """
    Assign risk points for suspicious top-level domains.
    """

    suspicious_tlds = [
        ".xyz",
        ".top",
        ".click",
        ".shop",
        ".info",
        ".live",
        ".site",
    ]

    domain = features["domain"].lower()

    for tld in suspicious_tlds:
        if domain.endswith(tld):
            return 15

    return 0

def score_digits(features):
    """
    Assign risk points for excessive digits in the URL.
    """

    digits = features["digit_count"]

    if digits >= 10:
        return 10

    elif digits >= 5:
        return 5

    return 0