# <h1 align="center">Gemini Pro Telegram Bot 🌌</h1>

<p align="center">
  <em>Gemini Pro: An AI-powered Telegram bot script for generating text and image-based responses using Gemini AI</em>
</p>
<hr>

## 🌟 Features

- 🍪 **Text Prompt Response**: Accepts text prompts and generates text.
- 🖼️ **Image Recognition**: Can read and interpret images.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.9 or higher.
- `pyrofork`, `google-generativeai`, and `pillow` libraries.
- A Telegram bot token (you can get one from [@BotFather](https://t.me/BotFather) on Telegram).
- API ID and Hash: You can get these by creating an application on [my.telegram.org](https://my.telegram.org).
- To Get `GOOGLE_API_KEY` Open [GOOGLE_API_KEY](https://makersuite.google.com/app/apikey).

## Installation

To install `pyrofork`, `google-generativeai`, and `pillow`, run the following command:

```bash
pip install pyrofork google-generativeai pillow
```

Alternatively, you can install the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**Note: If you previously installed `pyrogram`, uninstall it before installing `pyrofork`.**

## Configuration

1. Open the `config.py` file in your favorite text editor.
2. Replace the placeholders for `API_ID`, `API_HASH`, `GOOGLE_API_KEY`, and `BOT_TOKEN` with your actual values:
   - **`API_ID`**: Your API ID from [my.telegram.org](https://my.telegram.org).
   - **`API_HASH`**: Your API Hash from [my.telegram.org](https://my.telegram.org).
   - **`GOOGLE_API_KEY`**: To get Google API Key [Click Here](https://makersuite.google.com/app/apikey).
   - **`BOT_TOKEN`**: The token you obtained from [@BotFather](https://t.me/BotFather).

## Deploy the Bot

```sh
git clone https://github.com/abirxdhack/GeminiProBots
cd GeminiProBot
pip install -r requirements.txt
python gemini.py
```

## Usage 🛠️

The bot supports the following commands:

- `/gem <prompt>`: Generates a response based on a provided text prompt.
- `/gemi <prompt>`: Generates a response based on a provided text prompt.
- `/gemini <prompt>`: Generates a response based on a provided text prompt.
- `.gem <prompt>`: Generates a response based on a provided text prompt.
- `.gemi <prompt>`: Generates a response based on a provided text prompt.
- `.gemini <prompt>`: Generates a response based on a provided text prompt.
- `/imgai <optional prompt>`: Generates a response based on an image. Ensure you reply to an image with the /imgai command. Optionally, you can provide a prompt along with the command, like `/imgai What is this?`, while replying to a photo to get a more specific response.
- `.imgai <optional prompt>`: Generates a response based on an image. Ensure you reply to an image with the /imgai command. Optionally, you can provide a prompt along with the command, like `/imgai What is this?`, while replying to a photo to get a more specific response.
## Owner ⚡️

- Name: Bisnu Ray
- Telegram: [@TheSmartBisnu](https://t.me/TheSmartBisnu)

## Note 
I Just Added Start Message And Added . / Support + Group  So Main Credit TheSmartBisnu

## Update ⚡️

- Name: Abir Arafat Chawdhury
- Telegram: [@abirxdhackz](https://t.me/abirxdhackz)

Feel free to reach out if you have any questions or feedback.
