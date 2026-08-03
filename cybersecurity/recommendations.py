def generate_recommendation(risk_score):
    """
    Generate a recommendation based on the calculated risk score.
    """

    if risk_score >= 85:
        return (
            "Critical risk detected. Block access immediately and do not "
            "enter credentials or personal information."
        )

    elif risk_score >= 65:
        return (
            "High risk detected. Avoid interacting with this website."
        )

    elif risk_score >= 40:
        return (
            "Medium risk detected. Verify the website before proceeding."
        )

    elif risk_score >= 15:
        return (
            "Low risk detected. Exercise caution while browsing."
        )

    return (
        "No significant phishing indicators detected."
    )