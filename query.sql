CREATE TABLE cohort (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);


CREATE TABLE student (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slack_handle TEXT NOT NULL UNIQUE,
    cohortId INTEGER,
    FOREIGN KEY(cohortId) REFERENCES cohort(id)
);

CREATE TABLE instructor (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL UNIQUE,
    last_name TEXT NOT NULL UNIQUE,
    slack_handle TEXT NOT NULL UNIQUE,
    specialty TEXT NOT NULL UNIQUE,
    cohortId INTEGER,
    FOREIGN KEY(cohortId) 
    	REFERENCES cohort(id)
);

CREATE TABLE exercise (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    language TEXT NOT NULL
);


CREATE TABLE studentExercises (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    studentId INTEGER,
    exerciseId INTEGER,
    FOREIGN KEY(studentId) 
    	REFERENCES student(id),
    FOREIGN KEY(exerciseId) 
    	REFERENCES exercise(id)
);

INSERT INTO cohort (id, name)
VALUES (null, "Day Cohort 36");

INSERT INTO instructor (id, first_name, last_name, slack_handle, specialty, cohortId)
VALUES (null, "Steve", "Brownlee", "stevebrownlee", "staring into your soul", 1);

INSERT INTO instructor (id, first_name, last_name, slack_handle, specialty, cohortId)
VALUES (null, "Joe", "Shepherd", "JoeShep", "dad jokes", 1);

INSERT INTO instructor (id, first_name, last_name, slack_handle, specialty, cohortId)
VALUES (null, "Jisie", "David", "JisieD", "explaining stuff", 2);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Amber", "Gooch", "ambergooch", 1);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Syndey", "Noh", "simpleSnoh", 1);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Joe", "Kennerly", "jKen", 2);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Ben", "Parker", "benparker", 2);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Jake", "Scott", "jakeScott", 3);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Shane", "Miller", "STmill", 3);

INSERT INTO student (id, first_name, last_name, slack_handle, cohortId)
VALUES (null, "Misty", "Deramus", "mistyD", 1);

INSERT INTO exercise (id, name, language)
VALUES (null, "Daily Journal", "Javascript");

INSERT INTO exercise (id, name, language)
VALUES (null, "Coffee Houses", "HTML");

INSERT INTO exercise (id, name, language)
VALUES (null, "Ternary Traveler", "Javascript");

INSERT INTO exercise (id, name, language)
VALUES (null, "Cash to Coins", "Python");

INSERT INTO exercise (id, name, language)
VALUES (null, "Flower Shop", "Python");

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 1, 1);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 1, 2);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 2, 5);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 2, 3);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 3, 4);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 3, 5);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 4, 1);

INSERT INTO studentExercises (id, studentId, exerciseId)
VALUES (null, 4, 4);





