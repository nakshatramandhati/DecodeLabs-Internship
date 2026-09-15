# Project 1 - Rule-Based AI Chatbot
# DecodeLabs Artificial Intelligence Internship
# Batch: 2026


# Predefined responses for the chatbot
responses = {
    "hello": "Hi there! Welcome to DecodeLabs.",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How can I help you?",
    "good morning": "Good morning! Have a great day.",
    "how are you": "I am doing great. Thanks for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "what can you do": "I can respond to simple predefined questions using rules.",
    "what is artificial intelligence": (
        "Artificial Intelligence is the simulation of human intelligence "
        "by computers."
    ),
    "what is a chatbot": (
        "A chatbot is a computer program that communicates with users "
        "through text or voice."
    ),
    "what is rule based ai": (
        "Rule-Based AI uses predefined rules to decide how to respond "
        "to user input."
    ),
    "help": (
        "You can ask me about AI, chatbots, my name, or what I can do."
    ),
    "thank you": "You're welcome!",
    "thanks": "You're welcome! Happy to help."
}


# Welcome message
print("🤖 Bot: Hello! I am your Rule-Based AI Chatbot.")
print("🤖 Bot: You can ask me simple questions.")
print("🤖 Bot: Type 'bye', 'exit' or 'quit' to exit.")


# Continuous conversation loop
while True:

    # Get user input and clean it
    user_input = input("You: ").lower().strip()

    # Exit commands
    if user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("🤖 Bot: Goodbye! Have a great day!")
        break

    # Check whether the input has a predefined response
    if user_input in responses:
        print("🤖 Bot:", responses[user_input])

    # Fallback for unknown input
    else:
        print("🤖 Bot: I'm sorry, I don't understand that.")
