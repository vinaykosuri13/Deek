# ==========================
# Deek Tool Engine
# Version: 1.0
# ==========================

from .calculator import CalculatorTool
from .datetime_tool import DateTimeTool


class ToolEngine:

    def __init__(self):

        self.calculator = CalculatorTool()
        self.datetime = DateTimeTool()

    def execute(self, intent, question):

        # --------------------------
        # Calculator
        # --------------------------

        if intent == "CALCULATOR":

            return self.calculator.execute(question)

        # --------------------------
        # Date & Time
        # --------------------------

        if intent == "DATE_TIME":

            return self.datetime.execute()

        # --------------------------
        # Tool Not Found
        # --------------------------

        return None
