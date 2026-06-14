# test.py
import re
from typing import Optional

def double_price_from_string(text: str) -> Optional[float]:
    """מכפיל את המחיר שמופיע בתוך string ב-2"""
    match = re.search(r"\d+(\.\d+)?", text)
    if match:
        price = float(match.group())
        return price * 2
    return None