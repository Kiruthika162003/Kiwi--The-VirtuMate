import requests

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.api_key = "your_google_api_key"
        self.search_engine_id = "your_search_engine_id"
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def find_information(self, query):
        url = f"https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.api_key,
            "cx": self.search_engine_id,
            "q": query
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "items" in data:
                first_result = data["items"][0]
                return first_result["title"], first_result["link"]
            else:
                return "No information found.", ""
        except Exception as e:
            return "An error occurred while searching for information.", ""

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "find information" in user_input:
            query = user_input.replace("find information", "").strip()
            title, link = kiwi.find_information(query)
            if link:
                print(f"Kiwi: I found information: '{title}'.")
                print(f"Kiwi: Here's the link: {link}")
            else:
                print("Kiwi: Sorry, I couldn't find relevant information.")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
