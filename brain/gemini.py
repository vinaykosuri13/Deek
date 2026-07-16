# ==========================
# Deek Brain
# Gemini AI
# Version: 3.0
# ==========================

import time

from google import genai
from config import API_KEY, MODEL_NAME


class DeekBrain:
    """
    Deek AI Brain
    """

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

                # Retry on temporary server overload
                if "503" in error:

                    if attempt < retries - 1:
                        time.sleep(2)
                        continue

                    return (
                        "Sorry Boss! Gemini is currently experiencing high demand.\n"
                        "Please try again in a few moments."
                    )

                # Quota exceeded
                elif "429" in error or "RESOURCE_EXHAUSTED" in error:

                    return (
                        "Boss, I've reached my current AI usage limit.\n\n"
                        "Please try again later or use another Gemini API key."
                    )

                # Model not found
                elif "404" in error:

                    return (
                        "Sorry Boss! The configured AI model is unavailable."
                    )

                # Invalid API key
                elif "401" in error or "403" in error:

                    return (
                        "Sorry Boss! There is a problem with the Gemini API key."
                    )

                # Timeout
                elif "timeout" in error.lower():

                    return (
                        "Sorry Boss! The AI service took too long to respond."
                    )

                # Internet problem
                elif (
                    "connection" in error.lower()
                    or "network" in error.lower()
                ):

                    return (
                        "Sorry Boss! I couldn't connect to the AI service.\n"
                        "Please check your internet connection."
                    )

                # Any other error
                else:

                    return (
                        "Unexpected Error:\n\n"
                        f"{error}"
                    )

        return (
            "Sorry Boss! Something went wrong."
        )
