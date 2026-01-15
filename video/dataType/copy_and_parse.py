#! python3
"""
剪贴板复制粘贴
"""

import pyperclip
import sys

TEXT = {
    "agree": """Yes, I agree. That sounds fine to me.""",
    "busy": """Sorry, can we do this later this week or next week?""",
    "upsell": """Would you consider making this a monthly donation?""",
}

if len(sys.argv) < 2:
    print("Usage: python copy_and_parse.py [keyphrase] - copy phrase text")
    sys.exit()

# 获取命令行参数
key_parse = sys.argv[1]


if key_parse in TEXT:
    pyperclip.copy(TEXT[key_parse])
    print("Text for " + key_parse + " copied to clipboard.")
else:
    print("There is no text for " + key_parse)
