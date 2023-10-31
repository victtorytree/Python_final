import datetime
import json
from note import Note


class Methods():
    data = {}
    data["notes"] = []
    
    def __init__(self):
        self.name = "new Textbook"
        self.notes = []

    def newNote(self):
        a = Note()
        a.id = len(self.data["notes"])
        a.title = input("Введите название заметки: ")
        a.body = input("Введите текст заметки: ")
        newLine = {"number": str(a.id), "title": a.title, "body": a.body, "date": str(a.dateOfCreation)}
        self.data['notes'].append(newLine)  
        with open('notebook.txt', 'w', encoding="utf-8") as notebook:
            json.dump(self.data, notebook, indent=8)
        print("Заметка добавлена")


    def editNote(self):
        y = input("Введите номер заметки ")
        for item in self.data["notes"]:
            if item["number"] == y:
                item["title"] = input("Введите новое название заметки ")
                item["body"] = input("Введите новый текст заметки ")

    def printNote(self, index):
        ans = self.data["notes"][index]
        if(ans):
            print(ans)
        else:
            print("Заметка не найдена")

    def getNotes(self):
        text = json.dumps(self.data["notes"], indent=6)
        print(text)

    def deleteNote(self, index):
        for item in self.data["notes"]:
            if item["number"] == str(index):
                self.data["notes"].remove(item)
        self.getNotes()
        print("заметка удалена")
    
    def getAnswerFromConsole(self):
        res = input("Введите номер заметки, либо s - список всех заметок ")
        return res