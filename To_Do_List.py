tasks = []

def select_language():
    while True:
        language = input("\nchoose language:\n\n[1] russian\n[2] english\n[3] german\n[4] exit\n\nyour answer: ")

        if language == "1":
            main_ru()
        elif language == "2":
            main_en()
        elif language == "3":
            main_de()
        elif language == "4":
            exit()
        else:
            print("\ninvalid choice\n")
            select_language()

def delete_task_ru():
    task = input("\nвведите задачу для удаления: ")
    if task in tasks:
        tasks.remove(task)
        print("\nзадача удалена")
    else:
        print("\nзадача не найдена\n")

def new_task_ru():
    while True:
        task = input("\nчтобы выйти из меню добавления задач напишите ""exit""\nвведите задачу: ")
        if task == "exit":
            break
        else:
            tasks.append(task)

def show_tasks_ru():
    print("\nваши задачи:\n\n",tasks)
    input("\nнажмите ENTER чтобы продолжить\n")

def main_ru():
    print("\nвы выбрали русский язык")
    while True:
        choice = input("\nвыбери что ты хочешь сделать:\n\n[1] добавить задачи\n[2] показать задачи\n[3] удалить задачу\n\nваш ответ: ")
        if choice == "1":
            new_task_ru()
        else:
            if choice == "2":
                show_tasks_ru()
            else:
                if choice == "3":
                    delete_task_ru()
                else:
                    break

def delete_task_en():
    task = input("\nenter the task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print("\ntask deleted")
    else:
        print("\ntask not found\n")

def new_task_en():
    while True:
        task = input('\ntype "exit" to leave the task creation menu\nenter the task: ')
        if task == "exit":
            break
        tasks.append(task)

def show_tasks_en():
    print("\nyour tasks:\n\n",tasks)
    input("\npress ENTER to continue\n")

def main_en():
    print("\nyou chose English")
    while True:
        choice = input("\nchoose what you want to do:\n\n[1] create a task\n[2] show tasks\n[3] delete a task\n\nyour answer: ")
        if choice == "1":
            new_task_en()
        else:
            if choice == "2":
                show_tasks_en()
            else:
                if choice == "3":
                    delete_task_en()
                else:
                    break

def delete_task_de():
    task = input("\ngib die Aufgabe zum Löschen ein: ")
    if task in tasks:
        tasks.remove(task)
        print("\nAufgabe gelöscht")
    else:
        print("\nAufgabe nicht gefunden\n")

def new_task_de():
    while True:
        task = input('\nzum Verlassen des Aufgabenmenüs "exit" eingeben\ngib die Aufgabe ein: ')
        if task == "exit":
            break
        tasks.append(task)

def show_tasks_de():
    print("\nIhre Aufgaben:\n\n",tasks)
    input("\ndrücken Sie ENTER, um fortzufahren\n")

def main_de():
    print("\nSie haben Deutsch gewählt")
    while True:
        choice = input("\nwählen Sie, was Sie tun möchten:\n\n[1] eine Aufgabe erstellen\n[2] Aufgaben anzeigen\n[3] eine Aufgabe löschen\n\nIhre Antwort: ")
        if choice == "1":
            new_task_de()
        else:
            if choice == "2":
                show_tasks_de()
            else:
                if choice == "3":
                    delete_task_de()
                else:
                    break

select_language()
