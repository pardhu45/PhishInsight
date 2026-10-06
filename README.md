# 🛡️ PhishInsight

> Phishing URL Detection & Threat Analysis Platform

PhishInsight is a cybersecurity web application that analyzes URLs for phishing indicators using a rule-based detection engine. It evaluates multiple security features, calculates a risk score, classifies the threat level, and provides detailed explanations to help users understand why a URL is considered safe or suspicious.

---

## ✨ Features

- URL Validation
- Phishing URL Detection
- Risk Score Calculation (0–100)
- Threat Level Classification
- Threat Indicator Detection
- Detailed Risk Analysis
- Explainable Security Recommendations
- Modern Web Dashboard
- Flask-Based Backend

---

## 🛠 Technologies Used

- Python
- Flask
- HTML5
- Tailwind CSS
- Jinja2
- JavaScript

---

## 🚀 Project Status

**Version:** v1.0.0

This project is currently under active development.

---

## 📖 Overview

PhishInsight is a web-based cybersecurity application designed to identify potentially malicious URLs through rule-based threat analysis. Instead of relying solely on machine learning, the application examines multiple characteristics of a URL, including protocol, domain structure, suspicious keywords, entropy, special characters, query parameters, and other security indicators.

The application calculates a comprehensive risk score, classifies the URL into one of five threat levels (SAFE, LOW, MEDIUM, HIGH, or CRITICAL), and provides a transparent explanation of the factors contributing to the final assessment. This explainable approach helps users understand why a URL is considered suspicious rather than simply presenting a score.

PhishInsight is intended as a portfolio project that demonstrates practical cybersecurity concepts, secure web application development with Flask, and the implementation of a custom phishing detection engine.

---

## 🚀 Key Features

### 🔍 URL Validation
- Validates the input URL before analysis.
- Detects invalid or malformed URLs.

### 🛡️ Threat Detection
- Identifies suspicious phishing characteristics using a rule-based detection engine.

### 📊 Risk Score Calculation
- Generates a risk score ranging from **0 to 100** based on multiple security indicators.

### 🚨 Threat Classification
Each analyzed URL is classified into one of the following levels:

- 🟢 SAFE
- 🟡 LOW
- 🟠 MEDIUM
- 🔴 HIGH
- 🔥 CRITICAL

### 📋 Threat Indicators
Displays every suspicious indicator detected during analysis, including:
- HTTP instead of HTTPS
- IP Address Usage
- Suspicious Top-Level Domains
- Multiple Hyphens
- High Digit Count
- Suspicious Keywords
- High URL Entropy
- Query Parameter Analysis

### 📈 Risk Analysis
Provides a detailed breakdown showing how each indicator contributed to the final risk score.

### 💡 Security Recommendations
Generates recommendations based on the calculated threat level to help users make informed decisions.

### 🎨 Modern Dashboard
- Clean cybersecurity-themed interface
- Color-coded threat levels
- Interactive risk meter
- Easy-to-read analysis results

---

## 🔄 Detection Workflow

The URL analysis process follows a structured pipeline to ensure consistent and explainable threat detection.

```text
User Input URL
       │
       ▼
URL Validation
       │
       ▼
Feature Extraction
       │
       ├── Protocol (HTTP / HTTPS)
       ├── Domain Analysis
       ├── IP Address Detection
       ├── URL Length
       ├── Suspicious Keywords
       ├── Special Characters
       ├── Query Parameters
       └── URL Entropy
       │
       ▼
Threat Indicator Detection
       │
       ▼
Risk Score Calculation (0–100)
       │
       ▼
Threat Classification
(SAFE • LOW • MEDIUM • HIGH • CRITICAL)
       │
       ▼
Security Recommendation
       │
       ▼
Interactive Dashboard
```

### Detection Process

1. The user submits a URL through the web interface.
2. The application validates the URL format.
3. Multiple security-related features are extracted from the URL.
4. Each suspicious feature contributes to the overall risk score.
5. The final score determines the threat level.
6. Threat indicators and a detailed risk breakdown are displayed.
7. A security recommendation is generated based on the final assessment.


---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/PhishInsight.git
```

### 2. Navigate to the Project Directory

```bash
cd PhishInsight
```

### 3. Create a Virtual Environment

**Windows**

```bash
python -m venv .phish
.phish\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .phish
source .phish/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Your Browser

```
http://127.0.0.1:5000
```

---

## 🚀 Usage

1. Launch the Flask application.
2. Enter a URL into the scanner.
3. Click **Analyze URL**.
4. Review the generated:
   - Threat Level
   - Risk Score
   - Threat Indicators
   - Risk Analysis
   - Security Recommendation
5. Use the results to determine whether the URL appears safe or suspicious.


---

## 📂 Project Structure

```text
PhishInsight/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── backend/
│   ├── analyzer.py
│   ├── routes.py
│   └── __init__.py
│
├── cybersecurity/
│   ├── url_features.py
│   ├── scoring.py
│   ├── indicators.py
│   ├── breakdown.py
│   ├── recommendations.py
│   └── __init__.py
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   ├── images/
│   │   └── js/
│   │
│   └── templates/
│       ├── components/
│       ├── base.html
│       └── index.html
│
└── screenshots/
```

---

## 🔮 Future Enhancements

The following features are planned for future releases of **PhishInsight**:

### Version 1.1
- Scan History
- SQLite Database Integration
- Search & Filter Previous Scans

### Version 1.2
- Security Analytics Dashboard
- Risk Trend Charts
- Scan Statistics

### Version 1.3
- Interactive Dashboard
- System Health Overview
- Recent Activity Panel

### Version 1.4
- About Page
- Application Settings
- Export Reports (PDF / CSV)

### Version 2.0
- Machine Learning-Based Phishing Detection
- VirusTotal API Integration
- WHOIS Lookup
- Google Safe Browsing Integration
- Threat Intelligence Feeds
- User Authentication

---

## 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Pardhasaradhi Naidu**

Cybersecurity Enthusiast 

If you found this project interesting, feel free to connect with me on LinkedIn and explore the repository on GitHub.
