import re
from email.utils import parseaddr
from app.models import Finding

FREE_PROVIDERS = {"gmail.com","outlook.com","hotmail.com","yahoo.com","proton.me"}

def analyze_sender(sender: str, subject: str = "", body: str = ""):
    display, address = parseaddr(sender or "")
    domain = address.split("@",1)[1].lower() if "@" in address else ""
    findings = []
    data = {
        "display_name": display, "email": address, "domain": domain,
        "has_valid_email_shape": bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", address)),
        "free_provider": domain in FREE_PROVIDERS,
        "display_name_mismatch_signal": False,
    }
    lower_display = display.lower()
    trusted_words = ["bank","support","security","administrator","microsoft","google","apple","hr"]
    if any(w in lower_display for w in trusted_words) and domain in FREE_PROVIDERS:
        data["display_name_mismatch_signal"] = True
        findings.append(Finding("SENDER","HIGH",15,
            "Trusted-looking display name with free-mail domain",
            "The display name resembles an organization or security role while the address uses a free-mail provider.",
            sender))
    if not data["has_valid_email_shape"]:
        findings.append(Finding("SENDER","MEDIUM",8,"Unusual sender address",
            "The sender value does not look like a normal email address.",sender or "(empty)"))
    if "support" in address.lower() and domain in FREE_PROVIDERS:
        findings.append(Finding("SENDER","MEDIUM",8,"Support-themed free-mail sender",
            "A support-like mailbox on a free-mail domain deserves extra verification.",address))
    return data, findings
