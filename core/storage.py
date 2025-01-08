from abc import ABC, abstractmethod
from typing import List, Dict

from .note import Note

class Storage(ABC):

    @abstractmethod
    def save(self, notes: List[Note]) -> None:
        pass

    @abstractmethod
    def load(self) -> List[Note]:
        pass

    @property
    @abstractmethod
    def info(self) -> Dict[str, str]:
        pass


class JSONFile(Storage):

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def save(self, notes: List[Note]) -> None:
        # NOTE: demo implementation
        print(f"{len(notes)} notes saved into file {self.file_name}")

    def load(self) -> List[Note]:
        # NOTE: demo implementation
        return [Note(1, "First Note", "2024-12-12"), Note(2, "Second Note", "2024-12-12")]

    def info(self) -> Dict[str, str]:
        return {'file_name': self.file_name}
    

class CSVFile(Storage):

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def save(self, notes: List[Note]) -> None:
        # NOTE: demo implementation
        print(f"{len(notes)} notes saved into file {self.file_name}")

    def load(self) -> List[Note]:
        # NOTE: demo implementation
        return [Note(1, "First Note", "2024-12-12"), Note(2, "Second Note", "2024-12-12")]

    def info(self) -> Dict[str, str]:
        return {'file_name': self.file_name}
    

