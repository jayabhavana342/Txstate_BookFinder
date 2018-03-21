CREATE USER 'bhavana@localhost'
  IDENTIFIED BY '123456';

GRANT ALL PRIVILEGES ON txstatebookfinder.*
TO 'bhavana'@'localhost'
IDENTIFIED BY '123456';

SHOW GRANTS FOR 'bhavana'@'localhost';

USE txstatebookfinder;

/*
===============================
Customer Table
===============================
 */

DROP TABLE IF EXISTS CUSTOMER;

CREATE TABLE CUSTOMER (
  CustomerID    VARCHAR(100) UNIQUE NOT NULL,
  FirstName     VARCHAR(15)         NOT NULL,
  LastName      VARCHAR(15)         NOT NULL,
  Email         VARCHAR(320)        NOT NULL,
  Password      VARCHAR(16)         NOT NULL,
  StreetAddress VARCHAR(50)         NOT NULL,
  City          VARCHAR(15)         NOT NULL,
  PhoneNumber   INTEGER(10)         NOT NULL,
  PRIMARY KEY (CustomerID)
);

/*
Insert values into Customer Table
 */

INSERT INTO CUSTOMER (CustomerID, FirstName, LastName, Email, Password, StreetAddress, City, PhoneNumber)
VALUES (uuid(), 'John', 'Bradley', 'john@gmail.com', 'john@123', '509 Acacia Ave', 'San Diego', 896654753);


/*
Display Table Customer
 */

SELECT *
FROM CUSTOMER;

DESC CUSTOMER;

/*
===============================
BOOKS Table
===============================
 */

DROP TABLE IF EXISTS BOOKS;

CREATE TABLE BOOKS (
  ISBN            VARCHAR(100) UNIQUE NOT NULL,
  BookTitle       VARCHAR(300)        NOT NULL,
  BookAuthor      VARCHAR(100)        NOT NULL,
  BookPrice       DECIMAL(5, 2)       NOT NULL,
  BookImage       BLOB                NOT NULL,
  BookPublishDate DATE                NOT NULL,
  CourseID        VARCHAR(10) REFERENCES COURSES (CourseID),
  PRIMARY KEY (ISBN)
);

/*
Insert values into Books Table
 */

/*
Dr.Jill Seaman
 */

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780133360929', 'Starting Out with C++ From Control Structures through Objects', 'Tony Gaddis', 289.89,
   'images/1_tonny_gaddis.jpg', '2010-12-12', 'CS5301');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780138152215', 'Object Oriented Software Engineering Using UML, Patterns and JAVA', 'Bernd Bruegge Allen H.Dutiot',
   356.36,
   'images/2_Object_oriented.jpg', '2012-12-12', 'CS4354');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780805354478', 'Data Structures and Problem Solving Using C++', 'Weiss', 564.54, 'images/3_DataStructures.jpg',
   '1994-12-10', 'CS3358');

/*
Dr.Xiao Chen
 */

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780321205001', 'Operating System Concepts', 'Abraham Silberschatz', 657.56, 'images/4_Operatingsystems.jpg',
   '1998-04-12', 'CS4328');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780865424478', 'Software Engineering A Practitioners Approach', 'Roger S Pressman', 112.23, 'images/5_survey.jpg',
   '2001-06-08', 'CS5391');

/*
Dr.Anne Ngu
 */

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780790209765', 'Object Oriented Design and Patterns', 'Cay Horstmann', 321.45, 'images/6_Ngu_JAVA.jpg',
   '2002-09-08', 'CS3354');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780201612509', 'Fundamentals of Database Systems', 'Elmasri', 666.56, 'images/7_Fundaments DB_NGU.jpg',
   '2000-06-05', 'CS4332');

/*
Dr.Wuxu Peng
 */

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780071808552', 'Computer Networks', 'Tanenbaum Wetherall', 222.32, 'images/8_Computer_networks.jpg', '2002-03-15',
   'CS5310');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9783827321312', 'Wireless Communications and Networks', 'William Stallings', 333.45,
   'images/9_Wireless_networks.jpg', '2012-05-13', 'CS5343');

/*
Dr.Dan Tamir
 */

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780321149121', 'C++ GUI Programming with Qt4', 'Jasmin Blanchette', 123.32, 'images/10_GUI.jpg', '2003-11-17',
   'CS5306');

INSERT INTO BOOKS (ISBN, BookTitle, BookAuthor, BookPrice, BookImage, BookPublishDate, CourseID)
VALUES
  ('9780321165471', 'Advanced Operating Systems and Kernel Applications', 'Jasmin Blanchette', 506.32,
   'images/11_advanced_OS.jpg', '2006-06-05', 'CS5389');

/*
Display Table Books
 */

SELECT *
FROM BOOKS;

DESC BOOKS;

/*
===============================
PROFESSORS Details Table
===============================
 */
DROP TABLE IF EXISTS PROFESSORS;

CREATE TABLE PROFESSORS (
  ProfessorID      INT(3) UNIQUE NOT NULL,
  ProfessorName    VARCHAR(50)   NOT NULL,
  ProfessorWebsite VARCHAR(2083) NOT NULL,
  PRIMARY KEY (ProfessorID)
);

/*
Insert values into PROFESSORS Table
 */

INSERT INTO PROFESSORS (ProfessorID, ProfessorName, ProfessorWebsite)
VALUES
  (111, 'Dr.Jill Seaman', 'http://cs.txstate.edu/~js236/');

INSERT INTO PROFESSORS (ProfessorID, ProfessorName, ProfessorWebsite)
VALUES
  (222, 'Dr.Xiao Chen', 'http://cs.txstate.edu/~xc10/');

INSERT INTO PROFESSORS (ProfessorID, ProfessorName, ProfessorWebsite)
VALUES
  (333, 'Dr.Anne Hee Hiong Ngu', 'http://cs.txstate.edu/~hn12/');

INSERT INTO PROFESSORS (ProfessorID, ProfessorName, ProfessorWebsite)
VALUES
  (444, 'Dr.Wuxu Peng', 'https://keystone.cs.txstate.edu/personal/');

INSERT INTO PROFESSORS (ProfessorID, ProfessorName, ProfessorWebsite)
VALUES
  (555, 'Dr.Dan Tamir', 'http://cs.txstate.edu/~dt19/');


/*
Display PROFESSORS Table
 */

SELECT *
FROM PROFESSORS;

DESC PROFESSORS;

/*
===============================
COURSES Table
===============================
 */

DROP TABLE IF EXISTS COURSES;

CREATE TABLE COURSES (
  CourseID   VARCHAR(10) UNIQUE NOT NULL,
  CourseName VARCHAR(100)       NOT NULL,
  PRIMARY KEY (CourseID)
);

/*
Insert values into COURSES
 */

INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5301', 'Advanced Programming Practicum');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS4354', 'Object Oriented Design and Implementation');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS3358', 'Data Structures');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS4328', 'Operating Systems');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5391', 'Roger S Pressman');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS3354', 'Object Oriented Design and Patterns');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS4332', 'Introduction to Database Systems');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5310', 'Computer Networks and Communication Systems');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5343', 'Wireless Communication Networks and Systems');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5389', 'Graphical User Interface');


INSERT INTO COURSES (CourseID, CourseName)
VALUES ('CS5306', 'Advanced Operating Systems');

/*
Display Table COURSES
 */

SELECT *
FROM COURSES;

DESC COURSES;

/*
===============================
COURSESBYPROF Table
===============================
 */

DROP TABLE IF EXISTS COURSESBYPROF;

CREATE TABLE COURSESBYPROF (
  ProfessorID INT(3) UNIQUE      NOT NULL REFERENCES PROFESSORS (ProfessorID),
  CourseID    VARCHAR(10) UNIQUE NOT NULL REFERENCES COURSES (CourseID),
  PRIMARY KEY (ProfessorID, CourseID)
);

/*
Display Table COURSESBYPROF
 */

SELECT *
FROM COURSESBYPROF;

DESC COURSESBYPROF;

/*
===============================
CREDITCARDDETAILS Table
===============================
 */

DROP TABLE IF EXISTS CREDITCARDDETAILS;

CREATE TABLE CREDITCARDDETAILS (
  CardNum  VARCHAR(25) UNIQUE NOT NULL,
  CardType VARCHAR(50)        NOT NULL,
  ExpMonth TINYINT            NOT NULL,
  ExpYear  TINYINT            NOT NULL,
  PRIMARY KEY (CardNum)
);

/*
Display Table CREDITCARDDETAILS
 */

SELECT *
FROM CREDITCARDDETAILS;

DESC CREDITCARDDETAILS;

/*
===============================
CUSTOMERCREDITCARDDETAILS Table
===============================
 */

DROP TABLE IF EXISTS CUSTOMERCREDITCARDDETAILS;

CREATE TABLE CUSTOMERCREDITCARDDETAILS (
  CardNum    VARCHAR(25)  NOT NULL REFERENCES CREDITCARDDETAILS (CardNum),
  CustomerID VARCHAR(100) NOT NULL REFERENCES CUSTOMER (CustomerID),
  PRIMARY KEY (CardNum, CustomerID)
);

/*
Display Table CUSTOMERCREDITCARDDETAILS
 */

SELECT *
FROM CUSTOMERCREDITCARDDETAILS;

DESC CUSTOMERCREDITCARDDETAILS;

/*
===============================
SHOPPINGCART Table
===============================
 */

DROP TABLE IF EXISTS SHOPPINGCART;

CREATE TABLE SHOPPINGCART (
  CartID     VARCHAR(25) UNIQUE      NOT NULL,
  CustomerID VARCHAR(100) UNIQUE     NOT NULL REFERENCES CUSTOMER (CustomerID),
  PRIMARY KEY (CartID, CustomerID)
);

/*
Display Table SHOPPINGCART
 */

SELECT *
FROM SHOPPINGCART;

DESC SHOPPINGCART;

/*
===============================
SHOPPINGCARTBOOKS Table
===============================
 */

DROP TABLE IF EXISTS SHOPPINGCARTBOOKS;

CREATE TABLE SHOPPINGCARTBOOKS (
  CartID   VARCHAR(25)  NOT NULL REFERENCES SHOPPINGCART (CartID),
  ISBN     VARCHAR(100) NOT NULL REFERENCES BOOKS (ISBN),
  Quantity INT(2)       NOT NULL,
  PRIMARY KEY (CartID, ISBN)
);

/*
Display Table SHOPPINGCARTBOOKS
 */

SELECT *
FROM SHOPPINGCARTBOOKS;

DESC SHOPPINGCARTBOOKS;

SHOW TABLES;



