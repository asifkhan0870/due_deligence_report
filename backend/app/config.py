import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# API Key from environment
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Existing config (unchanged)
BASE_OUTPUT_DIR = "outputs"

# Optional safety (recommended)
if not ANTHROPIC_API_KEY:
    raise ValueError("❌ CLAUDE_API_KEY not found in .env file")