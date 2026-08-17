import argparse
import logging
import os
import tempfile
import traceback

import yt_dlp


def download_video(url):
    """Download a video from a URL into a temporary file using yt-dlp."""
    logging.info(f"Downloading: {url}")

    # Create a temporary file with a .mp4 extension
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_path = temp_file.name
    temp_file.close()

    # Configure yt-dlp options
    ydl_opts = {
        "outtmpl": temp_path,
        "quiet": True,
        "format": "best",
    }

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Print the path and size
    size_mb = os.path.getsize(temp_path) / (1024 * 1024)
    logging.info(f"Saved to: {temp_path} (Size: {size_mb:.1f} MB)")

    # Clean up the temporary file
    os.remove(temp_path)
    logging.info("Temporary file cleaned up.")


if __name__ == "__main__":
    # Configure the logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    parser = argparse.ArgumentParser(
        description="Download a video from a video hoster using yt-dlp."
    )

    parser.add_argument("--url", required=True, help="The video URL to download")

    args = parser.parse_args()

    try:
        download_video(args.url)
    except Exception as error:
        logging.error(f"An error occurred: {error}")
        logging.error("Traceback:")
        logging.error(traceback.format_exc())
    finally:
        logging.info("Done.")
