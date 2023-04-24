from src.models.user import User

_user_repo = None


def get_user_repository():
    global _user_repo

    class UserRepository:
        """In memory database which is a simple list of movies"""

        def __init__(self) -> None:
            self._db: list[User] = []

        def get_all_users(self) -> list[User]:
            """Simply return all movies from the in-memory database"""
            return self._db

        def get_user_by_username(self, username) -> User | None:
            for user in self._db:
                # If the movie title matches, return the movie
                if user.username == username:
                    return user
            # If we made it this far, no movies matched so return None
            return None

        # def get_post_by_title(self, title: str) -> Post | None:
        #     """Get a single movie by its title or None if it does not exist"""
        #     # Perform a linear search through the in-memory database
        #     for post in self._db:
        #         # If the movie title matches, return the movie
        #         if movie.title == title:
        #             return movie
        #     # If we made it this far, no movies matched so return None
        #     return None

        def get_new_user_num(self):
            return len(self._db)

        def create_user(self, fname: str, lname: str, email: str, username: str, user_id: int) -> User:
            ''' Create a new user and return it'''
            user = User(fname, lname, email, username, user_id)

            self._db.append(user)

            return user

        # def create_movie(self, title: str, director: str, rating: int) -> Movie:
        #     """Create a new movie and return it"""
        #     # Create the movie instance
        #     movie = Movie(title, director, rating)
        #     # Save the instance in our in-memory database
        #     self._db.append(movie)
        #     # Return the movie instance
        #     return movie

    # Singleton to be used in other modules
    if _user_repo is None:
        _user_repo = UserRepository()

    return _user_repo
