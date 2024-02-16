"""
Transform step for survey comments.

What it does:
- Redacts PII (emails, phone numbers) from comment_raw → comment_clean
- Normalizes whitespace
- Ensures required columns exist (defensive)
"""
# Clean up process for survey comments

import re
import pandas as pd

# Regexes for basic PII redaction
EMAIL = re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b") #
PHONE = re.compile(
    r"(?:\+?\d{1,3})?[\s\-\.]?(?:\(\d{3}\)|\d{3})[\s\-\.]?\d{3}[\s\-\.]?\d{4}"
)

def _normalize_ws(text: str) -> str:
    """Collapse multiple spaces and strip ends."""
    return re.sub(r"\s+", " ", text).strip()

def redact(text: str) -> str:
    """
    Remove PII from a single string:
    - Emails → [REDACTED_EMAIL]
    - Phone numbers → [REDACTED_PHONE]
    """
    if not isinstance(text, str):
        return ""
    text = EMAIL.sub("[REDACTED_EMAIL]", text)
    text = PHONE.sub("[REDACTED_PHONE]", text)
    return _normalize_ws(text)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes a DataFrame with at least:
        survey_id, submitted_at, product_line, region, rating, comment_raw
    Returns a copy with a new column:
        comment_clean
    """
    df = df.copy()

    # This makes sure the required columns exist (defensive; won’t crash if missing)
    required = ["survey_id", "submitted_at", "product_line", "region", "rating", "comment_raw"]
    for col in required:
        if col not in df.columns:
            df[col] = None

    # Create cleaned comment
    df["comment_clean"] = df["comment_raw"].fillna("").map(redact)

    # Optional: basic type normalization (keeps SQLite happy)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").fillna(0).astype(int)
    df["survey_id"] = df["survey_id"].astype(str)

    return df
