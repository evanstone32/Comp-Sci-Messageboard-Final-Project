from src.models.post import Post

_post_repo = None


def get_post_repository():
    global _post_repo

    class PostRepository:
        """In memory database which is a simple list of movies"""

        def __init__(self) -> None:
            self._db: list[Post] = []

        def get_all_posts(self) -> list[post]:
            """Simply return all movies from the in-memory database"""
            return self._db

        # def get_post_by_title(self, title: str) -> Post | None:
        #     """Get a single movie by its title or None if it does not exist"""
        #     # Perform a linear search through the in-memory database
        #     for post in self._db:
        #         # If the movie title matches, return the movie
        #         if movie.title == title:
        #             return movie
        #     # If we made it this far, no movies matched so return None
        #     return None

        # def create_movie(self, title: str, director: str, rating: int) -> Movie:
        #     """Create a new movie and return it"""
        #     # Create the movie instance
        #     movie = Movie(title, director, rating)
        #     # Save the instance in our in-memory database
        #     self._db.append(movie)
        #     # Return the movie instance
        #     return movie

    # Singleton to be used in other modules
    if _post_repo is None:
        _post_repo = PostRepository()

    return _post_repo
