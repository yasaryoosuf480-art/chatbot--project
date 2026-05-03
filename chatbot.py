print("Chatbot is running... Type 'bye' to exit")

while True:
    user = input("You: ")

    if user == "hello":
        print("Bot: Hi there!")
    elif user == "how are you":
        print("Bot: I'm just code, but I'm working fine!")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand that yet.")
