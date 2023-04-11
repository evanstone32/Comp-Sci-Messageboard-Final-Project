from src.models.movie import Movie


def test_movie_model():
    movie = Movie('Star Wars', 'George Lucas', 5)

    assert type(movie) == Movie
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5
