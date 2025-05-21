from enum import IntEnum
from typing import Protocol

from dbconnection import DBConnection


class UserTypes(IntEnum):
    STUDENT = 1
    TEACHER = 2


class Success[T](Protocol):
    """
    A callable that takes a string input and returns a tuple of a boolean indicating success or failure.
    """
    def __call__(self, string_input: str) -> tuple[bool, T | None]: ...


class Jupiter:
    def __init__(self, database: str) -> None:
        self.connection: DBConnection = DBConnection(database)
        self.user_type: UserTypes | None = None
        self.user_id: int | None = None
        self.successes: Successes = Successes(self)

    @staticmethod
    def __input_until_success[T](input_message: str, error_message: str, success: Success[T]) -> T:
        user_input: str = input(input_message).strip()
        successful, formatted_input = success(user_input)

        while not successful or formatted_input is None:
            print(error_message)
            user_input: str = input(input_message).strip()
            successful, formatted_input = success(user_input)

        return formatted_input

    def login(self):
        print("Are you a student or a teacher?")
        print("1: Student")
        print("2: Teacher")

        self.user_type = self.__input_until_success(
            "Enter choice: ",
            "Invalid choice!",
            self.successes.usertype_success,
        )

        self.user_id = self.__input_until_success(
            "Enter id: ",
            "Invalid id!",
            self.successes.id_success,
        )


class Successes:
    def __init__(self, jupiter: Jupiter):
        self.jupiter = jupiter

    @staticmethod
    def usertype_success(string_input: str) -> tuple[bool, UserTypes | None]:
        if not string_input.isdigit():
            return False, None

        integer_input: int = int(string_input)

        if integer_input not in UserTypes:
            return False, None

        return True, UserTypes(integer_input)

    def id_success(self, string_input: str) -> tuple[bool, int | None]:
        if self.jupiter.user_id is None:
            return False, None
        
        if self.jupiter.user_type not in UserTypes:
            return False, None
        
        if self.jupiter.user_type is UserTypes.STUDENT:
            query = "SELECT id FROM students WHERE id = %s"
        else:
            query = "SELECT id FROM teachers WHERE id = %s"

        result = self.jupiter.connection.query(query, (string_input,))
        
        if result is None:
            return False, None
        
        return True, result[0][0]
            