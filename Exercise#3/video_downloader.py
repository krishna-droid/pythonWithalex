"""Download videos using yt-dlp."""

import logging
import os
import tempfile

import yt_dlp


def download_video(url):
    """Download a video and return the path to the temporary file."""
    logging.info(f"Downloading: {url}")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_path = temp_file.name
    temp_file.close()

    ydl_opts = {
        "outtmpl": temp_path,
        "quiet": True,
        "format": "best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    size_mb = os.path.getsize(temp_path) / (1024 * 1024)
    logging.info(f"Downloaded to: {temp_path} (Size: {size_mb:.1f} MB)")

    return temp_path
