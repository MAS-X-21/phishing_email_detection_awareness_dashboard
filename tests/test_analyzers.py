from app.analyzers.url import analyze_url
from app.analyzers.sender import analyze_sender
from app.analyzers.content import analyze_content
from app.analyzers.scoring import calculate_score, classify

def test_ip_url_is_flagged():
    features, findings = analyze_url("http://192.0.2.10/verify")
    assert features["has_ip_host"]
    assert any("IP-address" in f.title for f in findings)

def test_credential_language_is_flagged():
    features, findings = analyze_content(
        "URGENT verify your account",
        "Provide your password and OTP immediately.", []
    )
    assert features["credential_matches"]
    assert any(f.title == "Credential-related request" for f in findings)

def test_display_name_mismatch():
    data, findings = analyze_sender(
        "Security Team <security@gmail.com>", "Account notice", "Please review this."
    )
    assert data["display_name_mismatch_signal"]
    assert findings

def test_score_classification():
    assert calculate_score([]) == 0
    assert classify(0) == "SAFE"
    assert classify(39) == "LOW RISK"
    assert classify(69) == "SUSPICIOUS"
    assert classify(70) == "HIGH RISK / LIKELY PHISHING"
