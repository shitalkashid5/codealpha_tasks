print("================================")
print("        BASIC CHATBOT")
print("================================")

print("Chatbot: Hello! I am your chatbot.")
print("Chatbot: You can say hello, how are you, or bye.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hi! Nice to meet you. 😊")

    elif user_input == "how are you":
        print("Chatbot: I'm fine, thanks! 😊")

    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Chatbot: Sorry, I don't understand that. 🤔")