from methods import Methods
import sys

controller = Methods()
while True:
    print('1 - Добавить заметку \n2 - Показать заметку \n3 - Редактировать заметку'
        '\n4 - Удалить заметку \n5 - Вывести все заметки \n6- Выход')
    
    try:
        userChoice = int(input())
        if userChoice == 1:
            controller.newNote()
        elif userChoice == 2:
            ans = controller.getAnswerFromConsole()
            if ans == "s":
                controller.getNotes()
            else: 
                controller.printNote(int(ans))
        elif userChoice== 3:
            controller.editNote()
        elif userChoice== 4:
            ans = controller.getAnswerFromConsole()
            if ans == "s":
                controller.getNotes()
            else:
                controller.deleteNote(int(ans))
        elif userChoice== 5:
            controller.getNotes()
        elif userChoice== 6:
            sys.exit()
    except ValueError:
        print("Введен некорректный номер контекстного меню")