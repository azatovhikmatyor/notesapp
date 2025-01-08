from __future__ import annotations

from typing import Union
from datetime import datetime

class Note:

    def __init__(self, id: int, text: str, created_date: Union[datetime, str]) -> None:
        self.id = id
        self.text = text
        self.created_date = created_date

    @classmethod
    def from_dict(cls, values: dict[str, str]) -> Note:
        note_id = values['id']
        text = values['text']
        created_date = values['created_date']
        return cls(note_id, text, created_date)
    
    @classmethod
    def from_tuple(cls, values: tuple[str, str, str]) -> Note:
        pass

    def as_dict(self) -> dict[str, str]:
        pass

    def as_tuple(self) -> tuple[str, str, str]:
        pass

    def __str__(self):
        return f'Note(id={self.id}, text={self.text!r}, created_date={self.created_date!r})'

# n1 = Note.from_dict({'id': 1, 'text': '', 'created_date': ''})
# print(type(n1))

if __name__ == '__main__':
    n1 = Note(1, 'text', '')
    n2 = Note.from_dict({'id': 1, 'text': '', 'created_date': ''})
    print(n1)
    print(n2)