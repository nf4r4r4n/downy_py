# Downy

A modern and interactive CLI video/audio downloader built with Python using:

- `yt-dlp`
- `ffmpeg`
- `questionary`
- `rich`

The project provides a clean terminal experience for downloading and converting media from supported platforms such as YouTube.

---

## Features

- Interactive terminal UI
- Audio and video download support
- Audio extraction and conversion
- Multiple output formats
- Live progress bar with download speed and ETA
- Modular and maintainable architecture
- ffmpeg-powered post-processing

---

## Supported Media Types

### Audio Formats

- aac
- flac
- mp3
- m4a
- opus
- vorbis
- wav

### Video Formats

- mp4
- mkv

---

## Project Structure

```text
downy_py/
│
├── core/
│   ├── downloader.py
│
├── ui/
│   ├── prompts.py
│   └── display.py
│
└── main.py
