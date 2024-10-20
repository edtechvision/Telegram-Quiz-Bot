
# 🤖 Telegram Quiz Bot Setup Guide

Follow these simple steps to set up your **Telegram Quiz Bot**.

---

## 🚀 Prerequisites

Make sure you have the following ready:

- 🐍 **Python 3.x** installed
- 🌐 An **Ngrok** account (for tunneling)
- 📱 A **Telegram** account

---

## 📋 Setup Instructions

### Step 1: Create Your Telegram Bot on BotFather

1. Open **Telegram** and search for **BotFather**.
2. Start a chat with **BotFather** and use the command:
   ```bash
   /newbot
   ```
3. Follow the prompts to:
   - **Name your bot**.
   - **Set a username** for your bot (must end with `_bot`).
4. **Save the API key** that **BotFather** provides for later use.

---

### Step 2: Create an Ngrok Account

1. Go to [Ngrok](https://ngrok.com/) and sign up for an account.
2. Once logged in, find and copy your **Ngrok Auth Token** from your Ngrok dashboard.

---

### Step 3: Extract the Project Files

1. **Download** the zip file containing the bot's source code.
2. **Extract** the contents to your desired folder.

---

### Step 4: Configure the Bot

1. Open the `config.py` file.
2. Replace the placeholder values with your own:
   ```python
   QUIZ_BOT_NAME = "YOUR QUIZ BOT NAME"
   NGROK_TOKEN = "YOUR NGROK AUTH TOKEN"
   API_KEY = "YOUR TELEGRAM BOT API KEY"
   ```
3. **Save** the file.

---

### Step 5: Install Required Libraries

1. Open a terminal and navigate to the project folder.
2. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 6: Run the Quiz Bot

1. In the terminal, start the bot by running:
   ```bash
   python app.py
   ```

---

## 🎉 You're Ready!

Your Telegram Quiz Bot is now up and running. Open Telegram, find your bot by its username, and start interacting with it!

---

Happy quizzing! 🎮
