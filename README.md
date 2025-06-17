# Discord Bot with OpenAI

A Discord bot built with Python that integrates OpenAI's GPT to answer user questions directly in Discord using the `!ask` command.

## Features

- Friendly Greeting: Use `!hello` to get a welcome from the bot.
- AI Q&A: Ask anything with `!ask <your question>`, and get a smart answer using OpenAI.
- Simple Setup: Easy configuration using environment variables.
- Error Handling: Graceful response if OpenAI API fails.

## Requirements

- Python 3.8+
- discord.py
- openai
- python-dotenv

## Installation

1. Clone this repository:

```bash
git clone https://github.com/abdessamadG/python_discord_bot.git
cd python_discord_bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your discord token and openai api key in .env file

## Usage
```bash
python discord_bot.py
```

### commands
```
!hello: Greets the user.
!ask <question>: Sends your question to OpenAI and replies with the answer.
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
