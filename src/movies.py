movies_db = [
    {"id": 1, "title": "Inception", "genre": "Sci-Fi"},
    {"id": 2, "title": "Interstellar", "genre": "Sci-Fi"}
]

def get_movies():
    return movies_db

def add_movie(title, genre):
    movie = {"id": len(movies_db) + 1, "title": title, "genre": genre}
    movies_db.append(movie)
    return movie

def get_movie_by_id(movie_id):
    return next((m for m in movies_db if m["id"] == movie_id), None)

favorites = []

def add_to_favorites(movie_id):
    favorites.append(movie_id)
    return favorites

