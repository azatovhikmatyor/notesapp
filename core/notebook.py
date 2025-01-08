from typing import List
from datetime import datetime

from .note import Note
from .storage import Storage



class Notebook:

    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.notes = self.__storage.load()

    def add_note(self, note: Note) -> None:
        """Add given Note object into existing list of notes"""
        if note :
            self.notes.append(note)
            self.__storage.save(self.notes)
        else: raise ValueError("Note cannot be None")

    def update_note(self, note: Note) -> None:

        for item in self.notes:
            if item.id == note.id:
              item.text = note.text
              self.__storage.save(self.notes)
              return


    def delete_note(self, note_id: int) -> None:
        for item in self.notes:
            if item.id == note_id:
                self.notes.remove(item)
                self.__storage.save(self.notes)
                return

    def get_notes(self) -> List[Note]:
        return self.notes

    
    def get_note(self, note_id: int) -> Note:
        for item in self.notes:
            if item.id == note_id:
                return item







if __name__ == '__main__':
    notebook1 = Notebook()
    notes = notebook1.notes
    print(notes)