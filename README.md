# 🛡️ Phishing Email Detection & Awareness Dashboard

A defensive, educational cybersecurity application that analyzes synthetic/sample emails for phishing indicators, suspicious URLs, sender anomalies, social-engineering language, and other security signals.

The application combines **explainable rule-based detection** with an **optional machine-learning classifier** to generate a phishing risk score and provide security recommendations.

> ⚠️ **Safety & Ethics:** This project is designed strictly for defensive cybersecurity education. It uses synthetic/sample emails and does not send phishing emails, collect credentials, create credential-harvesting pages, or attack real users, organizations, websites, or systems. URLs are analyzed as text and are not visited.

---

## 📌 Project Overview

Phishing attacks commonly use social engineering techniques such as urgency, threats, impersonation, suspicious links, and requests for credentials.

This project demonstrates how a defensive email-security system can identify these indicators and explain why an email may be suspicious.

The dashboard allows a user to:

* Paste email content
* Enter sender information
* Enter an email subject
* Upload safe `.txt` or `.eml` samples
* Analyze suspicious URLs
* Detect urgency and manipulation language
* Detect credential-related requests
* Analyze sender patterns
* Calculate a phishing risk score
* Classify emails by risk level
* View explainable findings
* Receive security recommendations
* Store analysis history
* View security analytics
* Learn phishing-awareness concepts

---

## 🎯 Objectives

The main objectives of this project are to demonstrate:

* Cybersecurity fundamentals
* Email security analysis
* Phishing detection
* Social-engineering detection
* URL security analysis
* Sender analysis
* Feature engineering
* Rule-based detection
* Explainable security decisions
* Machine-learning classification
* Threat/risk scoring
* Security analytics
* Secure and defensive programming
* Security awareness education

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────────┐
                    │       User / Analyst     │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
                    │    Streamlit Dashboard   │
                    └────────────┬─────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼
        ┌─────────────┐  ┌─────────────┐  ┌──────────────┐
        │   Content   │  │    URL      │  │    Sender    │
        │   Analyzer  │  │   Analyzer  │  │   Analyzer   │
        └──────┬──────┘  └──────┬──────┘  └───────┬──────┘
               │                │                  │
               └────────────────┼──────────────────┘
                                ▼
                     ┌─────────────────────┐
                     │  Rule-Based Engine  │
                     └──────────┬──────────┘
                                │
                                ▼
                     ┌─────────────────────┐
                     │    Risk Scoring     │
                     └──────────┬──────────┘
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
       ┌──────────────────┐          ┌──────────────────┐
       │ Optional ML Model│          │ Explainable      │
       │  Classification  │          │ Findings         │
       └────────┬─────────┘          └────────┬─────────┘
                │                             │
                └──────────────┬──────────────┘
                               ▼
                    ┌─────────────────────────┐
                    │ Classification & Advice │
                    └────────────┬────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ History & Security      │
                    │ Analytics Dashboard     │
                    └─────────────────────────┘
```

---

## 🔍 Detection Methodology

The project uses multiple defensive indicators.

### 1. Credential-related requests

The analyzer looks for language associated with:

* Passwords
* OTPs
* Login verification
* Account verification
* Authentication information

### 2. Urgency and manipulation

Examples include:

* Urgent
* Immediately
* Act now
* Within 24 hours
* Final warning

These techniques are commonly used to pressure recipients into making decisions without verification.

### 3. Threat and consequence language

The system identifies language related to:

* Account suspension
* Account termination
* Penalties
* Locking accounts
* Consequences for not acting

### 4. Suspicious URLs

The URL analyzer can identify indicators such as:

* IP-address URLs
* Suspicious URL structures
* Potentially unusual destinations

The application **does not visit or request these URLs**.

### 5. Sender analysis

The system can identify suspicious sender characteristics, including:

* Unusual sender formats
* Organization-like display names combined with free-mail providers
* Missing or unusual sender information

### 6. Risk scoring

Detected indicators contribute to an overall risk score from:

```text
0 ─────────────────────────────── 100
SAFE                              HIGH RISK
```

The application uses the resulting score to classify the email.

Example classifications:

* **SAFE**
* **LOW RISK**
* **SUSPICIOUS**
* **HIGH RISK / LIKELY PHISHING**

---

## 🤖 Machine Learning Component

The project includes an optional machine-learning component using a synthetic email dataset.

The ML model provides a **supporting phishing probability signal** rather than replacing the explainable rule-based engine.

This design allows the application to show both:

```text
Rule-Based Risk Score
        +
ML Probability
        ↓
Additional Security Context
```

The model was trained using synthetic/sample email data.

Because the dataset is intentionally small and educational, the ML evaluation should **not** be interpreted as production-level performance.

During testing, the current synthetic model produced approximately:

```text
Accuracy: 60%
```

This is expected to vary with such a small dataset.

---

## 📊 Example Results

### Safe Email

Example result:

```text
Risk Score: 0/100
Classification: SAFE
Findings: 0
```

### Synthetic Phishing Email

Example result:

```text
Risk Score: 80/100
Classification: HIGH RISK / LIKELY PHISHING
Findings: 5
```

Detected indicators included:

* Credential-related request
* IP-address URL
* Suspicious sender pattern
* Urgency/manipulation language
* Threat/consequence language

### Analysis History

Example dashboard statistics:

```text
Total analyses: 8
High-risk analyses: 2
Average score: 37.2
```

These values are examples from local testing and may change as additional samples are analyzed.

---

## 🖥️ Dashboard Features

### Email Analysis

Analyze:

* Sender
* Subject
* Email body
* Uploaded sample files

### Risk Analysis

Displays:

* Risk score
* Classification
* Number of findings
* Severity of findings
* Explanation for each finding
* Security recommendations

### URL Analysis

URLs are analyzed without visiting them.

### Analysis History

The application stores previous analysis results and provides historical visibility.

### Security Analytics

The dashboard provides visual analytics for analyzed emails and risk levels.

### Security Awareness

The application includes educational guidance about recognizing phishing and responding safely.

---

## 🧪 Testing

The project includes automated tests using `pytest`.

Current test status:

```text
4 passed
```

The tests cover core analyzer functionality.

Run the tests with:

```bash
pytest -q
```

If required in a Windows environment, the project can also be run with the project directory included in `PYTHONPATH`.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Dashboard

* Streamlit

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Joblib

### Visualization

* Plotly

### Testing

* Pytest

### Development Environment

* Anaconda / Conda
* Visual Studio Code
* Git
* GitHub

---

## 📁 Project Structure

```text
phishing-email-detection-awareness-dashboard/
│
├── app/
│   ├── analyzers/
│   ├── ...
│   └── main.py
│
├── data/
│   └── synthetic_emails.csv
│
├── docs/
│
├── models/
│   └── phishing_text_model.joblib
│
├── scripts/
│   └── train_model.py
│
├── tests/
│   └── test_analyzers.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

### 2. Enter the project directory

```bash
cd phishing-email-detection-awareness-dashboard
```

### 3. Create the Conda environment

```bash
conda create -n phishing-dashboard python=3.13 -y
```

### 4. Activate the environment

```bash
conda activate phishing-dashboard
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the tests

```bash
pytest -q
```

### 7. Start the dashboard

```bash
streamlit run app/main.py
```

The application should then be available locally through:

```text
http://localhost:8501
```

---

## 🧪 Safe Testing

The project should only be tested using:

* Synthetic phishing emails
* Legitimate sample emails
* Documentation/example URLs
* Controlled local files

Do not use the application to attack or test real people, organizations, systems, or websites without explicit authorization.

---

## 🔐 Security & Ethical Considerations

This project intentionally avoids offensive functionality.

It does **not**:

* Send phishing emails
* Collect passwords
* Collect OTPs
* Harvest credentials
* Create fake login pages
* Exploit websites
* Attack real users
* Visit suspicious URLs
* Perform unauthorized security testing

The goal is to demonstrate **defensive email security and security awareness**.

---

## ⚠️ Limitations

This project is an educational prototype rather than a production email-security gateway.

Current limitations include:

* Small synthetic dataset
* Limited ML training data
* Rule-based indicators
* No live threat-intelligence feeds
* No real mail-server integration
* No enterprise email gateway integration
* No guarantee of detecting every phishing message
* No guarantee that a low-risk email is safe

The application should therefore be treated as a **decision-support and educational tool**, not as a replacement for professional email-security infrastructure.

---

## 🔮 Future Enhancements

Possible future improvements include:

* Larger and more diverse datasets
* Improved ML models
* Ensemble detection
* Domain reputation analysis
* DNS-based analysis
* SPF/DKIM/DMARC header analysis
* More advanced URL feature extraction
* Better `.eml` header parsing
* Threat-intelligence API integration
* Email-header visualization
* Role-based access control
* Enterprise SIEM integration
* Docker deployment
* Cloud deployment
* Automated security reports
* Improved false-positive analysis

These enhancements should only be implemented in authorized and defensive environments.

---

## 📸 Screenshots


### 🟢 Safe Email Analysis

The system analyzes legitimate sample emails and provides an explainable risk assessment.

![Safe email input](screenshots/safe-email/email-input.png)

![Safe email analysis result](screenshots/safe-email/analysis-result1.png)

![Safe email analysis details](screenshots/safe-email/analysis-result2.ng)

---

### 🔴 Phishing Email Analysis

The system identifies multiple phishing indicators and generates an explainable risk score.

![Phishing email input](screenshots/phishing-email/phishing-input.png)

![Phishing email analysis result](screenshots/phishing-email/analysis-result1.png)

![Phishing email analysis details](screenshots/phishing-email/analysis-result2.png)

---

### 🔗 URL Analysis

The application analyzes suspicious URL characteristics without visiting the URL.

![URL analysis input](screenshots/url-analysis/url-input.png)

![URL analysis result](screenshots/url-analysis/analysis-result1.png)

![URL analysis details](screenshots/url-analysis/analysis-result2.png)

---

### 📎 Email File Upload Analysis

The application supports analysis of safe synthetic `.txt` and `.eml` email samples.

![Uploaded email input](screenshots/file-upload/input.png)

![Uploaded email analysis result](screenshots/file-upload/analysis-result1.png)

![Uploaded email analysis details](screenshots/file-upload/analysis-result2.png)

---

### 📊 Analysis History & Security Analytics

The dashboard stores previous analyses and presents security statistics, graphs, and analysis history.

![Security analytics dashboard](screenshots/analyse/Screenshot (53).png)

---

### 🎓 Phishing Security Awareness

The dashboard provides educational information to help users recognize and respond safely to phishing attempts.

![Security awareness dashboard](screenshots/awareness/screenshot (57).png)


## 🎓 Learning Outcomes

Through this project, I practiced:

* Phishing analysis
* Email-security concepts
* Social-engineering detection
* URL analysis
* Security feature engineering
* Rule-based detection
* Machine-learning classification
* Explainable security decisions
* Risk scoring
* Python development
* Streamlit development
* Data analysis
* Automated testing
* Git/GitHub
* Security awareness
* Defensive cybersecurity practices

---

## 📌 Project Status

```text
Development Status: Completed Educational Prototype
```

Implemented:

* ✅ Email analysis
* ✅ Sender analysis
* ✅ Content analysis
* ✅ URL analysis
* ✅ Rule-based scoring
* ✅ ML classifier
* ✅ Synthetic dataset
* ✅ File upload
* ✅ Analysis history
* ✅ Analytics dashboard
* ✅ Security recommendations
* ✅ Awareness education
* ✅ Automated testing
* ✅ GitHub documentation

---

## 👨‍💻 Author

[Muhammed Shammas]

Cybersecurity Student | Aspiring SOC / Cybersecurity Analyst

This project was developed as a defensive cybersecurity learning project to demonstrate practical skills in phishing detection, email security, security analytics, Python development, machine learning, and security awareness.

---

## ⭐ Disclaimer

This project is intended strictly for **education, defensive security research, and authorized testing**.

All phishing examples and URLs used for demonstration are synthetic or safe documentation examples. The project must not be used to conduct phishing attacks, credential harvesting, unauthorized access, or other malicious activity.
