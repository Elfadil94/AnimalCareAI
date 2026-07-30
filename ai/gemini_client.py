from __future__ import annotations

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiClient:
    """
    Wrapper around Google's GenAI SDK.
    """

    _client = None

    @classmethod
    def client(cls) -> genai.Client:
        """
        Return a singleton Gemini client.
        """

        if cls._client is None:

            api_key = os.getenv("GEMINI_API_KEY")

            if not api_key:
                raise ValueError(
                    "GEMINI_API_KEY was not found in the .env file."
                )

            cls._client = genai.Client(
                api_key=api_key,
            )

        return cls._client

    @classmethod
    def model(cls) -> str:
        """
        Return the Gemini model name.

        If GEMINI_MODEL exists in the .env file it will be used,
        otherwise gemini-2.5-flash will be used.
        """

        return os.getenv(
            "GEMINI_MODEL",
            "gemini-2.5-flash",
        )

    @classmethod
    def test_connection(cls) -> str:
        """
        Simple connection test.
        """

        response = cls.client().models.generate_content(
            model=cls.model(),
            contents="Reply with only the word: OK",
        )

        return response.text.strip()