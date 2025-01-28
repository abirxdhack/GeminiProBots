import os
import io
import logging
import PIL.Image
from pyrogram.types import Message
import google.generativeai as genai
from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN, GOOGLE_API_KEY, MODEL_NAME

app = Client(
    "gemini_session",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.MARKDOWN
)

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)

@app.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    start_message = (
        "**Welcome to Gemini AI Bot!**\n\n"
        "I am here to assist you with advanced AI capabilities. Here are my commands:\n\n"
        "➢ **/gem [Question]** - Ask a question to Gemini AI.\n"
        "   - Example: `/gem How does photosynthesis work?` (Returns an explanation of photosynthesis)\n\n"
        "➢ **/imgai [Optional Prompt]** - Analyze an image or generate a response based on it.\n"
        "   - Basic Usage: Reply to an image with `/imgai` to get a general analysis.\n"
        "   - With Prompt: Reply to an image with `/imgai [Your Prompt]` to get a specific response.\n"
        "   - Example 1: Reply to an image with `/imgai` (Provides a general description of the image).\n"
        "   - Example 2: Reply to an image with `/imgai What is this?` (Provides a specific response based on the prompt and image).\n\n"
        "> **NOTE:**\n"
        "1️⃣ These tools leverage advanced AI models for accurate and detailed outputs."
    )
    await message.reply_text(start_message)

@app.on_message(filters.command("gem"))
async def gemi_handler(client: Client, message: Message):
    loading_message = None
    try:
        loading_message = await message.reply_text("**Generating response ⚡️ please wait...**")

        if len(message.text.strip()) <= 5:
            await message.reply_text("**Provide a prompt after the command ❌ **")
            return

        prompt = message.text.split(maxsplit=1)[1]
        response = model.generate_content(prompt)

        response_text = response.text
        if len(response_text) > 4000:
            parts = [response_text[i:i + 4000] for i in range(0, len(response_text), 4000)]
            for part in parts:
                await message.reply_text(part)
        else:
            await message.reply_text(response_text)

    except Exception as e:
        await message.reply_text(f"**An error occurred ❌ : {str(e)}**")
    finally:
        if loading_message:
            await loading_message.delete()

@app.on_message(filters.command("imgai"))
async def generate_from_image(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        await message.reply_text("**Please reply to a photo for a response ❌ **")
        return

    prompt = message.command[1] if len(message.command) > 1 else message.reply_to_message.caption or "Describe this image."

    processing_message = await message.reply_text("**Processing The Image And Generating Response ⚡️ please wait...**")

    try:
        img_data = await client.download_media(message.reply_to_message, in_memory=True)
        img = PIL.Image.open(io.BytesIO(img_data.getbuffer()))

        response = model.generate_content([prompt, img])
        response_text = response.text

        await message.reply_text(response_text, parse_mode=None)
    except Exception as e:
        logging.error(f"Error during image analysis: {e}")
        await message.reply_text("**An error occurred. Please try again ❌ **")
    finally:
        await processing_message.delete()

if __name__ == '__main__':
    app.run()
