"""
🕒 Time Utilities
Provides consistent timestamping for metadata fields.
"""

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d")
