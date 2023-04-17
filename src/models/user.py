class User:
    """A user holds a first name, last name, handle, and a user id"""

    def __init__(self, fname: str, lname: str, email: str, username: str, user_id: int) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.username = username
        self.user_id = user_id

    def set_username(self, new_username):
        self.username = new_username

    def set_password(self, new_pass):
        self.password = new_pass

    def set_fname(self, new_fname):
        self.fname = new_fname

    def set_lname(self, new_lname):
        self.lname = new_lname
