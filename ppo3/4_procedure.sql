CREATE PROCEDURE SP_Speciality @faculty_id DEC(5,3) AS
	SELECT s.* 
	FROM Faculties as f
	INNER JOIN Specialities as s
		ON s.faculty_id = f.id
	WHERE f.id = @faculty_id

CREATE PROCEDURE SP_GROUPS @speciality_id DEC(5,3) AS
	SELECT g.*
	FROM Groups as g
	INNER JOIN Specialities as s
		ON g.speciality_id = s.id
	WHERE s.id = @speciality_id

CREATE PROCEDURE SP_Students @group_id DEC(5,3) AS
	SELECT s.*
	FROM Students as s
	INNER JOIN Groups as g
		ON s.group_id = g.id
	WHERE g.id = @group_id

