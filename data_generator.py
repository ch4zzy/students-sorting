from dataclasses import dataclass
from faker import Faker
from typing import Literal


fake = Faker('uk_UA')


@dataclass
class Student:
    name: str
    surname: str
    patronymic: str
    phone: str


def generate_students_data(num_students: int):
    students = []
    for _ in range(num_students):
        full_name = fake.full_name(gender='M' if fake.random_element(['M', 'F']) == 'M' else 'F')
        surname, name, patronymic = full_name.split()
        phone = fake.phone_number()
        students.append(Student(name=name, surname=surname, patronymic=patronymic, phone=phone))
    return students


def save_students_to_csv(filename: str, students):
    import csv
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Surname', 'Name', 'Patronymic', 'Phone'])
        for student in students:
            writer.writerow([student.surname, student.name, student.patronymic, student.phone])
