from dataclasses import dataclass
from faker import Faker
import csv


@dataclass
class Student:
    name: str
    surname: str
    patronymic: str
    phone: str


def generate_patronymic(fake, gender):
    first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
    if gender == 'male':
        return first_name + "ович"
    else:
        return first_name + "івна"


def generate_student_data(fake: Faker) -> Student:
    gender = fake.random_element(elements=("male", "female"))
    name = fake.first_name_male() if gender == "male" else fake.first_name_female()
    surname = fake.last_name()
    patronymic = generate_patronymic(fake, gender)
    phone = fake.phone_number()
    return Student(name, surname, patronymic, phone)


def generate_students_data(count: int) -> list[Student]:
    fake = Faker("uk_UA")
    students = [generate_student_data(fake) for _ in range(count)]
    return students


def save_students_to_csv(filename: str, students: list[Student]) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Surname", "Patronymic", "Phone"])
        for student in students:
            writer.writerow([student.name, student.surname, student.patronymic, student.phone])
