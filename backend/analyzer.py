from cybersecurity.url_features import (
    is_valid_url,
    extract_basic_features
)

from cybersecurity.scoring import calculate_risk_score
from cybersecurity.indicators import detect_indicators
from cybersecurity.recommendations import generate_recommendation
from cybersecurity.breakdown import generate_score_breakdown


def analyze_url(url):
    """
    Analyze a URL and return a phishing assessment.
    """

    url = url.lower().strip()

    # Validate URL
    if not is_valid_url(url):
        return {
            "url": url,
            "status": "Invalid URL",
            "threat_level": "INVALID",
            "risk_score": 0,
            "confidence": 0,
            "recommendation": "Please enter a valid URL.",
            "indicators": [],
            "breakdown": [],
        }

    # Extract Features
    features = extract_basic_features(url)

    # Calculate Risk Score
    risk_score = calculate_risk_score(features)

    # Generate Explainable Indicators
    indicators = detect_indicators(features)

    # Generate Score Breakdown
    breakdown = generate_score_breakdown(features)

    # Generate Recommendation
    recommendation = generate_recommendation(risk_score)

    # Determine Threat Level
    if risk_score >= 85:
        threat_level = "CRITICAL"

    elif risk_score >= 65:
        threat_level = "HIGH"

    elif risk_score >= 40:
        threat_level = "MEDIUM"

    elif risk_score >= 15:
        threat_level = "LOW"

    else:
        threat_level = "SAFE"

    return {
        "url": url,
        "status": "Analysis Complete",
        "threat_level": threat_level,
        "risk_score": risk_score,
        "confidence": 98,
        "recommendation": recommendation,
        "indicators": indicators,
        "breakdown": breakdown,
    }