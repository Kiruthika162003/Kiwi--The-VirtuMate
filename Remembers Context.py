import speech_recognition as sr
import pyttsx3

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.recognizer = sr.Recognizer()
        self.speaker = pyttsx3.init()
        self.conversation_context = []
    
    def communicate(self, user_input):
        if self.conversation_context:
            self.conversation_context[-1]["user_input"] = user_input
        
        conv = Conversation(self.conversation_context + [{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        self.conversation_context.append({"role": "user", "content": user_input})
        self.conversation_context.append({"role": "assistant", "content": response})
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
    
    def speak(self, message):
        self.speaker.say(message)
        self.speaker.runAndWait()

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "listen" in user_input:
            voice_input = kiwi.listen()
            print("You (Voice):", voice_input)
            kiwi_response = kiwi.communicate(voice_input)
        else:
            kiwi_response = kiwi.communicate(user_input)

        print("Kiwi:", kiwi_response)
        kiwi.speak(kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
