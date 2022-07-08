from application.salary import *
from application.db.people import *


def main():
    while True:
        command = input('Введите команду:')
        if command == 'c':
            calculate_salary()
        if command == 'g':
            get_employees()
        if command == 'e':
            break


if __name__ == '__main__':
    main()