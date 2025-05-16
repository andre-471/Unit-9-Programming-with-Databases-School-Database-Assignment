from enum import IntEnum
from collections.abc import Callable
from typing import Protocol

from dbconnection import DBConnection


class UserTypes(IntEnum):
    STUDENT = 1
    TEACHER = 2


class GetsInput(Protocol):
    def __call__(self, has_error: bool) -> str: ...


class ChecksSuccess[T](Protocol):
    def __call__(self, user_input: str) -> (bool, T | None): ...


class Jupiter:
    def __init__(self, database) -> None:
        self.connection: DBConnection = DBConnection(database)
        self.user_type: UserTypes | None = None

    def login(self):
        print("Are you a student or a teacher?")
        print("1: Student")
        print("2: Teacher")
        user_type: str = input("Enter choice: ").strip()
        user_type: int | None = int(user_type) if user_type.isdigit() else None

        while user_type not in UserTypes:
            print("Invalid choice!")
            user_type: str = input("Enter choice: ").strip()
            user_type: int | None = int(user_type) if user_type.isdigit() else None

        self.user_type: UserTypes = UserTypes(user_type)

        if self.user_type is UserTypes.STUDENT:
            pass
        else:
            pass

    def _input_until_success[T](self, get_input: GetsInput,
                                if_success: ChecksSuccess[T]) -> T:
        user_input: str = get_input(False)

        successful: bool
        formatted_input: T | None
        successful, formatted_input = if_success(user_input)

        while not successful:
            user_input: str = get_input(True)
            successful, formatted_input = if_success(user_input)

        return formatted_input
