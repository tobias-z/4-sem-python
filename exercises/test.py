
class User:
    username: str
    password: str

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_string(self):
        print("username: {username} {password}",
              (self.username, self.password))

    def message(self):
        return "{self.username} {self.password}"


if __name__ == "__main__":
    user = User("hello", "there")
    user.to_string()
    print(user.message())
