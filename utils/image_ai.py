import os

from dotenv import load_dotenv
from PIL import Image
from google import genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("MODEL", "gemini-3.5-flash")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=API_KEY)


# ==========================================
# Analyze Pet Image
# ==========================================

def analyze_pet_image(image_file) -> str:

    image = Image.open(image_file)

    prompt = """
You are AnimalCare AI.

Analyze the uploaded pet image.

Describe ONLY what is visibly observable.

Include:

- Animal type
- General appearance
- Eyes
- Nose
- Ears
- Fur or feathers
- Body posture
- Visible wounds or swelling
- Signs of distress (if visible)

IMPORTANT:

- Do NOT diagnose diseases.
- Do NOT guess things that cannot be seen.
- Keep the report under 120 words.
- Respond in plain English only.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=[
            prompt,
            image,
        ],
    )

    if response.text:
        return response.text.strip()

    return "No visual observations could be generated."