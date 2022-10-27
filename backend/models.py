from typing import Union
from pydantic import BaseModel


class Book(BaseModel):
    book_id: Union[str, None]
    title: str
    url: str
    text: list
    emotions: list
    hate_speech: list
    author: str
    main_img: str


class UserText(BaseModel):
    text: str

class UserUrlBook(BaseModel):
    title: Union[str, None]
    text: list
    emotions: list
    hate_speech: list