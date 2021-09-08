import string


class TextContainer:
    def __init__(self, text: str) -> None:
        self.text = text

    def get_amount_of_words(self):
        return len(self.text.split(" "))

    def get_amount_of_chars(self):
        return len(self.text)

    def get_amount_of_letters(self):
        return len([char for char in self.text if char.lower() in string.ascii_letters])


if __name__ == "__main__":
    text = TextContainer("Hello there how are you doing 12 321")
    print(text.get_amount_of_words())
    print(text.get_amount_of_chars())
    print(text.get_amount_of_letters())
