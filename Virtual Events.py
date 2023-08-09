class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.events = []
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def create_event(self, title, date_time, platform):
        self.events.append({"title": title, "date_time": date_time, "platform": platform})
        return f"Event '{title}' on {date_time} has been created on {platform.capitalize()}."
    
    def get_upcoming_events(self):
        upcoming_events = [event for event in self.events if event["date_time"] > "2023-08-09 00:00:00"]
        if not upcoming_events:
            return "There are no upcoming events."
        event_list = "\n".join([f"• {event['title']} on {event['date_time']} via {event['platform'].capitalize()}" for event in upcoming_events])
        return f"Upcoming Events:\n{event_list}"
    
def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "create event" in user_input:
            title = input("Enter event title: ")
            date_time = input("Enter event date and time (YYYY-MM-DD HH:MM:SS): ")
            platform = input("Enter event platform (Zoom, Microsoft Teams, Google Meet): ")
            event_response = kiwi.create_event(title, date_time, platform)
            print(f"Kiwi: {event_response}")
        elif "upcoming events" in user_input:
            upcoming_events = kiwi.get_upcoming_events()
            print(f"Kiwi: {upcoming_events}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
