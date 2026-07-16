# ==========================
# Deek Brain
# Gemini AI
# Version: 2.0
# ==========================

from google import genai
from config import API_KEY, MODEL_NAME


class DeekBrain:
    """
    Deek AI Brain
    """

    def __init__(self):

        self.client = genai.Client(api_key=API_KEY)

    def ask(self, question):

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=question
            )

            return response.text.strip()

        except Exception as e:

            error = str(e)

            if "503" in error:
                return (
                    "Sorry Boss! Gemini is currently experiencing high demand.\n"
                    "Please try again in a few moments."
                )

            elif "404" in error:
                return (
                    "Sorry Boss! The configured AI model is unavailable."
                )

            elif "401" in error or "403" in error:
                return (
                    "Sorry Boss! There is a problem with the Gemini API key."
                )

            elif "timeout" in error.lower():
                return (
                    "Sorry Boss! The request timed out. Please try again."
                )

            elif "connection" in error.lower():
                return (
                    "Sorry Boss! I couldn't connect to the internet."
                )

            else:
                return (
                    f"Unexpected Error:\n{error}"
                )
