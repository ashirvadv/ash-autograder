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

CREATE TABLE project_permissions(
	username VARCHAR(20) PRIMARY KEY NOT NULL,
	projectid INTEGER NOT NULL,
	FOREIGN KEY (username) REFERENCES users(username)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

CREATE TABLE submissions(
	submissionid INTEGER PRIMARY KEY AUTOINCREMENT,
	projectid INTEGER NOT NULL,
	filename_code VARCHAR(64) NOT NULL,
	filename_report VARCHAR(64) NOT NULL,
	owner VARCHAR(20) NOT NULL,
	created TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	FOREIGN KEY (projectid) REFERENCES projects(projectid),
	FOREIGN KEY (owner) REFERENCES users(username)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);
