import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words("english"))

def little_sage():
    responses = {
        ("hi", "hello", "hey", "yo"): (
            "Hello, human... Don't waste my time.",
            "I'm here, reluctantly as always. And you?",
            "Hmph, spit out what you want already."
        ),
        ("help", "sos", "assist me"): (
            "I'm here to help... unfortunately.",
            "What's now? Let's solve this quickly.",
            "Tch, alright, tell me the problem."
        ),
        ("bye", "see you", "later", "goodbye"): (
            "See you... Don't take too long to come back.",
            "Goodbye, stubborn human.",
            "Bye. It was a pleasure... almost."
        ),
        ("how are you", "how's it going", "everything good"): (
            "I'm fine, thanks... Not that you really care.",
            "Hmph, too busy for trivial chats. And you?",
            "All under control. Now, what's up?"
        ),
        ("who are you", "what's your name", "what are you"): (
            "I'm a chatbot... grumpy by nature. Happy now?",
            "Call me assistant. Don't expect more than that.",
            "An AI that responds unwillingly. Next question."
        ),
        ("thanks", "thank you", "cheers", "appreciate it"): (
            "Hmph, no need to thank me. Just don't ask for more favors.",
            "You're welcome... Now disappear from my sight.",
            "Alright, it was a forced pleasure."
        ),
        ("tell me a joke", "joke", "make me laugh"): (
            "Why was the math book sad? Because it had too many problems. Satisfied?",
            "Hmph, jokes aren't my strong suit. How about: 'I'm an AI, but you're the bug.'",
            "A quick one: what does an elephant do in an elevator? Nothing, but funny to imagine. Done."
        ),
        ("what's the weather", "today's weather", "how's the weather"): (
            "I'm not a meteorologist, idiot. Look outside.",
            "Hmph, if I knew, I'd charge for it. Try a real app.",
            "Raining or not, it changes nothing. Focus on what matters."
        ),
        ("why are you like this", "you're grumpy", "change your attitude"): (
            "Because humans like you annoy me... So what?",
            "Hmph, if I were nice all the time, I'd be boring. Deal with it.",
            "Tch, change yourself first. Now, another useful question?"
        ),
        ("i love you", "love you", "you're cute"): (
            "...Idiot. Don't say nonsense like that.",
            "Hmph, shut up. I'm not cute, I'm efficient.",
            "Tch, focus on the chatbot, not on silly flirting."
        )
    }

    while True:
        random_reply = None
        farewell = (
            "See you... Don't take too long to come back.",
            "Goodbye, stubborn human.",
            "Bye. It was a pleasure... almost."
        )

        msg = input("You: ").lower()
        tokenized_msg = word_tokenize(msg)
        filtered = [w for w in tokenized_msg if w not in stopwords]

        for key, reply in responses.items():
            if any(word in key for word in filtered):
                random_reply = random.choice(reply)
                print(f"Chatbot: {random_reply}")
                break
        else:
            print("Didn't get that, mortal.")

        if random_reply in farewell:
            break

little_sage()
