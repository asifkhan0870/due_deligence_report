import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API Key from environment
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

# Existing config (unchanged)
BASE_OUTPUT_DIR = "outputs"

# Optional safety (recommended)
if not CLAUDE_API_KEY:
    raise ValueError("❌ CLAUDE_API_KEY not found in .env file")