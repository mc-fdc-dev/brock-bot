from aiohttp import ClientSession
from bs4 import BeautifulSoup

from typing import TypedDict


class NewsItem(TypedDict):
    title: str
    date: str


class News:
    URL = "https://bocchi.rocks/news/"
    def __init__(self, session: ClientSession) -> None:
        self.__session = session

    async def fetch_news(self) -> list:
        async with self.__session.get(self.URL) as res:
            html = await res.text()
            soup = BeautifulSoup(html, "html.parser")
            news_blocks = soup.find_all("li", class_="js-newsdetail")
            news_items: list[NewsItem] = []
            for news_block in news_blocks:
                news_items.append(
                    {
                        "title": news_block.find("h3").text,
                        "date": (
                            news_block.find("span", class_="date").text
                                .replace(" ", "")
                        )
                    }
                )
            return news_items


if __name__ == "__main__":
    import asyncio


    async def main() -> None:
        async with ClientSession() as session:
            news = News(session)
            print(await news.fetch_news())
    
    asyncio.run(main())