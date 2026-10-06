import re
from app.models import Finding

URGENCY = ["urgent","immediately","act now","within 24 hours","final warning",
           "last chance","account will be closed","verify now","action required"]
CREDENTIALS = ["password","login","sign in","verify your account","username",
               "one-time password","otp","security code","credential"]
FINANCIAL = ["bank account","credit card","debit card","payment","invoice",
             "refund","gift card","wire transfer","crypto","cryptocurrency"]
THREATS = ["suspended","terminated","legal action","penalty","blocked",
           "lock your account","police"]

def _matches(text, phrases):
    low = text.lower()
    return [p for p in phrases if p in low]

def analyze_content(subject, body, attachments=None):
    text = f"{subject}\n{body}"
    attachments = attachments or []
    urgency = _matches(text, URGENCY)
    creds = _matches(text, CREDENTIALS)
    financial = _matches(text, FINANCIAL)
    threats = _matches(text, THREATS)
    features = {
        "word_count": len(re.findall(r"\b\w+\b", text)),
        "urgency_matches": urgency, "credential_matches": creds,
        "financial_matches": financial, "threat_matches": threats,
        "attachment_count": len(attachments), "has_attachment": bool(attachments),
        "exclamation_count": text.count("!"),
        "all_caps_words": len(re.findall(r"\b[A-Z]{4,}\b", text)),
    }
    findings = []
    if urgency:
        findings.append(Finding("CONTENT","HIGH",15,"Urgency/manipulation language",
            "The message uses time pressure or immediate-action language that can reduce careful verification.",
            ", ".join(urgency[:6])))
    if creds:
        findings.append(Finding("CONTENT","HIGH",20,"Credential-related request",
            "The message references passwords, login details, verification, OTPs, or similar authentication information.",
            ", ".join(creds[:6])))
    if financial:
        findings.append(Finding("CONTENT","MEDIUM",12,"Financial request/theme",
            "The message references payments, cards, transfers, refunds, or other financial actions.",
            ", ".join(financial[:6])))
    if threats:
        findings.append(Finding("CONTENT","MEDIUM",10,"Threat or consequence language",
            "The message uses threats, penalties, suspension, or account-lock language.",
            ", ".join(threats[:6])))
    if attachments:
        findings.append(Finding("CONTENT","LOW",4,"Attachment present",
            "Attachments should be verified before opening, especially when unexpected.",
            ", ".join(attachments[:5])))
    if features["all_caps_words"] >= 3:
        findings.append(Finding("CONTENT","LOW",3,"Excessive capitalized words",
            "Multiple all-caps words can be a social-engineering pressure signal.",
            str(features["all_caps_words"])))
    return features, findings
