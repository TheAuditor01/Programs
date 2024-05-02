import re

responses = {
    "hi": "Hello! Welcome to The Movie Bot.",
    "hello": "Hi there! How can I assist you with your movie queries?",
    "highest_rated": "The highest rated movie of all time is The Shawshank Redemption.",
    "comedy_movies": "Here are some popular movies in that genre: The Hangover, Superbad, and Anchorman.",
    "bollywood_thriller": "Some of the best Bollywood thriller movies include Dangal and Baahubali.",
    "watch_movies": "You can watch movies on platforms like Netflix, Amazon Prime, and Disney+.",
    "top_grossing": "The topmost grossing movie of all time is Titanic.",
    "most_watched_tvshow": "The most watched TV show is Game of Thrones.",
    "movies_for_kids": "Some great movies for kids include Finding Nemo, Toy Story, and The Lion King.",
    "family_movies": "Some of the best family movies to watch include The Lion King, Frozen, and Toy Story.",
    "other_movies_by_christopher_nolan": "Other movies by Christopher Nolan include Inception, The Dark Knight, and Interstellar.",
    "hollywood_comedy": "Some popular Hollywood comedy movies include The Hangover, Superbad, and Anchorman.",
    "genres": "What genre are you interested in? (Action, Adventure, Comedy, Drama, Romance)",
    "goodbye": "Thank you for visiting! Have a great day!",
    "unsupported": "I'm currently under development and unable to answer that question. Please Google it, and you will find it. Sorry for the inconvenience.",
    "popular_movie_year": "The most popular movie of the year varies each year. You can check the latest box office hits for the current year.",
    "mood_recommendation": "Sure, I can help with that. What mood are you in?",
    "classic_movies": "Some classic movies include 'Citizen Kane,' 'The Godfather,' and 'Pulp Fiction.'",
    "movie_genres": "You can learn about movie genres through various online resources, books, and film studies courses.",
    "popular_movies_2020": "Some popular movies from the 2020s include 'Tenet,' 'Wonder Woman 1984,' and 'The Mandalorian.'",
    "latest_movie_releases": "I can provide information on the latest movie releases. Would you like to know about upcoming releases or recent releases?",
    "improve_movie_experience": "Improving your movie watching experience can involve choosing the right movie for your mood, ensuring a comfortable viewing environment, and perhaps even watching movies with friends or family.",
    "tips_watching_movies": "Tips for watching movies at home include choosing a comfortable seating arrangement, ensuring good lighting, and having a selection of snacks and drinks.",
    "date_night_movie": "For a romantic date night, consider watching a classic love story or a movie that's known for its romantic scenes.",
    "similar_movies": "You can find movies similar to your favorite by looking at the movie's genre, director, or actors. Websites like IMDb and Letterboxd can also help you discover similar movies."
}

# Define rules for the chatbot using regex
def respond_to_input(user_input):
    user_input = user_input.lower()
    
    if re.match(r'hi|hello', user_input):
        return responses['hi']
    elif re.search(r'^what is the highest rated movie of all time$', user_input, re.IGNORECASE):
        return responses['highest_rated']
    elif re.search(r'^can you list some popular movies in the comedy genre$', user_input, re.IGNORECASE):
        return responses['comedy_movies']
    elif re.search(r'^what are some of the best bollywood thriller movies$', user_input, re.IGNORECASE):
        return responses['bollywood_thriller']
    elif re.search(r'^how can i watch movies$', user_input, re.IGNORECASE):
        return responses['watch_movies']
    elif re.search(r'^what is the topmost grossing movie of all time$', user_input, re.IGNORECASE):
        return responses['top_grossing']
    elif re.search(r'^which is the most watched tv show$', user_input, re.IGNORECASE):
        return responses['most_watched_tvshow']
    elif re.search(r'^what are some movies for kids$', user_input, re.IGNORECASE):
        return responses['movies_for_kids']
    elif re.search(r'^what are the best family movies$', user_input, re.IGNORECASE):
        return responses['family_movies']
    elif re.search(r'^can you tell me about other movies by christopher nolan$', user_input, re.IGNORECASE):
        return responses['other_movies_by_christopher_nolan']
    elif re.search(r'^what are some popular hollywood comedy movies$', user_input, re.IGNORECASE):
        return responses['hollywood_comedy']
    elif re.search(r'^what genre are you interested in$', user_input, re.IGNORECASE):
        return responses['genres']
    elif re.search(r'^goodbye$', user_input, re.IGNORECASE):
        return responses['goodbye']
    elif re.search(r'^what is the most popular movie of the year$', user_input, re.IGNORECASE):
        return responses['popular_movie_year']
    elif re.search(r'^can you recommend a movie based on my mood$', user_input, re.IGNORECASE):
        return responses['mood_recommendation']
    elif re.search(r'^what are some classic movies$', user_input, re.IGNORECASE):
        return responses['classic_movies']
    elif re.search(r'^how can i learn more about movie genres$', user_input, re.IGNORECASE):
        return responses['movie_genres']
    elif re.search(r'^what are some popular movies from the 2020s$', user_input, re.IGNORECASE):
        return responses['popular_movies_2020']
    elif re.search(r'^can you tell me about the latest movie releases$', user_input, re.IGNORECASE):
        return responses['latest_movie_releases']
    elif re.search(r'^how can i improve my movie watching experience$', user_input, re.IGNORECASE):
        return responses['improve_movie_experience']
    elif re.search(r'^how can i find movies similar to my favorite movie$', user_input, re.IGNORECASE):
        return responses['similar_movies']
    else:
        return responses['unsupported']

# Start the conversation
print("Welcome to The Movie Bot!")
print("You can start by saying 'hi' or 'hello'.")
print("To exit, simply say 'bye' or 'goodbye'.\n")

while True:
    user_input = input("User> ")
    response = respond_to_input(user_input)
    print("Bot> " + response)
    if user_input.lower() in ['bye', 'goodbye']:
        break
