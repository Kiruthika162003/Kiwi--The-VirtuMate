import requests

class KiwiAssistant:
    def __init__(self):
        self.chatbot = pipeline("conversational")
        self.tmdb_api_key = "your_tmdb_api_key"
        self.lastfm_api_key = "your_lastfm_api_key"
        self.google_books_api_key = "your_google_books_api_key"
    
    def communicate(self, user_input):
        conv = Conversation([{"role": "system", "content": "I am Kiwi, your helpful assistant."}, {"role": "user", "content": user_input}])
        response = self.chatbot(conv)[-1]["generated"]["text"]
        return response
    
    def get_movie_recommendation(self, genre):
        url = f"https://api.themoviedb.org/3/discover/movie"
        params = {
            "api_key": self.tmdb_api_key,
            "sort_by": "popularity.desc",
            "with_genres": genre
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "results" in data:
                movie = data["results"][0]["title"]
                return f"I recommend you watch: {movie}"
            else:
                return "Sorry, I couldn't find a movie recommendation."
        except Exception as e:
            return "An error occurred while getting a movie recommendation."
    
    def get_music_recommendation(self, genre):
        url = f"http://ws.audioscrobbler.com/2.0/"
        params = {
            "method": "tag.gettoptracks",
            "tag": genre,
            "api_key": self.lastfm_api_key,
            "format": "json"
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "tracks" in data and "track" in data["tracks"]:
                song = data["tracks"]["track"][0]["name"]
                return f"I recommend you listen to: {song}"
            else:
                return "Sorry, I couldn't find a music recommendation."
        except Exception as e:
            return "An error occurred while getting a music recommendation."
    
    def get_book_recommendation(self, topic):
        url = f"https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": topic,
            "key": self.google_books_api_key
        }
        
        try:
            response = requests.get(url, params=params)
            data = response.json()
            
            if "items" in data:
                book = data["items"][0]["volumeInfo"]["title"]
                return f"I recommend you read: {book}"
            else:
                return "Sorry, I couldn't find a book recommendation."
        except Exception as e:
            return "An error occurred while getting a book recommendation."

def main():
    print("Kiwi: Hello! I'm Kiwi, your advanced virtual assistant.")
    print("Kiwi: How can I assist you today? Feel free to ask or command. Type 'exit' to end the conversation.")

    kiwi = KiwiAssistant()
    user_input = input("You: ")

    while user_input.lower() != "exit":
        if "movie recommendation" in user_input:
            genre = input("Enter movie genre (e.g., action, comedy, romance): ")
            movie_recommendation = kiwi.get_movie_recommendation(genre)
            print(f"Kiwi: {movie_recommendation}")
        elif "music recommendation" in user_input:
            genre = input("Enter music genre (e.g., rock, pop, jazz): ")
            music_recommendation = kiwi.get_music_recommendation(genre)
            print(f"Kiwi: {music_recommendation}")
        elif "book recommendation" in user_input:
            topic = input("Enter book topic or keyword: ")
            book_recommendation = kiwi.get_book_recommendation(topic)
            print(f"Kiwi: {book_recommendation}")
        else:
            kiwi_response = kiwi.communicate(user_input)
            print("Kiwi:", kiwi_response)

        user_input = input("You: ")

    print("Kiwi: Goodbye! Have a wonderful day.")

if __name__ == "__main__":
    main()
