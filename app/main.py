import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.models import AnalysisResult
from app.parsers import parse_uploaded_file
from app.analyzers.sender import analyze_sender
from app.analyzers.content import analyze_content
from app.analyzers.url import analyze_urls
from app.analyzers.scoring import calculate_score, classify, recommendations
from app.services.ml_model import predict
from app.db import init_db, save_analysis, load_history, clear_history

st.set_page_config(page_title="Phishing Email Detection & Awareness Dashboard",
                   page_icon="🛡️", layout="wide")
init_db()

st.title("🛡️ Phishing Email Detection & Awareness Dashboard")
st.caption("Defensive educational analyzer — synthetic/sample emails only. URLs are analyzed without being visited.")

with st.sidebar:
    st.header("Project Controls")
    page = st.radio("Navigate", ["Analyzer", "History & Analytics", "Awareness"])
    st.divider()
    st.info("Never enter real passwords, OTPs, API keys, or confidential email content.")

if page == "Analyzer":
    st.subheader("1. Provide a safe sample email")
    uploaded = st.file_uploader("Optional .txt or .eml file", type=["txt","eml"])
    default_sender, default_subject, default_body = "", "", ""
    attachments = []

    if uploaded:
        try:
            parsed = parse_uploaded_file(uploaded.name, uploaded.getvalue())
            default_sender, default_subject, default_body = parsed["sender"], parsed["subject"], parsed["body"]
            attachments = parsed["attachments"]
            st.success(f"Loaded {uploaded.name}")
            if attachments:
                st.warning("Attachment names found: " + ", ".join(attachments))
        except Exception as exc:
            st.error(str(exc))

    sender = st.text_input("Sender", value=default_sender,
                           placeholder="Security Team <security@example.com>")
    subject = st.text_input("Subject", value=default_subject,
                            placeholder="Example: Monthly account notice")
    body = st.text_area("Email body", value=default_body, height=260,
                        placeholder="Paste a synthetic/sample email here...")
    analyze = st.button("🔍 Analyze Email", type="primary", use_container_width=True)

    if analyze:
        if not (sender or subject or body):
            st.warning("Enter at least some sample email information.")
        else:
            sender_data, sender_findings = analyze_sender(sender, subject, body)
            content_features, content_findings = analyze_content(subject, body, attachments)
            urls, url_findings = analyze_urls(body)
            findings = sender_findings + content_findings + url_findings
            score = calculate_score(findings)
            label = classify(score)
            recs = recommendations(findings, label)
            ml_prob, ml_label = predict(f"{subject}\n{body}")
            result = AnalysisResult(
                score=score, classification=label, findings=findings,
                recommendations=recs, urls=urls, sender=sender_data,
                content_features=content_features, ml_probability=ml_prob,
                ml_label=("PHISHING" if ml_label == 1 else "LEGITIMATE") if ml_label is not None else None
            )
            st.session_state["last_result"] = result
            save_analysis(result, sender, subject)

    result = st.session_state.get("last_result")
    if result:
        st.divider()
        st.subheader("2. Analysis Result")
        c1, c2, c3 = st.columns(3)
        c1.metric("Risk Score", f"{result.score}/100")
        c2.metric("Classification", result.classification)
        c3.metric("Findings", len(result.findings))

        if result.score >= 70:
            st.error("High-risk indicators detected. Treat this sample as likely phishing.")
        elif result.score >= 40:
            st.warning("Several suspicious indicators were detected.")
        elif result.score >= 20:
            st.info("Some indicators deserve verification.")
        else:
            st.success("No strong phishing indicators were detected by the rules.")

        st.subheader("Why?")
        if result.findings:
            for f in sorted(result.findings, key=lambda x: x.points, reverse=True):
                st.markdown(f"**{f.severity} — {f.title}** (+{f.points})")
                st.write(f.explanation)
                if f.evidence:
                    st.code(f.evidence, language="text")
        else:
            st.write("No rule-based findings.")

        st.subheader("Security Recommendations")
        for rec in result.recommendations:
            st.write("• " + rec)

        if result.urls:
            st.subheader("URL Analysis")
            st.dataframe(pd.DataFrame(result.urls), use_container_width=True)
            st.caption("The application does not visit these URLs.")

        if result.ml_probability is not None:
            st.subheader("Optional ML Signal")
            st.write(f"Model phishing probability: **{result.ml_probability:.1%}**")
            st.write(f"Model label: **{result.ml_label}**")

elif page == "History & Analytics":
    st.subheader("Analysis History")
    history = load_history()
    if not history:
        st.info("No analyses stored yet.")
    else:
        df = pd.DataFrame(history)
        a, b, c = st.columns(3)
        a.metric("Total analyses", len(df))
        b.metric("High-risk", int((df["classification"] == "HIGH RISK / LIKELY PHISHING").sum()))
        c.metric("Average score", f"{df['score'].mean():.1f}")
        st.plotly_chart(px.histogram(df, x="classification", title="Classification Distribution"),
                        use_container_width=True)
        st.plotly_chart(px.line(df.sort_values("id"), x="id", y="score",
                                 title="Risk Score Over Analyses"), use_container_width=True)
        st.dataframe(df, use_container_width=True)
        if st.button("Delete local analysis history"):
            clear_history()
            st.success("Local history cleared. Refresh the page.")

elif page == "Awareness":
    st.subheader("🎓 Phishing Awareness")
    st.markdown("""
### What is phishing?
Phishing is a social-engineering technique where an attacker attempts to trick a person
into revealing information, transferring money, opening a malicious file, or taking another unsafe action.

### Warning signs
- Unexpected urgency or threats
- Requests for passwords, OTPs, or payment
- Sender/display-name mismatch
- Suspicious or misleading URLs
- Unexpected attachments
- Requests to bypass normal procedures
- Poorly matched context or unusual communication

### Safe verification workflow
1. Pause — do not act immediately.
2. Inspect the sender address.
3. Check the destination without opening it.
4. Verify using a trusted channel you already know.
5. Report suspicious messages according to your organization's process.
6. Never share passwords or OTPs by email.

### Important
A detector can make mistakes. A low score does not prove that an email is safe.
Human verification and organizational controls remain important.
""")
