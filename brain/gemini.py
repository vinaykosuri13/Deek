# ==========================
# Deek Brain
# Gemini AI
# Version: 3.0
# ==========================

import time
from google import genai
from config import API_KEY, MODEL_NAME


class DeekBrain:

    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)

    def ask(self, question):

        retries = 3

        for attempt in range(retries):

            try:

                response = self.client.models.generate_content(
                    model=MODEL_NAME,
                    contents=question
                )

                return response.text.strip()

            except Exception as e:

                error = str(e)

                if "503" in error:

                    if attempt < retries - 1:
                        time.sleep(2)
                        continue

                    return (
                        "Boss, Gemini is busy right now.\n"
                        "Please try again in a few moments."
                    )

                elif "429" in error or "RESOURCE_EXHAUSTED" in error:

                    return (
                        "Boss, I've reached my current AI usage limit.\n\n"
                        "Please try again later or use another Gemini API key."
                    )

                elif "404" in error:

                    return (
                        "Boss, the configured AI model is unavailable."
                    )

                elif "401" in error or "403" in error:

                    return (
                        "Boss, there is a problem with
