# Little Sage Chatbot

A simple Python chatbot with a tsundere personality – grumpy but secretly helpful. This project was created as a personal exercise to practice Python basics (loops, dictionaries, functions) and add some fun to coding.

## Overview

This chatbot responds to basic user inputs with a mix of sass and reluctant assistance. It includes triggers for greetings, farewells, help requests, and even some bad jokes. The code was initially written in Portuguese, but the base has been translated to English using GPT (because the creator is lazy) for better accessibility on GitHub. This README was crafted by Grok (xAI), following the creator's instructions – no deception intended, just laziness acknowledged.

## Updates in This Version

- Added NLTK library for natural language processing: Now uses `word_tokenize` to break user messages into words and `stopwords` to filter out useless common words (like "the", "is", etc.). This makes matching triggers more accurate and efficient, ignoring filler words.
- Improved input handling: The chatbot now processes filtered words to check against response keys, reducing false negatives for varied user inputs.

## Features

- Responds to common phrases like "hi," "help," "bye," and more.
- Tsundere personality with grumpy yet caring replies (e.g., "Hmph, don't waste my time.").
- Random response selection for variety.
- Enhanced message processing with NLTK for better keyword detection.
- Graceful exit on farewell messages.

## How to Run

1. Ensure you have Python 3.x installed.
2. Install NLTK and download required data (run in Python console: `import nltk; nltk.download('punkt'); nltk.download('stopwords')`).
3. Clone this repository:

   ```
   git clone https://github.com/Yllodido3d/little-sage-agent.git
   ```
3. Navigate to the project folder and run the script:

   ```
   python chatbotsábioV0.2.py
   ```
5. Start chatting! Type messages and see the chatbot's responses.

## Code Details

- The dictionary of responses was crafted by Grok (xAI), adding a tsundere flair to keep things interesting.
- Uses `random.choice()` for dynamic replies and a simple loop to handle user input.
- NLTK integration: Tokenizes and filters user messages to improve trigger matching.
- No other external dependencies besides NLTK – pure Python otherwise!

## Future Improvements

- Add more response categories or advanced NLP features.
- Implement file storage for custom user inputs.
- Maybe make it less grumpy... but don’t count on it.

## Contributing

Feel free to fork and submit pull requests. Suggestions are welcome, but don’t expect me to be nice about it.

## License

This project is for personal use. No formal license yet – consider it a gift from a reluctant AI.
