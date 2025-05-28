# chatbot_logic.py

def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hello": "Hi! How can I help you today?",
        "hi": "Hello there!",
        "how are you": "I'm just a bot, but I'm doing great!",
        "what is your name": "I am your friendly chatbot.",
        "bye": "Goodbye! Have a nice day!",
        "thank you": "You're welcome!",
        "help": "You can ask me simple questions like 'what is your name', 'how are you', or say 'bye'."
    }

    return responses.get(user_input, "Sorry, I didn’t understand that.")
