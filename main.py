from application.salary import calculate_salary
from application.db.people import get_employees


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