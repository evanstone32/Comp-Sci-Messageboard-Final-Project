class Movie:
    """A movie holds a title, director, and rating"""

    def __init__(self, title: str, director: str, rating: int) -> None:
        self.title = title
        self.director = director
        self.rating = rating
