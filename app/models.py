from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Finding:
    category: str
    severity: str
    points: int
    title: str
    explanation: str
    evidence: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class AnalysisResult:
    score: int
    classification: str
    findings: list[Finding]
    recommendations: list[str]
    urls: list[dict[str, Any]]
    sender: dict[str, Any]
    content_features: dict[str, Any]
    ml_probability: float | None = None
    ml_label: str | None = None

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["findings"] = [f.to_dict() for f in self.findings]
        return data
