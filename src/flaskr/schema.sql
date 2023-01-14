DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS projects;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE projects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  name TEXT NOT NULL,
  create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  finished BOOLEAN NULL,
  description TEXT NOT NULL,
  FOREIGN KEY (user_id) REFERENCES user (id)
);