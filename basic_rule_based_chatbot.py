import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary downloads (run only once)
nltk.download('punkt')

# Define chatbot responses
responses = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that."
}

# Function to get response
def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())  # Tokenizing input and converting to lowercase
    for key in responses:
        if key in tokens:
            return responses[key]
    return responses["default"]

# Chat loop
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", responses["bye"])
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!", "I'm here to assist you!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break
    print("Chatbot:", chatbot_response(user_input))
import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!", "I'm here to assist you!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Take care!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", random.choice(responses["bye"]))
        break
    print("Chatbot:", chatbot_response(user_input))


