INSERT INTO users(username, fullname, email, filename, password, created)
	VALUES ('ashvarma', 'Ashirvad Varma', 'ashvarma@umich.edu', 'ash.jpg', 'sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', CURRENT_TIMESTAMP);
	
INSERT INTO projects(projectid, filename, created)
	VALUES (0, 'file', CURRENT_TIMESTAMP);

INSERT INTO users(username, fullname, email, filename, password, created)
	VALUES ('admin', 'Ashirvad Varma', 'ashvarma@umich.edu', 'f32e278bb9c2fbb07278c7457b71ebbb717ca114d9d5733efdefbdbb20ba3897', 'sha512$94cf1765058940f8b28a0e7233e95e72$d5b987513263d65380503e78f7a70db96854634af3051a3e99a291e3c08f5f68242465d84def5f14725fdc5624772b9e1ae5910e6b4d0557ee5fe476d8204a42', CURRENT_TIMESTAMP);

INSERT INTO project_permissions(username, projectid)
	VALUES ('admin', 0);
