"""Exercise 3: prepare the Whisper video transcription program."""

import logging
import os

from dotenv import load_dotenv
from video_downloader import download_video
from whisper_transcriber import transcribe_audio


def main():
    """Load the Whisper settings before starting the program."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    load_dotenv()

    api_key = os.getenv("WHISPER_API_KEY")
    base_url = os.getenv("WHISPER_BASE_URL")
    model = os.getenv("WHISPER_MODEL", "whisper-1")

    if not api_key:
        logging.error("WHISPER_API_KEY is not set. Check your .env file.")
        return

    if not base_url:
        logging.error("WHISPER_BASE_URL is not set. Check your .env file.")
        return

    logging.info(f"Whisper model ready: {model}")


if __name__ == "__main__":
    main()
