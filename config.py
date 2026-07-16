# ==========================
# Deek Configuration
# Version: 1.0
# ==========================

import os


APP_NAME = "Deek"
APP_VERSION = "1.0"

# Gemini model
MODEL_NAME = "gemini-flash-latest"

# Read API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please create the API setup cell first."
    )
