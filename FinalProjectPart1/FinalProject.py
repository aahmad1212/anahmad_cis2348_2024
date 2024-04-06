# Adil Ahmad
# 2278219
import csv
from datetime import datetime


# Student object to store information about a student. We use default values so we can update attributes as needed.
# GPA is stored as a float so we can compare it in order to determine if a student is eligible for a scholarship.
class Student:
    def __init__(
            self, student_id=0, major="null", first_name="null", last_name="null", gpa=0.0, grad_date="1/1/1970",
            disc_action="null"
    ):
        self.student_id = student_id
        self.major = major
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa
        self.grad_date = grad_date
        self.disc_action = disc_action

    # String representation of the object for debugging purposes
    def __str__(self):
        return f"ID#{self.student_id}"


# Sort by last name
def lastname(a):
    return a[3]


# Sort by student ID
def id_num(a):
    return a[0]


# Sort by date
def date(a):
    return datetime.strptime(a[3], "%m/%d/%Y")


# Sort by GPA
def student_gpa(a):
    return a[4]


today = datetime.today()
# Empty lists that will become tables later on
majors_list = []
full_roster = []
list_per_major = []
scholarship_candidates = []
disciplined_students = []
students = []
# Dictionary keys are student ID numbers, values are the Student objects.
students_dict = {}


# Open StudentsMajorsList.csv. Because it has the most information, we will use this file to build the Student objects.
with open("StudentsMajorsList.csv") as csvfile:
    majors_reader = csv.reader(csvfile)
    for row in majors_reader:
        # Create a list of majors which we will use to generate the Majors tables.
        if row[3] not in majors_list:
            majors_list.append(row[3])
        # Creates a student object using the data in each row, and associates them with the student ID number in the
        # dictionary.
        student = Student(student_id=int(row[0]), major=row[3], first_name=row[2], last_name=row[1], disc_action=row[4])
        students.append(student)
        students_dict[row[0]] = student

with open("GPAList.csv") as csvfile:
    gpa_reader = csv.reader(csvfile)
    for row in gpa_reader:
        for student in students_dict:
            # Matches ID in GPAList with ID of a Student. Updates the GPA attribute with corresponding GPA value.
            if int(row[0]) == students_dict[student].student_id:
                students_dict[student].gpa = float(row[1])

with open("GraduationDatesList.csv") as csvfile:
    grad_reader = csv.reader(csvfile)
    for row in grad_reader:
        for student in students_dict:
            # Updates graduation date attribute of students with their graduation dates.
            if int(row[0]) == students_dict[student].student_id:
                students_dict[student].grad_date = row[1]

# Now that we have all of the student data, we can build our tables.

# We use the attributes of each Student object to fill each row.

# The rows will contain all data for the listed attributes. We will filter the data using conditionals to determine
# whether to write a row or not using CSV writer.
for i in students_dict:
    x = students_dict[i]

    full_roster.append([x.student_id, x.major, x.first_name, x.last_name, x.gpa, x.grad_date, x.disc_action])

    scholarship_candidates.append([x.student_id, x.last_name, x.first_name, x.major, x.gpa])

    list_per_major.append([x.student_id, x.last_name, x.first_name, x.grad_date, x.disc_action])

    disciplined_students.append([x.student_id, x.last_name, x.first_name, x.grad_date])

full_roster.sort(key=lastname)
scholarship_candidates.sort(key=student_gpa)
scholarship_candidates.reverse()
list_per_major.sort(key=id_num)
disciplined_students.sort(key=date)

# Creates FullRoster.csv and writes the table to it.
with open("FullRoster.csv", "w", newline="") as csvfile:
    roster_writer = csv.writer(csvfile)
    for row in full_roster:
        roster_writer.writerow(row)

# We use a for loop to create a new file for each given major. Checks if the major matches with the student, then writes
# the row to the file.
for i in majors_list:
    filename = i.replace(" ", "")
    with open(f"{filename}Students.csv", "w", newline="") as csvfile:
        majors_writer = csv.writer(csvfile)
        for row in list_per_major:
            if students_dict[str(row[0])].major == i:
                majors_writer.writerow(row)

# Checks if a student meets all criteria (GPA above 3.8, hasn't graduated yet, not disciplined). If so, it writes the
# the row to the file.
with open("ScholarshipCandidates.csv", "w", newline="") as csvfile:
    scholarship_writer = csv.writer(csvfile)
    for row in scholarship_candidates:
        date_compare = datetime.strptime(students_dict[str(row[0])].grad_date, "%m/%d/%Y")
        if date_compare > today and students_dict[str(row[0])].disc_action != "Y" and row[4] > 3.8:
            scholarship_writer.writerow(row)

# Checks if a student has been disciplined. If so, it writes the row to the file.
with open("DisciplinedStudents.csv", "w", newline="") as csvfile:
    disciplined_writer = csv.writer(csvfile)
    for row in disciplined_students:
        if students_dict[str(row[0])].disc_action == "Y":
            disciplined_writer.writerow(row)
