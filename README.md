# **Консольное приложение для работы с контактами**

# Описание
В данном репозитории расположено консольное приложение, позволяющее работать со списком контактов.
Оно состоит из:
1. Модуля управления - `main.py`, загружающего, сохраняющего и публикующего в консоль контакты.
2. Его дочернего модуля функций (управляющих команд) - `commands.py`, изменяющих состояние списка контактов.
3. Создаваемого/изменяемого в процессе списка контактов - `contacts.json`. Создавать этот файл вручную не требуется.
4. Архива контактов - `contacts_archive.json`, сугубо вспомогательного списка контактов, данные из которого могут быть использованы для проверки функционала в файле `contacts.json`.

# Инструкция
1. Работа с программой начинается с её запуска из модуля `main.py`.
2. Далее, в целом, достаточно следовать консольной инструкции, вызывая предлагаемые команды:
```Bash
    add name       добавления контакта
    edit name      редактирования контакта name
    remove name    удаления контакта
    exit           выхода из программы
```

# Особенности и уязвимости
1. Во все поля списка контактов можно ввести любые символы. Условно считаем, что это записная книжка,
без проверки типов. Однако, вместе с тем, программа из записываемых телефонов удаляет пробелы.
2. Следствием пункта 1, является отсутствие проверок на формат телефона, электронной почты.