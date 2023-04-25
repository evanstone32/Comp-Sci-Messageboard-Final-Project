CREATE DATABASE Forum;
USE Forum;

CREATE TABLE Users
	(User_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username varchar(50),
	email varchar(50),
    pass varchar (50), 
    first_name varchar(50), 
    last_name varchar(50)
    );
    
CREATE TABLE Post
	(Post_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	post varchar(300),
    User_ID INT NOT NULL,
	FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
	);
    
CREATE TABLE Forum
	(Forum_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title varchar(20),
    Post_ID INT NOT NULL,
    FOREIGN KEY (Post_ID) REFERENCES Post(Post_ID)
    );
    
CREATE TABLE Comments
	(Comment_ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    comments varchar(50),
    Post_ID INT NOT NULL,
    User_ID INT NOT NULL,
    FOREIGN KEY (Post_ID) REFERENCES Post(Post_ID),
    FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
    );