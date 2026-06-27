# CodeAlpha Task 4 - Basic Chatbot

def chatbot():

    print(" Welcome to Basic Chatbot!")
    print("Type 'bye' to exit\n")


    while True:

        user = input("You: ").lower().strip()


        if user == "hello" or user == "hi":
            print("Bot: Hi! How can I help you?")


        elif user == "how are you":
            print("Bot: I am fine, thanks!")


        elif user == "your name":
            print("Bot: My name is CodeBot.")


        elif user == "what can you do":
            print("Bot: I can answer simple questions.")


        elif user == "thanks":
            print("Bot: You're welcome!")


        elif user == "bye":
            print("Bot: Goodbye! Have a nice day ")
            break


        else:
            print("Bot: Sorry, I don't understand.")


chatbot()