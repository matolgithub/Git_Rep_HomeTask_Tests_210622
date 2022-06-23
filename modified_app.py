documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

# function 1
def check_document_existance(user_doc_number):
    doc_founded = False
    for current_document in documents:
        doc_number = current_document['number']
        if doc_number == user_doc_number:
            doc_founded = True
            break
    return doc_founded

# function 2
def get_doc_owner_name(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                return current_document['name']

# function 3
def get_all_doc_owners_names():
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)

# function 4
def remove_doc_from_shelf(doc_number):
    for directory_number, directory_docs_list in directories.items():
        if doc_number in directory_docs_list:
            directory_docs_list.remove(doc_number)
            break

# function 5
def add_new_shelf(shelf_number, bool=True):
    if not shelf_number:
        bool = False
    if shelf_number not in directories.keys():
        directories[shelf_number] = []
        return shelf_number, bool
    return shelf_number, bool

# function 6
def append_doc_to_shelf(doc_number, shelf_number):
    add_new_shelf(shelf_number)
    directories[shelf_number].append(doc_number)
    return directories

# function 7
def delete_doc(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for current_document in documents:
            doc_number = current_document['number']
            if doc_number == user_doc_number:
                documents.remove(current_document)
                remove_doc_from_shelf(doc_number)
                return directories

# function 8
def get_doc_shelf(user_doc_number):
    doc_exist = check_document_existance(user_doc_number)
    if doc_exist:
        for directory_number, directory_docs_list in directories.items():
            if user_doc_number in directory_docs_list:
                return directory_number, directories

# function 9
def move_doc_to_shelf(user_doc_number, user_shelf_number):
    remove_doc_from_shelf(user_doc_number)
    append_doc_to_shelf(user_doc_number, user_shelf_number)
    res_move_text = f'Документ номер "{user_doc_number}" был перемещен на полку номер "{user_shelf_number}"'
    return  res_move_text

# function 10
def show_document_info(document):
    doc_type = document['type']
    doc_number = document['number']
    doc_owner_name = document['name']
    show_doc_text = f'{doc_type} "{doc_number}" "{doc_owner_name}"'
    return show_doc_text

# function 11
def show_all_docs_info():
    for current_document in documents:
        show_document_info(current_document)

# function 12
def add_new_doc(new_doc_type, new_doc_number, new_doc_owner_name, new_doc_shelf_number):
    new_doc = {
        "type": new_doc_type,
        "number": new_doc_number,
        "name": new_doc_owner_name
    }
    documents.append(new_doc)
    append_doc_to_shelf(new_doc_number, new_doc_shelf_number)
    return new_doc_shelf_number, new_doc_number

# function 13
def secretary_program_start(user_command):
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    # print(
    #     'Вас приветствует программа помощник!\n',
    #     '(Введите help, для просмотра списка поддерживаемых команд)\n'
    # )
    while True:
        if user_command == 'p':
            owner_name = get_doc_owner_name()
            choice_result_text = f'Владелец документа - {owner_name}'
        elif user_command == 'ap':
            uniq_users = get_all_doc_owners_names()
            choice_result_text = f'Список владельцев документов - {uniq_users}'
        elif user_command == 'l':
            all_docs = show_all_docs_info()
            choice_result_text = f'Все документы {all_docs}'
        elif user_command == 's':
            directory_number = get_doc_shelf()
            choice_result_text = f'Документ находится на полке номер {directory_number}'
        elif user_command == 'a':
            new_doc_shelf_number, new_doc_number = add_new_doc()
            choice_result_text = f'На полку "{new_doc_shelf_number}" добавлен новый документ: "{new_doc_number}"'
        elif user_command == 'd':
            doc_number, deleted = delete_doc()
            if deleted:
                choice_result_text = f'Документ с номером "{doc_number}" был успешно удален'
        elif user_command == 'm':
            res_move_text = move_doc_to_shelf()
            choice_result_text = f'{res_move_text}'
        elif user_command == 'as':
            shelf_number, added = add_new_shelf()
            if added:
                choice_result_text = f'Добавлена полка "{shelf_number}"'
        elif user_command == 'help':
            choice_result_text = f'{secretary_program_start.__doc__}'
        elif user_command == 'q':
            break
    return choice_result_text


if __name__ == '__main__':
    secretary_program_start()