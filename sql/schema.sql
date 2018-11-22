CREATE TABLE Users(
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	email VARCHAR(40) NOT NULL,
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted TIMESTAMP,
	password VARCHAR(255) NOT NULL
);


-- Email_to_Id is a temporary hack to efficiently retrieve user_id by email
CREATE TABLE Email_to_Id(
	email VARCHAR(40),
	user_id INTEGER NOT NULL,
	PRIMARY KEY(email)
);


-- filename is the filename of the project specification
-- starter_files is the filename of the zipped starter files
-- autograder is the filename of the autograder 
CREATE TABLE Projects(
	project_id INTEGER PRIMARY KEY AUTOINCREMENT,
	project_name VARCHAR(40) NOT NULL, 
	filename VARCHAR(40) NOT NULL,
	starter_files VARCHAR(40), 
	autograder VARCHAR(40)
);


-- This table identifies what user is allowed to access project_id
CREATE TABLE Project_Permissions(
	project_id INTEGER,
	user_id INTEGER,
	PRIMARY KEY(project_id, user_id)
);

--Each user will also create their own submissions table
--The table will be named user_projectnum_submissions;

/*
Each submissions table should look roughly like this:
CREATE TABLE user_projectnum_submissions(
	submission_id INTEGER NOT NULL,
	time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	PRIMARY KEY(submission_id)
);
*/
