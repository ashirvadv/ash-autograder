CREATE TABLE Users(
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	email VARCHAR(40) NOT NULL,
	user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	deleted TIMESTAMP,
	username VARCHAR(20) NOT NULL,
	password VARCHAR(255) NOT NULL,
	FOREIGN KEY(username) REFERENCES Username_to_Id(username),
	FOREIGN KEY(email) REFERENCES Email_to_Id(email)
);

CREATE TABLE Username_to_Id(
	username VARCHAR(20) NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY(username),
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE Email_to_Id(
	email VARCHAR(20) NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY(email),
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
);

CREATE TABLE Projects(
	project_id INTEGER PRIMARY KEY AUTOINCREMENT,
	project_name VARCHAR(40) NOT NULL,
);

CREATE TABLE Project_Permissions(
	project_id INTEGER,
	user_id INTEGER,
	PRIMARY KEY(project_id, user_id),
	FOREIGN KEY(project_id) REFERENCES Projects(project_id),
	FOREIGN KEY(user_id) REFERENCES Users(user_id)
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
