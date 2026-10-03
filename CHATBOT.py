import datetime
import random


# -----------------------------
# Chatbot Functions
# -----------------------------

def get_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%I:%M %p")


def get_date():
    current_date = datetime.datetime.now()
    return current_date.strftime("%d-%m-%Y")


def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
        "Why was the computer cold? It left its Windows open! 😄",
        "Why did the programmer quit his job? Because he didn't get arrays! 😂"
    ]

    return random.choice(jokes)


def calculator():
    print("Bot: Enter two numbers and an operator.")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                return "Cannot divide by zero!"
            result = num1 / num2

        else:
            return "Invalid operator!"

        return f"Result = {result}"

    except ValueError:
        return "Please enter valid numbers."


# -----------------------------
# Main Chatbot
# -----------------------------

def chatbot():

    print("=" * 40)
    print("        🤖 PYTHON CHATBOT")
    print("=" * 40)

    name = input("Bot: What is your name?\nYou: ")

    print(f"\nBot: Nice to meet you, {name}! 😊")
    print("Bot: You can ask me things like:")
    print("     - Hello")
    print("     - How are you?")
    print("     - What is Python?")
    print("     - What is the time?")
    print("     - What is the date?")
    print("     - Tell me a joke")
    print("     - Calculate")
    print("     - Bye")

    while True:

        user = input(f"\n{name}: ").lower().strip()

        # Greeting
        if user in ["hi", "hello", "hey"]:

            responses = [
                "Hello! 😊",
                "Hi! Nice to talk with you!",
                "Hey! How can I help you?"
            ]

            print("Bot:", random.choice(responses))


        # How are you
        elif "how are you" in user:

            print("Bot: I'm doing great! 😄 Thanks for asking.")


        # User name
        elif "my name" in user:

            print(f"Bot: Your name is {name}.")


        # Bot name
        elif "your name" in user:

            print("Bot: My name is PyBot 🤖")


        # Python
        elif "python" in user:

            print(
                "Bot: Python is a high-level, "
                "easy-to-learn programming language. 🐍"
            )


        # Time
        elif "time" in user:

            print("Bot: Current time is", get_time())


        # Date
        elif "date" in user:

            print("Bot: Today's date is", get_date())


        # Joke
        elif "joke" in user:

            print("Bot:", tell_joke())


        # Calculator
        elif "calculate" in user or "calculator" in user:

            result = calculator()
            print("Bot:", result)


        # Help
        elif "help" in user:

            print("\nBot: Here are the things I can do:")
            print("1. Chat with you")
            print("2. Tell current time")
            print("3. Tell today's date")
            print("4. Tell jokes")
            print("5. Answer basic Python questions")
            print("6. Calculate numbers")


        # Exit
        elif user in ["bye", "exit", "quit"]:

            print(f"Bot: Goodbye {name}! 👋")
            print("Bot: Have a great day! 😊")
            break


        # Unknown question
        else:

            print(
                "Bot: Sorry, I don't understand that yet. "
                "Try typing 'help'."
            )


# Start chatbot
chatbot()