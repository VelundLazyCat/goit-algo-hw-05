'''
Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок
за допомоги декораторів.

Вимоги до завдання:
Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error.
Цей декоратор відповідає за повернення користувачеві повідомлень типу "Enter user name",
"Give me name and phone please" тощо.
Декоратор input_error повинен обробляти винятки, що виникають у функціях - handler і це винятки: KeyError,
ValueError, IndexError. Коли відбувається виняток декоратор повинен повертати відповідну відповідь 
користувачеві. Виконання програми при цьому не припиняється.
'''


class MyCustomError(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except MyCustomError as f:
            return f
        except KeyError as k:
            print(k)
        except IndexError:
            return "Nust be one phone number"

    return inner


@input_error
def say_hello(contacts, *args):
    return "How can I help you?"


@input_error
def good_bye(contacts, *args):
    return "Good bye!\nPress Enter please..."


@input_error
def add_contact(contacts, *args):
    name, phone = args
    if name in contacts:
        raise MyCustomError('We have a problem. This contact alredy exist')
    contacts[name] = phone
    return f'New contact: {name}, phone:{phone} added'


@input_error
def do_change(contacts, *args):
    name, phone = args
    contacts[name] = phone
    return f'Contact {name} has been changed'


@input_error
def show_phone(contacts, *args):
    name = args[0]
    return f' Phone of {name} is: {contacts[name]}'


@input_error
def show_all(contacts, *args):
    result = ''
    for key, value in contacts.items():
        result += f"{key}:   {value}\n"
    return result


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def unknown_comand():
    raise KeyError('Command unknown! Maybe try else?')


def get_handler(command):
    return COMMANDS[command]


COMMANDS = {'hello': say_hello,  'add': add_contact,
            'change': do_change, 'phone': show_phone,
            'all': show_all,     'close': good_bye,
            'exit': good_bye,
            }


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        if COMMANDS.get(command):
            result = get_handler(command)(contacts, *args)
            print(result)
            if 'bye' in str(result):
                input()
                break
        else:
            unknown_comand()


if __name__ == "__main__":
    main()

'''
Список тестових команд:
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356 
Enter a command:
'''
