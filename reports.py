import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        # self.id = id
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Instructor():

    def __init__(self, first, last, handle, specialty, cohort):
        # self.id = id
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} teaches {self.cohort} and specializes in {self.specialty}'

class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    # def __repr__(self):
    #     return f'{self.name} is a {self.language} exercise'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/Amber/workspace/python/exercises/book2/chapter3/student-exercises/student-exercises.db"

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[4], row[5])

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(
                row[1], row[2], row[3], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.cohortId,
                c.name
            from student s
            join cohort c on s.cohortId = c.id
            order by s.cohortId
            """)

            all_students = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            for student in all_students:
                print(student)

    def all_instructors(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(
                row[1], row[2], row[3], row[4], row[5]
            )
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.id,
                i.first_name,
                i.last_name,
                i.slack_handle,
                i.specialty,
                i.cohortId,
                c.name
            from instructor i
            join cohort c on i.cohortId = c.id
            order by i.cohortId
            """)

            all_instructors = db_cursor.fetchall()

            # for student in all_students:
            #     print(f'{student[1]} {student[2]} is in {student[5]}')

            for instructor in all_instructors:
                print(instructor)

    def all_cohorts(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(
                row[1]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select c.id,
                    c.name
                from cohort c
                order by c.id
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)

    def all_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercise e
                order by e.id
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(f'{exercise.name} is a {exercise.language} exercise')

    def javascript_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercise e
                where e.language = "Javascript"
            """)

            javascript_exercises = db_cursor.fetchall()

            print("Javascript exercises:")
            for exercise in javascript_exercises:
                print(f"    *{exercise.name}")

    def python_exercises(self):

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(
                row[1], row[2]
            )

            db_cursor = conn.cursor()

            db_cursor.execute("""
                select e.id,
                    e.name,
                    e.language
                from exercise e
                where e.language = "Python"
            """)

            javascript_exercises = db_cursor.fetchall()

            print("Python exercises:")
            for exercise in javascript_exercises:
                print(f"    *{exercise.name}")



reports = StudentExerciseReports()
reports.all_students()
student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
print(f'{student.first_name} {student.last_name} is in {student.cohort}')

reports.all_instructors()
reports.all_cohorts()
reports.all_exercises()
reports.javascript_exercises()
reports.python_exercises()

