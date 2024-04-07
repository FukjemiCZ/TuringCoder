import os

# Základní cesty jako výchozí relativní
RUN_DIR = os.getcwd()
APP_DIR=os.path.join(RUN_DIR, "DemoApp")
TEMPLATE_DIR = os.path.join(RUN_DIR, "Templates")
OUTPUT_DIR = os.path.join(RUN_DIR, "Request")
RESPONSE_DIR = os.path.join(RUN_DIR, "Response")

# API Tokens
OPENAI_API_KEY=""
OPENAI_MODEL="gpt-4-turbo-preview"
OPENAI_TEMPERATURE="0.7"
OPENAI_MAX_TOKENS="2048"
