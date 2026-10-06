# Project Report — Phishing Email Detection & Awareness Dashboard

## Abstract
Phishing is a social-engineering threat in which attackers manipulate users into unsafe actions.
This project implements a local defensive analyzer that examines sender information, email content,
URLs, and selected message characteristics. It produces an explainable risk score, classification,
findings, recommendations, analysis history, and awareness guidance.

## Objectives
- Identify common phishing indicators.
- Demonstrate email-security concepts.
- Apply feature engineering and rule-based detection.
- Provide explainable security decisions.
- Demonstrate optional machine learning.
- Store analysis history for analytics.
- Teach users how to recognize phishing.
- Build a safe portfolio project without attacking real systems.

## Methodology
Input -> Parsing -> Feature extraction -> Rule analysis -> Risk scoring -> Classification -> Explanation -> Storage -> Analytics.

## Modules
### Sender analysis
Checks sender formatting and patterns such as trusted-looking display names paired with free-mail domains.

### Content analysis
Looks for urgency, credential requests, financial themes, threat language, attachments, and excessive capitalization.

### URL analysis
Extracts URLs without visiting them. Checks IP hosts, @ symbols, punycode, shorteners, unusual TLDs,
deep subdomains, long URLs, and non-standard ports.

### Risk scoring
Signals contribute weighted points. The score is capped at 100 and mapped to four classifications.

### Machine learning
The optional model uses TF-IDF + Logistic Regression on a small synthetic dataset. It is a supporting
signal rather than the sole decision-maker.

### Database
SQLite stores timestamp, sender, subject, score, classification, finding count, and a JSON result.

## Security and ethics
No credentials are collected. No real phishing messages are sent. No target systems are scanned.
The URL analyzer does not request remote pages. Demonstration domains are fictional/reserved.

## Limitations
The project does not independently verify SPF/DKIM/DMARC, detonate attachments, inspect reputation feeds,
or replace enterprise secure email gateways. It is a student defensive-security prototype.

## Future work
Authorized mail-header authentication analysis, threat-intelligence integration, multilingual NLP,
model monitoring, and controlled SIEM/SOAR integration.

## Conclusion
The project demonstrates practical cybersecurity engineering through phishing detection, social-engineering
analysis, safe URL inspection, explainable risk scoring, machine learning, database persistence, analytics,
testing, and security awareness.
