# Little Sage Chatbot (LittleSageV0.3)

A Python chatbot with a tsundere twist – grumpy on the outside, secretly useful. This project started as a personal exercise to master Python basics (loops, dictionaries, functions) and has evolved into a sass-filled assistant with memory. Created by a stubborn coder who’s too lazy to write this himself, so Grok (xAI) stepped in – no tricks, just pure reluctance!

## Overview

"Little Sage" responds to user inputs with a mix of attitude and hidden care, now powered by a SQLite database for memory. Originally coded in Portuguese and translated to English (thanks to GPT and creator laziness), this version upgrades the chatbot’s brain to store and retrieve responses dynamically. It’s still a work in progress, but it’s getting sassier and smarter!

## Updates in This Version (V0.3)

- **SQLite Integration**: Swapped the old dictionary for a `responses` table in `wise_memory.db`, adding `id`, `question`, `answer`, and `timestamp` fields. Responses are now stored and fetched from the database, making it scalable (and less prone to manual edits).
- **Database Initialization**: Includes a function to populate the table, with a `DELETE` and `INSERT` combo to refresh data on startup.
- **Query Logic**: Uses `SELECT` with `IN` clauses to match tokenized user inputs against database questions, improving flexibility over the dictionary approach.
- **NLTK Enhancements**: Continues using `word_tokenize` and `stopwords` to filter meaningful words, ensuring better intent detection.

## Features

- Handles common phrases like "hi," "help," "bye," and more with tsundere flair.
- Random response selection for variety and sass (e.g., "Hmph, don’t waste my time.").
- Persistent memory via SQLite, storing all question-answer pairs with timestamps.
- NLTK-powered input processing for smarter keyword matching.
- Clean exit on farewell messages.

## How to Run

1. Ensure Python 3.x is installed.
2. Install NLTK and download required data (run in Python console: `import nltk; nltk.download('punkt'); nltk.download('stopwords')`).
3. Clone this repository:
textgit clone https://github.com/Yllodido3d/little-sage-agent.git


Navigate to the project folder and install dependencies (if any beyond NLTK arise, check requirements.txt).


4. Navigate to the project folder and install dependencies (if any beyond NLTK arise, check `requirements.txt`).
5. Run the script:


6. Start chatting! Type messages and enjoy the chatbot’s reluctant responses.

## Code Details

- Responses crafted by Grok (xAI) with a tsundere personality to keep things spicy.
- Uses `random.choice()` for dynamic replies and a loop for continuous interaction.
- SQLite handles data storage with `INSERT` and `SELECT` queries, managed via `sqlite3`.
- NLTK filters out stopwords, making the chatbot less confused by filler words.
- No heavy dependencies – just Python, NLTK, and SQLite!

## Future Improvements

- Add more response categories or integrate external APIs (e.g., weather data).
- Enhance NLP with intent recognition or context awareness.
- Build a GUI or Telegram/Discord bot interface for easier access.
- Maybe soften the attitude… but don’t hold your breath!

## Contributing

Fork it and send pull requests if you dare. Suggestions are welcome, but expect a grumpy review – I’m not here to coddle you!

## License

Personal use only for now. No formal license – consider it a reluctant gift from an AI with attitude.
