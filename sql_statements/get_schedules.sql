CREATE VIEW room_per_offering AS
SELECT offering_id, room
FROM offerings
JOIN rooms
    ON offerings.room_id = rooms.room_id;

CREATE VIEW teacher_per_offering AS
SELECT offering_id, teacher_name
FROM offerings
JOIN teachers
    ON offerings.teacher_id = teachers.teacher_id;

CREATE VIEW course_per_offering AS
SELECT offering_id, crs_name, crs_type, courses.crs_type_id
FROM offerings
JOIN courses
    ON offerings.crs_id = courses.crs_id
JOIN course_types
    ON courses.crs_type_id = course_types.crs_type_id;

CREATE PROCEDURE get_schedule_per_student(pstudent_id INTEGER)
SELECT period, crs_name, room, teacher_name, o.offering_id, crs_type, crs_type_id
FROM offerings AS o
JOIN course_per_offering AS co
    ON o.offering_id = co.offering_id
JOIN room_per_offering AS ro
    ON o.offering_id = ro.offering_id
JOIN teacher_per_offering AS te
    ON o.offering_id = te.offering_id
WHERE o.offering_id IN (
	SELECT offering_id
	FROM roster
	WHERE student_id = pstudent_id
)
ORDER BY period;

CREATE PROCEDURE get_schedule_per_teacher(pteacher_id INTEGER)
SELECT period, crs_name, room, o.offering_id, crs_type, crs_type_id
FROM offerings AS o
JOIN course_per_offering AS co
    ON o.offering_id = co.offering_id
JOIN room_per_offering AS ro
    ON o.offering_id = ro.offering_id
WHERE o.teacher_id = pteacher_id
ORDER BY period;