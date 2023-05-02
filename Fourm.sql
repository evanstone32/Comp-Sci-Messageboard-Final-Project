DROP DATABASE `forum`;
CREATE DATABASE Forum;
USE Forum;

CREATE TABLE User
	(User_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username varchar(50),
	email varchar(50),
    password varchar (255), 
    first_name varchar(50), 
    last_name varchar(50)
    );
    
CREATE TABLE Forum
    (Forum_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title varchar(20)
    );
    
CREATE TABLE Post
	(Post_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	post varchar(300),
    User_ID INT NOT NULL,
    Forum_ID INT NOT NULL,
	FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Forum_ID) REFERENCES Forum(Forum_ID)
	);
    
CREATE TABLE Comment
	(Comment_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    comment varchar(50),
    Post_ID INT NOT NULL,
    User_ID INT NOT NULL,
    FOREIGN KEY (Post_ID) REFERENCES Post(Post_ID),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
    );