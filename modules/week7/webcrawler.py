from typing import List
from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor

CPHBUSINESS_URL = "https://www.cphbusiness.dk/"


class Crawler:
    def __init__(self) -> None:
        self.links_used: List[str] = []

    def crawl_link(self, link):
        the_link = link.get("href")
        if the_link in self.links_used:
            return self.links_used
        self.links_used.append(the_link)
        return self.get_all_links(the_link)

    def get_all_links(self, url: str) -> List[str]:
        if len(self.links_used) == 20:
            return self.links_used
        res = requests.get(url)
        res.raise_for_status()
        html = BeautifulSoup(res.text, "html.parser")
        all_links = html.select("a")
        with ThreadPoolExecutor(len(all_links)) as ex:
            return list(ex.map(self.crawl_link, all_links))


if __name__ == "__main__":
    crawler = Crawler()
    print(crawler.get_all_links(CPHBUSINESS_URL))
