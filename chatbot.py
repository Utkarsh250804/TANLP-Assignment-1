class MiniChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a bot, but I'm doing great! How about you?",
            "what's your name": "I'm a mini chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!",
        }
    
    def get_response(self, user_input):
        # Normalize user input to lowercase
        user_input = user_input.lower()
        return self.responses.get(user_input, "Sorry, I didn't understand that.")

    def run(self):
        print("Mini Chatbot: Hello! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("Mini Chatbot: Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"Mini Chatbot: {response}")

if __name__ == "__main__":
    bot = MiniChatbot()
    bot.run()
