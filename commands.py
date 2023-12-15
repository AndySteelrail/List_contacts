def add_contact(contacts, name):
    if name in contacts:
        print(f"Контакт '{name}' уже существует. Используйте другое имя.")
        return
    if name == "":
        print(f"Вы вводите контакт с пустым именем. Используйте другое имя.")
        return

    phones = input("Введите телефоны через пробел: ").split()
    phones = [phone.strip() for phone in phones]
    birthday = input("Введите день рождения: ")
    email = input("Введите email: ")
    
    new_contact = {"phones": phones,
                   "birthday": birthday,
                   "email": email}
    contacts[name] = new_contact

    print()
    print(f"Контакт '{name}' создан.")

    return contacts

def get_input_with_default(message, default):
    user_input = input(message)
    if user_input != "":
        return user_input
    else:
        return default

def edit_contact(contacts, name):
    if name not in contacts:
        print(f"Контакт '{name}' не существует. Используйте другое имя.")
        return contacts

    print("Поля контакта оставленные без заполнения, сохранят свои значения")
    contact = contacts[name]

    updates_phones = input("Введите телефоны через пробел: ").split() or contact["phones"]
    updates_birthday = get_input_with_default("Введите день рождения: ", contact["birthday"])
    updates_email = get_input_with_default("Введите email: ", contact["email"])

    updates_contact = {"phones": updates_phones,
                       "birthday": updates_birthday,
                       "email": updates_email}
    contacts[name] = updates_contact

    print(f"Контакт '{name}' обновлён.")
    return contacts

def remove_contact(contacts, name):
    if name not in contacts:
        print(f"Контакт '{name}' не существует. Используйте другое имя.")
        return

    del contacts[name]
    
    print()
    print(f"Контакт '{name}' удалён.")

    return contacts