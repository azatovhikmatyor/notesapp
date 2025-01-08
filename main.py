import sys

from core import Note, Notebook, JSONFile, CSVFile
from datetime import datetime

class ConsoleApp:
    def __init__(self):
        self.__notebook = Notebook(JSONFile('notes.json'))
        self.commands = {
            '1': self.__show_notes,
            '2': self.__show_note,
            '3': self.__add_note,
            '4': self.__update_note,
            '5': self.__delete_note,
            'm': self.__show_menu,
            'q': sys.exit
        }

    def run(self):
        self.__show_menu()
        while True:
            choice = input('Choice: ')

            command = self.commands.get(choice.lower())
            if command:
                command()
            else:
                print('Invalid choice')


    def __show_notes(self) -> None:
        all_notes = self.__notebook.get_notes()
        for note in all_notes:
            print(note)

    def __show_note(self) -> None:
        note_id = input("Enter note id: ")
        note = self.__notebook.get_note(note_id)
        print(note)
    
    def __add_note(self):
        note_id = input("Enter note id: ")
        text = input("Enter new text: ")
        created_date = datetime.now()
        note = Note(note_id, text, created_date)
        self.__notebook.add_note(note)


    def __update_note(self) -> None:
        note_id = input("Enter note id: ")
        new_text = input("Enter new text: ")
        self.__notebook.update_note(
            Note(note_id, new_text, 
                 datetime.now() # NOTE: datetime will note be updated anyway
            )
        )

    def __delete_note(self) -> None:
        note_id = input("Enter note id: ")
        self.__notebook.delete_note(note_id)\
        
    def __show_menu(self):
        print("""
1. Show All Notes
2. Show Note Details
3. Write New Note
4. Update Existing Note
5. Delete Existing Note
m. Show Menu Again
q. Quit Application
""")


if __name__ == '__main__':
    app = ConsoleApp()
    app.run()