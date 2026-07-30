from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_DIR = BASE_DIR / "database"

UPLOADS_DIR = BASE_DIR / "uploads"

EXPORTS_DIR = BASE_DIR / "exports"

ASSETS_DIR = BASE_DIR / "assets"

LOGS_DIR = BASE_DIR / "logs"

# Create directories automatically

for directory in (
    DATABASE_DIR,
    UPLOADS_DIR,
    EXPORTS_DIR,
    ASSETS_DIR,
    LOGS_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)

# ==========================================================
# Database
# ==========================================================

DATABASE_NAME = os.getenv("DATABASE_NAME", "animalcare.db")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{DATABASE_DIR / DATABASE_NAME}"
)

# ==========================================================
# Gemini AI
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

GEMINI_MODEL = os.getenv(
    "MODEL",
    "gemini-2.5-flash"
)

# ==========================================================
# Application
# ==========================================================

APP_NAME = "AnimalCare AI"

APP_VERSION = "1.0.0"

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

# ==========================================================
# Image Upload
# ==========================================================

MAX_IMAGE_SIZE_MB = 10

ALLOWED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".webp"
}

# ==========================================================
# AI
# ==========================================================

MAX_IMAGES_PER_ANALYSIS = 4

MAX_AI_OUTPUT_TOKENS = 1024

AI_TEMPERATURE = 0.2