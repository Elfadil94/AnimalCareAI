import os
import json

from dotenv import load_dotenv
from google import genai
from google.genai import types

from utils.prompts import SYSTEM_PROMPT

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
# Analyze Pet Symptoms
# ==========================================

def analyze_pet(pet: str, age: float, symptoms: str) -> dict:

    prompt = f"""
{SYSTEM_PROMPT}

Pet Type: {pet}
Age: {age}

Symptoms:
{symptoms}

Return ONLY a valid JSON object.

Example:

{{
  "possible_causes": [
    "Cause 1",
    "Cause 2",
    "Cause 3"
  ],
  "risk_level": "Low",
  "recommendations": [
    "Recommendation 1",
    "Recommendation 2",
    "Recommendation 3"
  ],
  "visit_vet": "Visit a veterinarian if symptoms continue or worsen.",
  "emergency": false,
  "disclaimer": "This information is educational only and does not replace a licensed veterinarian."
}}

IMPORTANT:
- Return ONLY JSON.
- No markdown.
- No ```json.
- No explanations.
"""

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0,
                max_output_tokens=1024,
            ),
        )

        text = response.text.strip()

        print("=" * 60)
        print("RAW RESPONSE")
        print("=" * 60)
        print(text)
        print("=" * 60)

        # إزالة markdown إن وجد
        text = text.replace("```json", "")
        text = text.replace("```", "").strip()

        # استخراج JSON إذا أضاف النموذج نصًا إضافيًا
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            text = text[start:end + 1]

        return json.loads(text)

    except json.JSONDecodeError:
        raise Exception(
            f"Gemini returned invalid JSON:\n\n{text}"
        )

    except Exception as e:
        raise Exception(
            f"AI Analysis Failed:\n\n{e}"
        )