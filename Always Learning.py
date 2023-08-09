class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.knowledge_base = {
            "greeting": ["Hello!", "Hi there!", "Hey!", "Greetings!"],
            "farewell": ["Goodbye!", "See you later!", "Farewell!", "Take care!"]
            # Add more predefined responses and categories as needed
        }
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def learn_response(self, category, response):
        category = category.lower()
        if category in self.knowledge_base:
            self.knowledge_base[category].append(response)
            return f"Thank you for teaching me! I'll remember the new {category} response."
        else:
            return f"Sorry, I can't learn responses for the {category} category."
    
    def get_learned_responses(self):
        response_list = "\n".join([f"{category.capitalize()}: {responses}" for category, responses in self.knowledge_base.items()])
        return "Learned Responses:\n" + response_list
    
def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "teach me" in user_input:
            category = input("Enter category you want to teach (e.g., greeting, farewell): ")
            response = input(f"Enter the new {category} response: ")
            learn_response = kiwi.learn_response(category, response)
            print(f"Kiwi: {learn_response}")
        elif "learned responses" in user_input:
            learned_responses = kiwi.get_learned_responses()
            print(f"Kiwi: {learned_responses}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
