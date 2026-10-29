"""Beginner-friendly rule-based chatbot."""
from datetime import datetime


def get_reply(message):
    message = message.strip().lower()

    if message in {"hello", "hi", "hey"}:
        return "Hi! How can I help you today?"
    if "how are you" in message:
        return "I'm doing well, thanks for asking! How are you?"
    if "your name" in message:
        return "I'm PyBot, a simple rule-based chatbot."
    if "time" in message:
        return "The current time on this computer is " + datetime.now().strftime("%H:%M") + "."
    if message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day."
    if "help" in message:
        return "Try saying hello, asking how I am, asking my name, or typing bye to exit."
    return "I'm not sure how to respond to that yet. Type 'help' to see example messages."


def main():
    print("=== PyBot: Basic Chatbot ===")
    print("Type 'help' for ideas or 'bye' to exit.")
    while True:
        message = input("You: ")
        reply = get_reply(message)
        print("PyBot:", reply)
        if message.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
