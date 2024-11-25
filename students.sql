CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    StudentNumber VARCHAR(20),
    Class VARCHAR(50),
    Age INT NOT NULL
);
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100),
    TeacherID INT,
    Credits INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID)
);
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseID INT,
    EnrollmentDate DATE,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    Name VARCHAR(100),
    Qualification VARCHAR(50)
);
CREATE TABLE Class(
     Class ID INT,
     Class NAME INT,
     Class TYPE VARCHAR(50),
     Classroom ID INT
);
