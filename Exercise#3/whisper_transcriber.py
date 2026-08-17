"""Transcribe audio files with Whisper."""

import logging

from openai import OpenAI


def transcribe_audio(audio_path, api_key, base_url, model="whisper-1"):
    """Send an audio file to Whisper and return the transcript."""
    logging.info(f"Transcribing: {audio_path}")
    logging.info(f"Using model: {model}")

    client = OpenAI(api_key=api_key, base_url=base_url)

    with open(audio_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model=model,
            file=audio_file,
        )

    transcript = response.text
    logging.info(f"Transcription complete ({len(transcript)} characters)")

    return transcript
