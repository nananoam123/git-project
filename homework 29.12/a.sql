CREATE TABLE "Busses" (
	"destination "	TEXT NOT NULL,
	"company "	TEXT NOT NULL
);

INSERT INTO Busses
VALUES('Beer Sheva','Dan');
INSERT INTO Busses
VALUES('Herzliya','Metropoline');
INSERT INTO Busses
VALUES('HOLON','Metropoline');
INSERT INTO Busses
VALUES('HOLON','Metropoline');

UPDATE Busses SET company = 'Egged' WHERE destination = 'HOLON'

