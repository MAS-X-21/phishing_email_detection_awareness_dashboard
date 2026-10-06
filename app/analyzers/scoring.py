from app.models import Finding

def classify(score):
    if score < 20: return "SAFE"
    if score < 40: return "LOW RISK"
    if score < 70: return "SUSPICIOUS"
    return "HIGH RISK / LIKELY PHISHING"

def calculate_score(findings):
    best = {}
    for f in findings:
        best[f.title] = max(best.get(f.title, 0), f.points)
    return min(100, sum(best.values()))

def recommendations(findings, classification):
    recs = []
    categories = {f.category for f in findings}
    if "URL" in categories:
        recs.append("Do not open suspicious links; verify the destination through a trusted channel.")
    if "SENDER" in categories:
        recs.append("Verify the sender address independently rather than trusting the display name.")
    if "CONTENT" in categories:
        recs.append("Treat urgent requests for credentials, payment, or account changes as high-risk until verified.")
    if any(f.category == "CONTENT" and "Attachment" in f.title for f in findings):
        recs.append("Do not open unexpected attachments; confirm the sender and context first.")
    if classification in {"SUSPICIOUS","HIGH RISK / LIKELY PHISHING"}:
        recs.append("Report the message through your organization's approved phishing-reporting process.")
    if not recs:
        recs.append("No strong phishing indicators were detected by this educational analyzer.")
    recs.append("Remember: a low score is not proof that an email is safe.")
    return list(dict.fromkeys(recs))
