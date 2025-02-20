import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?", ]
    ],
    [
        r"hi|hello|hey",
        ["Hi there!", "Hello!", "Hey there!"]
    ],
    [
        r"what is your name?",
        ["I don't have a name, I'm just a chatbot.", ]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm great, how about you?"]
    ],
    [
        r"quit",
        ["Bye! It was nice talking to you.", "See you later!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I didn't understand that.", "Could you please rephrase?", "Tell me more!"]
    ],
]

# Default reflections (can be customized)
reflections = {
    "i'm": "you are",
    "i am": "you are",
    "you are": "I am",
    "you're": "I am",
    "my": "your",
    "yours": "mine"
}

def chatbot():
    print("Hi! I'm a simple chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    nltk.download('punkt')  # Download necessary NLTK data (if not already downloaded)
    chatbot()
