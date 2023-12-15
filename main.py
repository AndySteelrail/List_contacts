import json
from commands import add_contact, edit_contact, remove_contact


def load():
    try:
        with open("contacts.json", "r", encoding="utf-8") as doc:
            contacts = json.load(doc)
            return contacts
    except:
        return {}

def save(contacts):
    with open("contacts.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(contacts, indent = 2))

def print_contacts(contacts):
    if contacts == {}:
        print("Контактов пока нет\n")
        return 
    for name, info in contacts.items():
        print(f"Контакт: {name}")
        print(f"Телефоны: {', '.join(map(str, info['phones']))}")
        print(f"День рождения: {info['birthday']}")
        print(f"email: {info['email']}")
        print()

main_message = "Введите команду для:\n" + \
    "add name       добавления контакта" + "\n" + \
    "edit name      редактирования контакта name" + "\n" + \
    "remove name    удаления контакта" + "\n" + \
    "exit           выхода из программы" + "\n\n"

while True:
    contacts = load()
    print_contacts(contacts)

    user_input = input(main_message)
    user_input_words = user_input.split()
    command = user_input_words[0]
    name = " ".join(user_input_words[1:])

    if command == "add":
        add_contact(contacts, name)
    elif command == "edit":
        edit_contact(contacts, name)
    elif command == "remove":
        remove_contact(contacts, name)
    elif command == "exit":
        break
    else:
        print("Вы ввели неверную комманду!")

    save(contacts)