from typing import List
from typing_extensions import TypedDict

class Source(TypedDict):
    id: int
    name: str

class Article(TypedDict):
    source: Source
    author: str
    title: str
    description: str
    url: str
    urlToImage: str
    publishedAt: str
    content: str

class Feed(TypedDict):
    status: str
    totalResults: int
    articles: List[Article]