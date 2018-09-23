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


-- CREATE VIEW CountOfStudents AS
-- 	SELECT 
-- 		fac.name as Faculty, 
-- 		spec.name as Speciality, 
-- 		g.name as "Group",
-- 		COUNT(s.id) as count 
-- 	FROM Students as s
-- 	INNER JOIN Groups as g
-- 		ON s.group_id = g.id
-- 	INNER JOIN Specialities as spec
-- 		ON g.speciality_id = spec.id
-- 	INNER JOIN Faculties as fac
-- 		ON spec.faculty_id = fac.id

-- 	GROUP BY fac.name, spec.name, g.name
-- GO

CREATE VIEW CountByStudentsAges AS
	SELECT Groupa, Age, count(Student) as Count
	FROM ListOfStudents
	GROUP BY Groupa, Age
GO
