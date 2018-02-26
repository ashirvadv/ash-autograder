CREATE TABLE users(
	username VARCHAR(20) NOT NULL,
	fullname VARCHAR(40) NOT NULL,
	email VARCHAR(40) NOT NULL, 
	filename VARCHAR(64) NOT NULL, 
	password VARCHAR(256) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	PRIMARY KEY(username)
);

CREATE TABLE projects(
	projectid INTEGER PRIMARY KEY NOT NULL,
	filename VARCHAR(64) NOT NULL, 
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

CREATE TABLE submissions(
	submissionid INTEGER PRIMARY KEY AUTOINCREMENT,
	filename VARCHAR(64) NOT NULL,
	owner VARCHAR(20) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	FOREIGN KEY (owner) REFERENCES users(username)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);
