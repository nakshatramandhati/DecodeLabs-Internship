movies = [
    {"title": "Inception", "genre": "sci-fi"},
    {"title": "Interstellar", "genre": "sci-fi"},
    {"title": "The Notebook", "genre": "romance"},
    {"title": "Titanic", "genre": "romance"},
    {"title": "The Conjuring", "genre": "horror"},
    {"title": "Annabelle", "genre": "horror"},
    {"title": "Avengers: Endgame", "genre": "action"},
    {"title": "John Wick", "genre": "action"},
    {"title": "The Hangover", "genre": "comedy"},
    {"title": "3 Idiots", "genre": "comedy"}
]

print("AI Movie Recommendation System")
print("Available genres: sci-fi, romance, horror, action, comedy")

preference = input("Enter your preferred genre: ").lower().strip()

recommendations = []

for movie in movies:
    if movie["genre"] == preference:
        recommendations.append(movie["title"])

if recommendations:
    print("\nRecommended Movies:")
    for movie in recommendations:
        print("-", movie)
else:
    print("\nSorry, no recommendations found for this genre.")
