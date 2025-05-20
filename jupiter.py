from enum import IntEnum
from typing import Protocol

from dbconnection import DBConnection


class UserTypes(IntEnum):
    STUDENT = 1
    TEACHER = 2


class Success[T](Protocol):
    def __call__(self, string_input: str, **kwargs) -> tuple[bool, T | None]: ...


class Jupiter:
    def __init__(self, database: str) -> None:
        # self.connection: DBConnection = DBConnection(database)
        self.user_type: UserTypes | None = None
        self.user_id: int | None = None

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
            self.Successes.until_valid_usertype,
        )

        if self.user_type is UserTypes.STUDENT:
            self.user_id = self.__input_until_success(
                "Enter id: "
                "Invalid id!"
            )
        else:
            pass

    class Successes:
        @staticmethod
        def until_valid_usertype(string_input: str, **kwargs) -> tuple[bool, UserTypes | None]:
            if not string_input.isdigit():
                return False, None

            integer_input: int = int(string_input)

            if integer_input not in UserTypes:
                return False, None

            return True, UserTypes(integer_input)

        @staticmethod
        def until_valid_id(string_input: str, **kwargs) -> tuple[bool, int | None]:
            if kwargs["user_type"] is
