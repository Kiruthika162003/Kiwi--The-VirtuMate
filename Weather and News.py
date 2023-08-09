import requests

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.weather_api_key = "your_openweathermap_api_key"
        self.news_api_key = "your_news_api_key"
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def get_weather(self, city_name):
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city_name,
            "appid": self.weather_api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("cod") == 200:
                weather_description = data["weather"][0]["description"]
                temperature = data["main"]["temp"]
                return f"Current weather in {city_name}: {weather_description}, Temperature: {temperature}°C"
            else:
                return "Sorry, I couldn't retrieve weather information."
        except Exception as e:
            return "An error occurred while retrieving weather information."
    
    def get_news(self, query):
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": self.news_api_key,
            "q": query
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if data.get("status") == "ok" and "articles" in data:
                articles = data["articles"][:3]  # Get top 3 articles
                news_stories = []
                for article in articles:
                    title = article["title"]
                    source = article["source"]["name"]
                    news_stories.append(f"{title} (Source: {source})")
                
                return "\n".join(news_stories)
            else:
                return "Sorry, I couldn't retrieve news articles."
        except Exception as e:
            return "An error occurred while retrieving news articles."

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "weather" in user_input:
            city_name = input("Enter city name: ")
            weather_info = kiwi.get_weather(city_name)
            print(f"Kiwi: {weather_info}")
        elif "news" in user_input:
            query = input("Enter a news topic: ")
            news_articles = kiwi.get_news(query)
            print(f"Kiwi: Latest news:\n{news_articles}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
