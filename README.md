# Phishing Email Detection & Awareness Dashboard

A defensive, educational cybersecurity project that analyzes synthetic/sample emails for phishing indicators.

## Features
- Paste email content or upload safe `.txt` / `.eml` samples
- Sender, subject, body and URL analysis
- Rule-based phishing risk scoring
- Explainable findings and recommendations
- Safe URL feature analysis without visiting URLs
- Optional machine-learning classifier trained on synthetic data
- SQLite analysis history
- Dashboard analytics
- Phishing-awareness education
- Automated tests
- No credential collection, phishing-page generation, or real-user targeting

## Architecture
```text
User -> Streamlit UI -> Email Parser
                       -> Sender Analyzer
                       -> Content Analyzer
                       -> URL Analyzer
                       -> Rule-Based Risk Engine
                       -> Optional ML Signal
                       -> SQLite History -> Analytics
```

## Safety
Use only synthetic/sample emails. Never enter real passwords, API keys, OTPs, tokens, or confidential content.
The URL analyzer extracts and parses URL characteristics; it does not browse to them. Demo URLs use reserved
or fictional examples such as `example.com`, `example.org`, `example.net`, and documentation IP ranges.

## Installation
Windows:
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/train_model.py
streamlit run app/main.py
```

Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/train_model.py
streamlit run app/main.py
```

## Risk model
| Score | Classification |
|---:|---|
| 0-19 | SAFE |
| 20-39 | LOW RISK |
| 40-69 | SUSPICIOUS |
| 70-100 | HIGH RISK / LIKELY PHISHING |

This is an educational scoring model, not a production email gateway.

## Testing
```bash
pytest -q
```

## GitHub strategy
Suggested repository name: `phishing-email-detection-awareness-dashboard`

Suggested commits:
1. `chore: initialize project`
2. `feat: add synthetic dataset`
3. `feat: add email parser`
4. `feat: add sender and content analyzers`
5. `feat: add safe URL analyzer`
6. `feat: add explainable risk scoring`
7. `feat: add SQLite analysis history`
8. `feat: add optional ML classifier`
9. `feat: add Streamlit dashboard`
10. `test: add detection test suite`
11. `docs: add project report and interview guide`

## Limitations
This is not a replacement for secure email gateways, sandboxing, DMARC/SPF/DKIM verification, attachment detonation,
threat-intelligence feeds, or enterprise SIEM/SOAR systems.

## Future work
- Authorized SPF/DKIM/DMARC header analysis
- Threat-intelligence integration
- Better multilingual NLP
- Model monitoring and drift analysis
- SIEM/SOAR export in a controlled lab
- Role-based access control
