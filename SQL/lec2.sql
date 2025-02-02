DROP TABLE IF EXISTS Students;

CREATE TABLE Students(
	StudentID SERIAL PRIMARY KEY NOT NULL,
	FirstName VARCHAR(20) NOT NULL,
	LastName VARCHAR(20) NOT NULL
);

-- fill the table with data:
INSERT INTO Students(FirstName, LastName)
VALUES ('Moshe', 'Doe'), ('Dave', 'Green');


INSERT INTO Students(FirstName, LastName)
VALUES ('Joe', 'Krup');

SELECT * FROM Students;


DROP TABLE IF EXISTS Products;

CREATE TABLE Products(
	ProductID SERIAL PRIMARY KEY NOT NULL, 
	ProductName VARCHAR(64) NOT NULL,
	Price DECIMAL(10, 2) NOT NULL
);

INSERT INTO Products(ProductName, Price)
VALUES('Notebook', 5.9), ('Banana', 3.9);

SELECT * FROM Products;


DROP TABLE IF EXISTS Users CASCADE; -- also delete any related rows in other tables
DROP TABLE IF EXISTS UserProfiles CASCADE;

CREATE TABLE Users(
	UserID SERIAL PRIMARY KEY,
	Username VARCHAR(32)
);

CREATE TABLE UserProfiles(
	UserProfileID SERIAL PRIMARY KEY,
	Phone VARCHAR(20) NULL,
	Email VARCHAR(100) NOT NULL UNIQUE,
	UserID INTEGER, 
	FOREIGN KEY (UserID) REFERENCES Users(UserID) 
);

INSERT INTO Users(Username)
VALUES ('Larry'), ('Jerry'), ('Margo');

INSERT INTO UserProfiles(Email, UserId)
VALUES('LarryBird@gmail.com', 1);

SELECT * 
FROM Users JOIN UserProfiles USING(UserID);

DROP TABLE IF EXISTS Country CASCADE;
DROP TABLE IF EXISTS Capital CASCADE;

CREATE TABLE Country(
	CountryID SERIAL PRIMARY KEY,
	CountyName VARCHAR(64) NOT NULL
);

CREATE TABLE Capital(
	CapitalID SERIAL PRIMARY KEY,
	CapitalName VARCHAR(64) NOT NULL,
	CountryID INTEGER UNIQUE,
	FOREIGN KEY (CountryID) REFERENCES Country(CountryID) ON DELETE SET NULL
);

SELECT * FROM Capital;

INSERT INTO Country(CountyName)
VALUES ('UK'),('France'), ('Ukraine');

INSERT INTO Capital(CountryID, CapitalName)
VALUES (1, 'London'),(2, 'Paris'), (3, 'Kyiv');


SELECT * 
FROM Country JOIN Capital USING(CountryID);


DROP TABLE IF EXISTS Movies CASCADE;
DROP TABLE IF EXISTS Categories CASCADE;
DROP TABLE IF EXISTS MovieCategories CASCADE;

CREATE TABLE Movies(
	MovieID SERIAL PRIMARY KEY,
	Title VARCHAR(100) NOT NULL
);

CREATE TABLE Categories(
	CategoryID SERIAL PRIMARY KEY,
	CategoryName VARCHAR(100) NOT NULL
);

-- many to many
--1) relationship table:
CREATE TABLE MovieCategories(
	MovieID INTEGER,
	CategoryID INTEGER,
	PRIMARY KEY (MovieID, CategoryID),
	FOREIGN KEY (MovieID) REFERENCES Movies(MovieID) ON DELETE CASCADE,
	FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE
);

INSERT INTO Movies(title)
VALUES ('Batman'), ('Spiderman'), ('Shrek');

INSERT INTO CATEGORIES(CategoryName)
VALUES ('action'), ('fantasy'), ('comedy') ,('scifi'), ('cartoon'), ('horror'), ('crime'), ('animation');

--2) insert each movie id and related category ids
INSERT INTO MovieCategories(MovieID, CategoryID)
VALUES (1, 1), (1, 2), (1, 4), (1, 7), (2, 1), (2, 2), (2, 4), (2, 7);


DELETE FROM Movies
WHERE title = 'Batman';


--3) query using joins
SELECT title, categoryname
FROM Movies
JOIN MovieCategories USING(MovieID)
JOIN Categories USING(CategoryID);

DROP TABLE IF EXISTS Meetings;

-- Timestamp = Date + Time
CREATE TABLE Meetings(
	MeetingID SERIAL PRIMARY KEY,
	Title VARCHAR(200) NOT NULL,
	MeetingTime TIMESTAMP NOT NULL
);

INSERT INTO Meetings(title, MeetingTime)
VALUES ('Project Kickoff', '2025-02-02 09:30:00'),
		('Team Meeting', '2025-02-02'); -- time defaults to 00:00:00.000

INSERT INTO Meetings(title, MeetingTime)
VALUES ('Break', NOW());

SELECT *
FROM Meetings;
DROP TABLE IF EXISTS Events;
-- Date = Date only (no time)
CREATE TABLE Events(
	EventID SERIAL PRIMARY KEY,
	Title VARCHAR(200) NOT NULL,
	EventDate DATE NOT NULL
);

INSERT INTO Events(Title, EventDate)
VALUES ('Birtday Party', '2025-03-15'); -- YYYY-MM-DD  '2025-03-15'

-- use the current date
INSERT INTO Events(Title, EventDate)
VALUES ('Yoga Class', NOW()); -- 2025-02-02

SELECT *
FROM Events;




DROP TABLE IF EXISTS Tasks;

CREATE TABLE Tasks(
	TaskID SERIAL PRIMARY KEY,
	TaskName VARCHAR(100) NOT NULL,
	IsComplete BOOLEAN NOT NULL DEFAULT FALSE,
	CreatedAt TIMESTAMP DEFAULT NOW()
);

INSERT INTO Tasks(TaskName)
VALUES ('Call Mom'), ('Drink Coffee'), ('Learn Django'), ('Learn SQL');

UPDATE Tasks
SET IsComplete = TRUE
WHERE TaskID = 1;

SELECT *
FROM Tasks;


