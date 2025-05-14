from enum import IntEnum
from dbconnection import DBConnection


class UserTypes(IntEnum):
    STUDENT = 1
    TEACHER = 2


class Jupiter:
    def __init__(self, database):
        self.connection = DBConnection(database)
        self.user_type: UserTypes | None = None

    def login(self):
        print("Are you a student or a teacher?")
        print("1: Student")
        print("2: Teacher")
        user_type = input("Enter choice: ").strip()
        user_type = int(user_type) if user_type.isdigit() else None

        while user_type not in UserTypes:
            print("Invalid choice!")
            user_type = input("Enter choice: ").strip()
            user_type = int(user_type) if user_type.isdigit() else None

        self.user_type = UserTypes(user_type)

