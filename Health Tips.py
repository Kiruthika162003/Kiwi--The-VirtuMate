import random

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.health_tips = [
            "Stay hydrated by drinking plenty of water throughout the day.",
            "Get enough sleep to ensure your body can recover and rejuvenate.",
            "Eat a balanced diet rich in fruits, vegetables, lean proteins, and whole grains.",
            "Engage in regular physical activity to keep your body and mind healthy.",
            "Practice stress-relief techniques such as meditation or deep breathing.",
            "Limit processed foods and sugary drinks to maintain a healthy lifestyle.",
            "Remember to take breaks and stretch if you're sitting for long periods.",
            "Avoid smoking and excessive alcohol consumption for better overall health.",
            "Stay connected with friends and family for a strong social support system."
        ]
        self.workout_suggestions = [
            "Try a 30-minute brisk walk or jog in your local park.",
            "Engage in a home workout routine that includes bodyweight exercises like squats, push-ups, and lunges.",
            "Join a yoga or pilates class for flexibility and relaxation.",
            "Go for a swim at your local pool for a full-body workout.",
            "Consider cycling or biking for cardiovascular fitness.",
            "Explore a dance workout, such as Zumba or dance aerobics, for a fun and energetic exercise session.",
            "Challenge yourself with a high-intensity interval training (HIIT) workout.",
            "Practice a calming tai chi routine to improve balance and coordination.",
            "Join a local sports club or team to stay active and socialize."
        ]
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def get_health_tip(self):
        return random.choice(self.health_tips)
    
    def get_workout_suggestion(self):
        return random.choice(self.workout_suggestions)

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "health tip" in user_input:
            health_tip = kiwi.get_health_tip()
            print(f"Kiwi: Health Tip: {health_tip}")
        elif "workout suggestion" in user_input:
            workout_suggestion = kiwi.get_workout_suggestion()
            print(f"Kiwi: Workout Suggestion: {workout_suggestion}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
