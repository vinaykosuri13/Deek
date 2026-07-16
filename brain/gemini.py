# ==========================
# Deek Brain
# Gemini AI
# ==========================

from google import genai

from config import API_KEY, MODEL_NAME


class DeekBrain:
    """
    Deek AI Brain
    Handles communication with Gemini.
    """

    def __init__(self):

        self.client = genai.Client(
            api_key=API_KEY
        )

    def ask(self, question):

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=question
            )

            return response.text.strip()

        except Exception as e:

            return f"Error: {e}"
