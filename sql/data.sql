INSERT INTO Projects(project_name, filename, starter_files, autograder)
VALUES ('First project!', 'tempfile.txt', 'starter.txt', 'auto.txt');

INSERT INTO Project_Permissions(project_id, user_id)
VALUES (1, 1);

INSERT INTO Project_Permissions(project_id, user_id)
VALUES (1, 2);