CREATE TABLE Users(
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	email VARCHAR(40) NOT NULL,
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted TIMESTAMP,
	password VARCHAR(255) NOT NULL
);

CREATE TABLE Email_to_Id(
	email VARCHAR(40),
	user_id INTEGER NOT NULL,
	PRIMARY KEY(email)
);

CREATE TABLE Projects(
	project_id INTEGER PRIMARY KEY AUTOINCREMENT,
	project_name VARCHAR(40) NOT NULL, 
	filename VARCHAR(40) NOT NULL,
	starter_files VARCHAR(40), 
	autograder VARCHAR(40)
);

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
