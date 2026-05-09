import json


def save_data(students):

    with open("students.json", "w") as file:
        json.dump(students, file)

    print("\nData Saved Successfully!")


def load_data():

    try:
        with open("students.json", "r") as file:
            students = json.load(file)

    except FileNotFoundError:
        students = {}

    return students