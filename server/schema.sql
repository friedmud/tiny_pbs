DROP TABLE IF EXISTS job;
DROP TABLE IF EXISTS running;

CREATE TABLE job (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  submitted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  started TIMESTEAMP,
  finished TIMESTAMP,
  command TEXT NOT NULL
);

CREATE TABLE running (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  job_id INTEGER NOT NULL,
  FOREIGN KEY (job_id) REFERENCES job (id)
);
