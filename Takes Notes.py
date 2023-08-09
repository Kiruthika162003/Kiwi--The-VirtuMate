import os
import speech_recognition as sr

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.recognizer = sr.Recognizer()
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def listen(self):
        with sr.Microphone() as source:
            print("Kiwi: Listening...")
            audio = self.recognizer.listen(source)
            
            try:
                user_input = self.recognizer.recognize_google(audio)
                return user_input
            except sr.UnknownValueError:
                return "I'm sorry, I couldn't understand you."
            except sr.RequestError:
                return "Sorry, I'm having trouble accessing the speech recognition service."
    
    def take_notes(self, note_text):
        with open("notes.txt", "a") as file:
            file.write(note_text + "\n")
        return "Note saved successfully."

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "take a note" in user_input:
            note_input = kiwi.listen()
            print("You (Voice):", note_input)
            note_response = kiwi.take_notes(note_input)
            print(f"Kiwi: {note_response}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
