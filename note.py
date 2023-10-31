from datetime import datetime

class Note(object):
    id = None
    title = ""
    body = ""
    
    def __init__(self):
        self.title = ""
        self.dateOfCreation = datetime.now().strftime('%Y-%m-%d %H:%M')

    def __setTitle__(self):
        self.title = input("Введите название заметки")

    def __setBody__(self):
        self.body = input("Введите текст заметки")

    def getTitle(self):
        return self.title    