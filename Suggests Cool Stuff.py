import requests

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.tmdb_api_key = "your_tmdb_api_key"
        self.lastfm_api_key = "your_lastfm_api_key"
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def suggest_cool_stuff(self, user_preferences):
        movie_suggestion = self.get_movie_suggestion(user_preferences)
        music_suggestion = self.get_music_suggestion(user_preferences)
        
        return f"Kiwi suggests: {movie_suggestion} and {music_suggestion}"
    
    def get_movie_suggestion(self, preferences):
        url = f"https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": self.tmdb_api_key,
            "sort_by": "popularity.desc",
            "with_genres": preferences.get("movie_genre")
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "results" in data:
                return data["results"][0]["title"]
            else:
                return "a popular movie"
        except Exception as e:
            return "a popular movie"
    
    def get_music_suggestion(self, preferences):
        url = f"http://ws.audioscrobbler.com/2.0/"
        params = {
            "method": "tag.gettoptracks",
            "tag": preferences.get("music_genre"),
            "api_key": self.lastfm_api_key,
            "format": "json"
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "tracks" in data and "track" in data["tracks"]:
                return data["tracks"]["track"][0]["name"]
            else:
                return "a popular song"
        except Exception as e:
            return "a popular song"

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "suggest cool stuff" in user_input:
            preferences = {
                "movie_genre": "28",  # Action genre ID for TMDb
                "music_genre": "rock"
            }
            cool_stuff_suggestion = kiwi.suggest_cool_stuff(preferences)
            print(f"Kiwi: {cool_stuff_suggestion}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
