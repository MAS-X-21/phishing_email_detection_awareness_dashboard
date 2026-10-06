# Interview / Viva Preparation

## 1. What problem does the project solve?
It helps users identify common phishing indicators in email samples and explains why a message may be risky.

## 2. Is it an attack tool?
No. It is a defensive analyzer. It does not send phishing emails, collect credentials, or attack systems.

## 3. What is phishing?
Phishing is social engineering that attempts to trick a user into unsafe actions such as revealing information,
making payments, or opening malicious content.

## 4. Why use rule-based detection?
Rules are transparent and explainable. Analysts can see exactly why a signal contributed to the score.

## 5. Why add machine learning?
ML can learn text patterns from examples and provide a second signal. It should not blindly replace deterministic controls.

## 6. Why TF-IDF?
TF-IDF converts text into numerical features based on word importance, making it a simple baseline for text classification.

## 7. Why Logistic Regression?
It is fast and effective for sparse text features and can provide probabilities useful as a supporting signal.

## 8. How does URL analysis work?
The program extracts URLs and parses them locally. It checks structural properties such as IP hosts, @ symbols,
punycode, shorteners, long URLs, deep subdomains, unusual ports and selected TLD patterns. It does not visit the URL.

## 9. How is risk score calculated?
Each detected signal has a weight. The strongest unique signal per title is counted and the final score is capped at 100.

## 10. Why is explainability important?
Analysts and users need to understand why a message was flagged so they can verify it rather than blindly trusting automation.

## 11. Why SQLite?
It is lightweight, serverless, included with Python, and sufficient for a local student project.

## 12. What are false positives?
Legitimate messages incorrectly flagged as suspicious.

## 13. What are false negatives?
Phishing messages incorrectly treated as safe. This matters because a low score never proves safety.

## 14. How would you improve it for production?
Add authorized SPF/DKIM/DMARC analysis, enterprise threat intelligence, stronger NLP, attachment sandboxing,
reputation data, model monitoring, access controls, SIEM/SOAR workflows, and a much larger representative dataset.

## 15. What cybersecurity concepts are demonstrated?
Phishing detection, social engineering, URL analysis, threat scoring, defensive analytics, secure coding,
explainability, data persistence, testing, and security awareness.
