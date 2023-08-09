from googletrans import Translator
from gtts import gTTS
import os

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.translator = Translator()
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def learn_language(self, target_language, word):
        target_language = target_language.lower()
        translation = self.get_translation(target_language, word)
        if translation:
            pronunciation = self.get_pronunciation(target_language, word, translation)
            return f"In {target_language.capitalize()}, '{word}' translates to '{translation}'." + \
                   (f" Pronunciation: {pronunciation}" if pronunciation else "")
        else:
            return f"Sorry, I couldn't retrieve information for the word '{word}' in {target_language.capitalize()}."
    
    def get_translation(self, target_language, word):
        try:
            translation = self.translator.translate(word, src="en", dest=target_language)
            return translation.text
        except Exception as e:
            return None
    
    def get_pronunciation(self, target_language, word, translation):
        try:
            pronunciation = gTTS(text=translation, lang=target_language)
            pronunciation_path = "pronunciation.mp3"
            pronunciation.save(pronunciation_path)
            return pronunciation_path
        except Exception as e:
            return None

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "learn language" in user_input:
            target_language = input("Enter target language: ")
            word = input("Enter word you want to learn: ")
            language_response = kiwi.learn_language(target_language, word)
            print(f"Kiwi: {language_response}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
