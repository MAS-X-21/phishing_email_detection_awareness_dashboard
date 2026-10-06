from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import Any
import re

def parse_eml_bytes(raw: bytes) -> dict[str, Any]:
    msg = BytesParser(policy=policy.default).parsebytes(raw)
    sender = msg.get("From", "")
    subject = msg.get("Subject", "")
    text_parts, html_parts, attachments = [], [], []

    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition = part.get_content_disposition()
            if disposition == "attachment":
                attachments.append(part.get_filename() or "unnamed")
                continue
            if content_type == "text/plain":
                try: text_parts.append(part.get_content())
                except Exception: pass
            elif content_type == "text/html":
                try: html_parts.append(part.get_content())
                except Exception: pass
    else:
        try: content = msg.get_content()
        except Exception: content = ""
        if msg.get_content_type() == "text/html":
            html_parts.append(content)
        else:
            text_parts.append(content)

    body = "\n".join(text_parts)
    if not body and html_parts:
        body = re.sub(r"<[^>]+>", " ", "\n".join(html_parts))
    return {"sender": sender, "subject": subject, "body": body,
            "attachments": attachments, "headers": dict(msg.items())}

def parse_txt_bytes(raw: bytes) -> dict[str, Any]:
    text = raw.decode("utf-8", errors="replace")
    return {"sender": "", "subject": "", "body": text,
            "attachments": [], "headers": {}}

def parse_uploaded_file(name: str, raw: bytes) -> dict[str, Any]:
    suffix = Path(name).suffix.lower()
    if suffix == ".eml": return parse_eml_bytes(raw)
    if suffix == ".txt": return parse_txt_bytes(raw)
    raise ValueError("Only .txt and .eml files are supported.")
