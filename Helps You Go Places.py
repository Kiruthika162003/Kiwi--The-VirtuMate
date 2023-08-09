import requests

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.api_key = "your_google_maps_api_key"
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def get_directions(self, origin, destination, travel_mode="driving"):
        url = "https://maps.googleapis.com/maps/api/directions/json"
        params = {
            "origin": origin,
            "destination": destination,
            "mode": travel_mode,
            "key": self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("status") == "OK" and "routes" in data:
                route = data["routes"][0]
                duration = route["legs"][0]["duration"]["text"]
                distance = route["legs"][0]["distance"]["text"]
                steps = route["legs"][0]["steps"]
                
                directions = [f"Duration: {duration}", f"Distance: {distance}"]
                for step in steps:
                    directions.append(step["html_instructions"])
                
                return "\n".join(directions)
            else:
                return "Sorry, I couldn't retrieve directions at the moment."
        except Exception as e:
            return "An error occurred while retrieving directions."

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "get directions" in user_input:
            origin = input("Enter starting location: ")
            destination = input("Enter destination location: ")
            travel_mode = input("Enter travel mode (driving, walking, transit): ").lower()
            
            directions = kiwi.get_directions(origin, destination, travel_mode)
            print(f"Kiwi: Directions:\n{directions}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
