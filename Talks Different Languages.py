from googletrans import Translator

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.translator = Translator()
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def translate(self, text, target_language):
        translation = self.translator.translate(text, dest=target_language)
        return translation.text

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "translate" in user_input:
            target_language = input("Enter target language code (e.g., 'fr' for French): ")
            text_to_translate = user_input.replace("translate", "").strip()
            translated_text = kiwi.translate(text_to_translate, target_language)
            print(f"Kiwi: Translated text: {translated_text}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
