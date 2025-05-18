import sys
from dbconnection import DBConnection
from jupiter import Jupiter

# connection = DBConnection("andrewz47_db")
#
# student_id = input("Enter a student ID: ")
# student_id = int(student_id) if student_id.isdigit() else None
#
# if student_id is None:
#     print("Invalid option")
#     sys.exit(0)
#
# info = connection.query("CALL get_schedule_per_student(%(student_id)s)", {'student_id': student_id})
#
# for period, course, room, teacher in info:
#     print(f"Period: {period}")
#     print(f"Course: {course}")
#     print(f"Room: {room}")
#     print(f"Teacher: {teacher}")
#     print()

def main():
    jupiter = Jupiter("hi")
    jupiter.login()




if __name__ == '__main__':
    main()