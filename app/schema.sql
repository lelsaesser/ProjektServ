DROP TABLE IF EXISTS foodking;
CREATE TABLE foodking (
  food_id integer PRIMARY KEY autoincrement,
  title text NOT NULL,
  'text' text NOT NULL
);