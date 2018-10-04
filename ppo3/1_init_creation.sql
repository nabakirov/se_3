CREATE DATABASE University
GO

USE University
GO

CREATE TABLE Regions (
	id TINYINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE Nationalities(
	id SMALLINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Faculties(
	id TINYINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Subjects(
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
);

CREATE TABLE Specialities(
	id SMALLINT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	faculty_id TINYINT NOT NULL,

	CONSTRAINT fk_spec_faculty_id
		FOREIGN KEY(faculty_id) 
		REFERENCES Faculties(id)
		ON UPDATE CASCADE	
);

CREATE TABLE Groups(
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	speciality_id SMALLINT NOT NULL,

	CONSTRAINT fk_spec_group_id
		FOREIGN KEY(speciality_id) 
		REFERENCES Specialities(id)
		ON UPDATE CASCADE
);

CREATE TABLE Students(
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	birthday DATE NULL,
	region_id TINYINT NULL,
	nationality_id SMALLINT NULL,
	group_id INT NOT NULL,

	CONSTRAINT fk_stud_region_id
		FOREIGN KEY(region_id) 
		REFERENCES Regions(id)
		ON DELETE SET NULL
		ON UPDATE CASCADE,
	CONSTRAINT fk_stud_nationality_id
		FOREIGN KEY(nationality_id) 
		REFERENCES Nationalities(id)
		ON DELETE SET NULL
		ON UPDATE CASCADE,
	CONSTRAINT fk_stud_group_id
		FOREIGN KEY(group_id) 
		REFERENCES Groups(id)
		ON UPDATE CASCADE
	
);

CREATE TABLE Teachers (
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	addres VARCHAR(150) NOT NULL,
);
CREATE TABLE ProgressInStudy(
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	student_id INT NOT NULL,
	subject_id INT NOT NULL,
	term TINYINT NOT NULL,
	prize TINYINT NOT NULL,

	CHECK(term >= 1 AND term <= 10),
	CHECK(prize >= 0 AND prize <= 100),
	CONSTRAINT fk_progress_student_id
		FOREIGN KEY(student_id) 
		REFERENCES Students(id)
		ON UPDATE CASCADE,
	CONSTRAINT fk_progress_subject_id
		FOREIGN KEY(subject_id) 
		REFERENCES Subjects(id)
		ON UPDATE CASCADE
);
CREATE TABLE Lectures(
	id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	teacher_id INT NOT NULL,
	subject_id INT NOT NULL,
	group_id INT NOT NULL,

	CONSTRAINT fk_lecture_group_id
		FOREIGN KEY(group_id) 
		REFERENCES Groups(id)
		ON UPDATE CASCADE,
	CONSTRAINT fk_lecture_teacher_id
		FOREIGN KEY(teacher_id) 
		REFERENCES Teachers(id)
		ON UPDATE CASCADE,
	CONSTRAINT fk_lecture_subject_id
		FOREIGN KEY(subject_id) 
		REFERENCES Subjects(id)
		ON UPDATE CASCADE
);
GO
