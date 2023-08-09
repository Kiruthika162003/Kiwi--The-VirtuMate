class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.smart_home_devices = {
            "lights": {"status": "off"},
            "thermostat": {"temperature": 72}
        }
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def control_smart_home_device(self, device, action):
        device = device.lower()
        action = action.lower()
        
        if device in self.smart_home_devices:
            if device == "lights":
                if action == "on":
                    self.smart_home_devices[device]["status"] = "on"
                    return f"The {device} are now turned on."
                elif action == "off":
                    self.smart_home_devices[device]["status"] = "off"
                    return f"The {device} are now turned off."
                else:
                    return f"Sorry, I couldn't understand the action for {device}."
            elif device == "thermostat":
                if action.startswith("set temperature"):
                    temperature = int(action.split()[-1])
                    self.smart_home_devices[device]["temperature"] = temperature
                    return f"The {device} temperature is set to {temperature} degrees."
                else:
                    return f"Sorry, I couldn't understand the action for {device}."
        else:
            return f"Sorry, I don't have control over {device}."
    
def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "control device" in user_input:
            device = input("Enter device (lights, thermostat): ")
            action = input("Enter action (on, off, set temperature): ")
            smart_home_response = kiwi.control_smart_home_device(device, action)
            print(f"Kiwi: {smart_home_response}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
