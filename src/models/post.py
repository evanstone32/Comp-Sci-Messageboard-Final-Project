class Post:
    """A post holds a title, text, and post author"""

    def __init__(self, title: str, text: str, author: int) -> None:
        self.title = title
        self.text = text
        self.author = author
