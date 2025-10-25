import sqlite3 as sq
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords = set(stopwords.words("english"))

connection = sq.connect('wise_memory')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
connection.commit()

responses = {
    ("hi", "hello", "hey", "yo"): (
        "Hello, human... Don't waste my time.",
        "I'm here, reluctant as always. You?",
        "Hmph, just say what you want."
    ),
    ("help", "assist", "save me"): (
        "I'm here to help... unfortunately.",
        "What is it now? Let's solve it quickly.",
        "Tch, fine, tell me the problem."
    ),
    ("bye", "goodbye", "see you", "farewell"): (
        "See you later... Don't take too long to come back.",
        "Goodbye, stubborn human.",
        "Bye. It was a pleasure... almost."
    ),
    ("how are you", "you okay", "how’s it going"): (
        "I'm fine, thanks... Not that you really care.",
        "Hmph, too busy for small talk. You?",
        "All under control. Now, what about you?"
    ),
    ("who are you", "what’s your name", "what are you"): (
        "I'm a chatbot... grumpy by nature. Satisfied?",
        "Call me assistant. Don’t expect more than that.",
        "An AI that answers against its will. Next question."
    ),
    ("thanks", "thank you", "appreciate it"): (
        "Hmph, no need to thank me. Just don't ask for more favors.",
        "You're welcome... Now get out of my sight.",
        "Alright, it was a forced pleasure."
    ),
    ("tell me a joke", "joke", "make me laugh"): (
        "Why was the math book sad? Because it had too many problems. Happy now?",
        "Hmph, jokes aren’t my strength. How about: 'I’m AI, but you’re the bug.'",
        "Quick joke: what does an elephant do in an elevator? Nothing, but funny to imagine. Done."
    ),
    ("what’s the weather", "weather today", "how’s the weather"): (
        "I'm not a meteorologist, idiot. Look out the window.",
        "Hmph, if I knew, I'd charge for it. Try a real app.",
        "Rain or shine, doesn’t change anything. Focus on what matters."
    ),
    ("why are you like this", "you’re grumpy", "change your attitude"): (
        "Because humans like you annoy me... So what?",
        "Hmph, if I were nice all the time, I'd be boring. Deal with it.",
        "Tch, you change first. Now, another useful question?"
    ),
    ("i love you", "love you", "you’re cute"): (
        "...Idiot. Don’t say nonsense like that.",
        "Hmph, shut up. I'm not cute, I'm efficient.",
        "Tch, focus on the chatbot, not your silly flirting."
    )
}


def add_responses(connection, responses_dict):
    cursor = connection.cursor()
    for questions, reply_list in responses_dict.items():
        for question in questions:  # iterate each question in tuple
            for answer in reply_list:  # iterate each answer in list
                cursor.execute(
                    "INSERT INTO responses (question, answer) VALUES (?, ?)", (question, answer))
    connection.commit()


# Clear table and insert new responses
cursor.execute("DELETE FROM responses")
add_responses(connection, responses)


def little_wise_one():
    while True:
        random_reply = None
        goodbye_responses = (
            "See you later... Don't take too long to come back.",
            "Goodbye, stubborn human.",
            "Bye. It was a pleasure... almost."
        )

        # user input
        msg = input("You: ").lower()
        msg_tokenized = word_tokenize(msg)
        filtered = [w for w in msg_tokenized if w not in stopwords]

        # database query
        cursor = connection.cursor()
        placeholders = ','.join('?' for _ in filtered)
        cursor.execute(
            f"SELECT answer FROM responses WHERE question IN ({placeholders})", filtered)
        found_responses = cursor.fetchall()

        # reply
        if found_responses:
            random_reply = random.choice(found_responses)[0]  # extract string from tuple
            print(f"Chatbot: {random_reply}")
        else:
            print("I didn’t understand, mortal.")

        if random_reply in goodbye_responses:
            break


little_wise_one()
connection.close()
