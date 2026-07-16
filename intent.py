# ==========================
# Deek Intent Engine
# Version: 1.0
# ==========================

import re


class IntentEngine:

    def detect(self, question):

        text = question.lower().strip()

        # --------------------------
        # Memory Save
        # --------------------------

        if text.startswith("remember my") and " is " in text:
            return "MEMORY_SAVE"

        # --------------------------
        # Memory Recall
        # --------------------------

        if text.startswith("what is my"):
            return "MEMORY_RECALL"

        # --------------------------
        # Calculator
        # --------------------------

        if re.fullmatch(r"[0-9+\-*/().% ]+", text):
            return "CALCULATOR"

        # --------------------------
        # Date & Time
        # --------------------------

        if any(word in text for word in [
            "date",
            "time",
            "today"
        ]):
            return "DATE_TIME"

        # --------------------------
        # Default
        # --------------------------

        return "AI_CHAT"
