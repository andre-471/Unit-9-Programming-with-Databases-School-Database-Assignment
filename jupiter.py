from enum import IntEnum
from typing import Protocol

from dbconnection import DBConnection


class UserTypes(IntEnum):
    STUDENT = 1
    TEACHER = 2


class ConvertsType[T](Protocol):
    def __call__(self, string_input: str) -> tuple[bool, T | None]: ...


def input_until_success[T](input_message: str, error_message: str, convert_type: ConvertsType[T]) -> T:
    user_input: str = input(input_message).strip()
    successful, formatted_input = convert_type(user_input)

    while not successful or formatted_input is None:
        print(error_message)
        user_input: str = input(input_message).strip()
        successful, formatted_input = convert_type(user_input)

    return formatted_input


class Jupiter:
    def __init__(self, database: str) -> None:
        # self.connection: DBConnection = DBConnection(database)
        self.user_type: UserTypes | None = None

    def login(self):
        print("Are you a student or a teacher?")
        print("1: Student")
        print("2: Teacher")

        self.user_type = input_until_success(
            "Enter choice: ",
            "Invalid choice!",
            lambda string_input: (True, UserTypes(integer_input))
            if string_input.isdigit() and (integer_input := int(string_input)) in UserTypes
            else (False, None)
        )

        if self.user_type is UserTypes.STUDENT:
            pass
        else:
            pass
