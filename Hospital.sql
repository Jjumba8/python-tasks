CREATE DATABASE Hospital;

USE Hospital;

CREATE TABLE Patient(PID VARCHAR(20) PRIMARY KEY,
Pname VARCHAR(30),
address VARCHAR(20),
Fees INT);

INSERT INTO Patient(PID, Pname, address, Fees) VALUES
('P1', 'Chemo', 'Kasese', 200000),
('P2', 'Tally', 'mukono', 150000),
('P3', 'Johnson', 'Lira', 100000),
('P4', 'Jay', 'Janeiro', 200000);

CREATE VIEW VIEW_A AS SELECT  SUM(Fees) FROM Patient;

CREATE VIEW VIEW_B AS 
SELECT Pname FROM Patient ORDER BY Pname DESC;

ALTER TABLE Patient ADD COLUMN DOB VARCHAR(10)

UPDATE Patient SET DOB = '2005' WHERE PID = 'P1';

UPDATE Patient SET DOB = '2006' WHERE PID = 'P2'

UPDATE Patient SET DOB = '2004' WHERE PID = 'P3'

UPDATE Patient SET DOB = '2008' WHERE PID = 'P4'

SELECT * FROM Patient