from typing import List
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing


class NotFoundException(Exception):
    pass


class TextComparer:
    def __init__(self, urls: List[str]) -> None:
        self.urls = urls
        self.filenames = [f"files/books/{url.split('/')[-1]}" for url in urls]

    def multi_download(self):
        with ThreadPoolExecutor(len(self.urls)) as ex:
            ex.map(self.download, self.urls, self.filenames)

    def download(self, url: str, filename: str):
        res = requests.get(url)
        if res.status_code is not 200:
            raise NotFoundException(f"url: {url} was not found")
        with open(filename, "wb") as file:
            for chuck in res.iter_content(chunk_size=1024):
                file.write(chuck)

    def __iter__(self):
        self.currentNumber = 0
        return self

    def __next__(self):
        if self.currentNumber >= len(self.filenames):
            raise StopIteration()
        item = self.filenames[self.currentNumber]
        self.currentNumber += 1
        return item

    def urllist_generator(self):
        for url in self.urls:
            yield url

    def avg_vowels(self, filename):
        VOWELS = "aeiou"
        vovel_count = 0
        letter_count = 0
        with open(filename, "r") as file:
            for line in file:
                for word in line.split(" "):
                    for letter in word:
                        letter_count += 1
                        if letter.lower() in VOWELS:
                            vovel_count += 1
        avg_in_percent = (vovel_count / letter_count) * 100
        return (filename.split("/")[-1], avg_in_percent)

    def hardest_read(self):
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.avg_vowels, self.filenames)
        return dict(
            item for item in sorted(list(res), key=lambda book: book[1], reverse=True)
        )
