import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "Feeling great, thanks!"],
    "what's up": ["Not much, just here to chat!", "Just chilling, how about you?"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "what can you do": ["I can chat with you, tell jokes, provide information, and more! Just ask me anything."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
}

def chat():
    print("AI: Hello, I'm your AI assistant. How can I help you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("AI: Goodbye!")
            break
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        if isinstance(response, list):
            print("AI:", random.choice(response))
        else:
            print("AI:", response)

if __name__ == "__main__":
    chat()
