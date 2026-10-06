import re
from urllib.parse import urlparse
from app.models import Finding

URL_RE = re.compile(r"https?://[^\s<>'\"]+", re.I)
SHORTENERS = {"bit.ly", "tinyurl.com", "t.co", "goo.gl", "is.gd", "ow.ly"}
SUSPICIOUS_TLDS = {".zip", ".mov", ".click", ".top", ".xyz", ".work", ".support"}

def extract_urls(text: str) -> list[str]:
    return [u.rstrip(".,);]") for u in URL_RE.findall(text or "")]

def analyze_url(url: str) -> tuple[dict, list[Finding]]:
    findings = []
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower()
    features = {
        "url": url, "scheme": parsed.scheme, "host": host,
        "port": parsed.port, "path_length": len(parsed.path),
        "query_length": len(parsed.query),
        "subdomain_count": max(0, host.count(".")),
        "has_ip_host": bool(re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host)),
        "has_at_symbol": "@" in url, "has_punycode": "xn--" in host,
        "is_shortener": host in SHORTENERS,
        "suspicious_tld": any(host.endswith(tld) for tld in SUSPICIOUS_TLDS),
        "https": parsed.scheme.lower() == "https",
    }
    if features["has_ip_host"]:
        findings.append(Finding("URL","HIGH",20,"IP-address URL",
            "The link uses an IP address instead of a normal domain name.",url))
    if features["has_at_symbol"]:
        findings.append(Finding("URL","HIGH",15,"Misleading @ symbol",
            "An @ character can make a URL visually misleading because the hostname is after it.",url))
    if features["has_punycode"]:
        findings.append(Finding("URL","HIGH",15,"Punycode domain",
            "The hostname contains xn-- encoding, which can be associated with look-alike domains.",host))
    if features["is_shortener"]:
        findings.append(Finding("URL","MEDIUM",8,"URL shortener",
            "A shortened URL hides the final destination from a reader.",host))
    if features["suspicious_tld"]:
        findings.append(Finding("URL","MEDIUM",7,"Unusual URL ending",
            "The domain uses a TLD commonly seen in some low-trust or disposable campaigns.",host))
    if features["subdomain_count"] >= 4:
        findings.append(Finding("URL","MEDIUM",7,"Deep subdomain structure",
            "The hostname contains many subdomain levels, which can make a domain harder to inspect.",host))
    if len(url) > 120:
        findings.append(Finding("URL","LOW",4,"Very long URL",
            "The link is unusually long and may hide tracking or deceptive parameters.",url[:140]))
    if parsed.port and parsed.port not in {80,443}:
        findings.append(Finding("URL","MEDIUM",6,"Non-standard port",
            "The URL explicitly specifies a non-standard web port.",str(parsed.port)))
    return features, findings

def analyze_urls(text: str) -> tuple[list[dict], list[Finding]]:
    all_features, all_findings = [], []
    for url in extract_urls(text):
        features, findings = analyze_url(url)
        all_features.append(features)
        all_findings.extend(findings)
    return all_features, all_findings
