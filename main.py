import locale
from data_generator import save_students_to_csv, generate_students_data
import csv


locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')


def print_students_from_csv(filename: str) -> None:
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def print_students(students):
    for student in students:
        print(f"{student.surname} {student.name} {student.patronymic}, {student.phone}")


def sort_menu(students):
    while True:
        print("\nОберіть спосіб сортування:")
        print("1. За прізвищем")
        print("2. За ім'ям")
        print("3. За по батькові")
        print("4. За номером телефону")
        print("5. Зберегти відсортованих студентів у CSV файл")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            sorted_students = sorted(students, key=lambda x: locale.strxfrm(x.surname))
            print("\nСортування за прізвищем:")
            print_students(sorted_students)
        elif choice == '2':
            sorted_students = sorted(students, key=lambda x: locale.strxfrm(x.name))
            print("\nСортування за ім'ям:")
            print_students(sorted_students)
        elif choice == '3':
            sorted_students = sorted(students, key=lambda x: locale.strxfrm(x.patronymic))
            print("\nСортування за по батькові:")
            print_students(sorted_students)
        elif choice == '4':
            sorted_students = sorted(students, key=lambda x: locale.strxfrm(x.phone))
            print("\nСортування за номером телефону:")
            print_students(sorted_students)
        elif choice == '5':
            filename = input("Введіть ім'я файлу для збереження (наприклад, 'sorted_students.csv'): ")
            save_students_to_csv(filename, sorted_students)
            print(f"Відсортовані студенти збережені у файл {filename}")
        elif choice == '0':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


def main():
    students = generate_students_data(10)
    save_students_to_csv("students.csv", students)  
    print("\nПочатковий список студентів з файлу:")
    print_students_from_csv("students.csv") 
    sort_menu(students)  


if __name__ == "__main__":
    main()
