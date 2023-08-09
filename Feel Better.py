class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.relaxation_tips = [
            "Take a few deep breaths and focus on your breath.",
            "Listen to calming music or nature sounds.",
            "Practice progressive muscle relaxation: tense and release each muscle group.",
            "Close your eyes and visualize a peaceful place.",
            "Try mindfulness meditation: focus on the present moment without judgment.",
            "Engage in gentle stretching or yoga.",
            "Write down your thoughts in a journal to release stress.",
            "Spend time in nature or take a short walk outside.",
            "Take a warm bath to relax your body.",
            "Connect with a friend or loved one for support.",
            "Practice gratitude by listing things you're thankful for.",
            "Engage in a creative activity like drawing or crafting.",
            "Use aromatherapy with calming scents like lavender or chamomile.",
            "Laugh! Watch a funny movie or read a humorous book.",
            "Try a quick mindfulness exercise: observe your surroundings and senses.",
        ]
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def provide_relaxation_tip(self):
        return "Relaxation Tip: " + random.choice(self.relaxation_tips)
    
def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "relaxation tip" in user_input:
            relaxation_tip = kiwi.provide_relaxation_tip()
            print(f"Kiwi: {relaxation_tip}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
