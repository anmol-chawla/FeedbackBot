CREATE TABLE feedback (
  id integer PRIMARY KEY AUTOINCREMENT,
  uid text NOT NULL,
  time text NOT NULL,
  query text NOT NULL,
  response text NOT NULL
)