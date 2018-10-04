use university
go

CREATE VIEW ListOfStudents AS
	SELECT 
		fac.name as Faculty, 
		spec.name as Speciality, 
		g.name as Groupa, 
		s.name as Student, 
		n.name as Natianality, 
		r.name as Region, 
		DATEDIFF(Year, 0, DATEDIFF(Day, s.birthday, GETDATE())) as Age
	FROM Students as s

	INNER JOIN Regions as r
		ON s.region_id = r.id
	INNER JOIN Nationalities as n
		ON s.nationality_id = n.id
	INNER JOIN Groups as g
		ON s.group_id = g.id
	INNER JOIN Specialities as spec
		ON g.speciality_id = spec.id
	INNER JOIN Faculties as fac
		ON spec.faculty_id = fac.id

GO


CREATE VIEW CountOfStudents AS
	SELECT 
		fac.name as Faculty, 
		spec.name as Speciality, 
		g.name as "Group",
		COUNT(s.id) as count 
	FROM Students as s
	INNER JOIN Groups as g
		ON s.group_id = g.id
	INNER JOIN Specialities as spec
		ON g.speciality_id = spec.id
	INNER JOIN Faculties as fac
		ON spec.faculty_id = fac.id

	GROUP BY fac.name, spec.name, g.name
GO

CREATE VIEW CountByStudentsAges AS
	SELECT Groupa, Age, count(Student) as Count
	FROM ListOfStudents
	GROUP BY Groupa, Age
GO



CREATE VIEW StudentWithGoodGrade AS
	SELECT s.name 
	FROM Student as s
	INNER JOIN ProgresInStudy as pis
		ON s.id = pis.student_id
	WHERE pis.prize > 87
	GROUP BY s.name

GO

CREATE VIEW TeachersTop AS
	SELECT t.name AS teacher, g.name AS [group], COUNT(s.name) AS subjects
	FROM  dbo.Teachers AS t 
	INNER JOIN dbo.Lectures AS l 
		ON t.id = l.teacher_id 
	INNER JOIN dbo.Groups AS g 
		ON l.group_id = g.id 
	INNER JOIN dbo.Subjects AS s 
		ON l.subject_id = s.id
	GROUP BY t.name, g.name
	ORDER BY subjects DESC
	