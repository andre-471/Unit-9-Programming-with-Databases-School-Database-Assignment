CREATE PROCEDURE get_grades_per_student(pstudent_id INTEGER, poffering_id INTEGER)
SELECT asg_name, asg_type, asg_type_id, grade
FROM assignments a
JOIN assignment_types t
    ON a.asg_type_id = t.asg_type_id
JOIN grades g
    ON a.asg_id = g.asg_id
WHERE offering_id = poffering_id
AND student_id = pstudent_id;
