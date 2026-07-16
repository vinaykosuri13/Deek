# ==========================
# Calculator Tool
# Version: 1.0
# ==========================


class CalculatorTool:

    def execute(self, expression):

        try:

            return str(eval(expression))

        except Exception:

            return "Sorry Boss, I couldn't calculate that."
