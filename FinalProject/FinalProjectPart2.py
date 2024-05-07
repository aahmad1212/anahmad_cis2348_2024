# Adil Ahmad
# 2278219
import csv
from datetime import datetime


# Student object to store information about a student. We use default values so we can update attributes as needed.
# GPA is stored as a float so we can compare it in order to determine if a student is eligible for a scholarship.
class Student:
    def __init__(
            self, student_id="null", major="null", first_name="null", last_name="null", gpa=0.0, grad_date="1/1/1970",
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


# Convert to date
def date(a):
    return datetime.strptime(a, "%m/%d/%Y")


# Find closest value
def min_diff_value(lst, trgt):
    def calculate_diff(x):
        return abs(x - trgt)

    return min(lst, key=calculate_diff)


today = datetime.today()

majors_list = []
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
        student = Student(student_id=row[0], major=row[3], first_name=row[2], last_name=row[1], disc_action=row[4])
        students.append(student)
        students_dict[row[0]] = student

with open("GPAList.csv") as csvfile:
    gpa_reader = csv.reader(csvfile)
    for row in gpa_reader:
        for student in students_dict:
            # Matches ID in GPAList with ID of a Student. Updates the GPA attribute with corresponding GPA value.
            if row[0] == students_dict[student].student_id:
                students_dict[student].gpa = float(row[1])

with open("GraduationDatesList.csv") as csvfile:
    grad_reader = csv.reader(csvfile)
    for row in grad_reader:
        for student in students_dict:
            # Updates graduation date attribute of students with their graduation dates.
            if row[0] == students_dict[student].student_id:
                students_dict[student].grad_date = row[1]

# Continuously prompts the user to enter a major or GPA until "q" is entered
while True:
    query = str(input("Enter a student's major and GPA, separated by space (q to quit):\n"))
    if query == "q":
        break
    # Initialize variables
    query_major = None
    query_gpa = None
    found_major = False
    more_one_maj = False
    gpa_found = False
    more_one_gpa = False

    # Extract the major from the query
    for maj in majors_list:
        if maj in query:
            query_major = maj
            query = query.replace(maj, "")
            found_major = True
            break

    # If more than one major was queried, flag it
    if found_major:
        for maj in majors_list:
            if maj in query:
                more_one_maj = True

    # Remove all non-numeric characters from the query to prep it for extracting the GPA
    for ch in query:
        if not ch.isdigit() and ch != "." and ch != " ":
            query = query.replace(ch, "")

    # Split the query
    parts = query.split()

    # Check if we can convert one part of the query into a float- if we can, it's the GPA we're looking to extract
    for part in parts:
        try:
            float(part)
        except ValueError:
            continue
        else:
            query_gpa = float(part)
            query = query.replace(part, "")
            gpa_found = True
            break

    parts = query.split()

    # If there's anything float-able left, it means more than 1 GPA was entered - flag it
    if gpa_found:
        for part in parts:
            try:
                float(part)
            except ValueError:
                continue
            else:
                more_one_gpa = True

    # If more than 1 major or GPA was entered, or if the major or GPA don't exist/weren't entered, no such student
    # Otherwise, check for students matching the query
    if more_one_gpa or more_one_maj or query_major is None or query_gpa is None:
        print("No such student.")
    else:
        print("Your student(s):")
        exact_match = False
        within_quarter = False
        gpa_list = []

        # Find the students within 0.1 of the requested GPA
        for s in students_dict.values():
            if (s.major == query_major and (s.gpa - 0.1) <= query_gpa <= (s.gpa + 0.1) and date(s.grad_date) > today
                    and s.disc_action != "Y"):
                print(
                    f"ID: {s.student_id}\n"
                    f"First Name: {s.first_name}\n"
                    f"Last Name: {s.last_name}\n"
                    f"GPA: {s.gpa}\n"
                )
                exact_match = True

        # If we can't, we let the user know
        if not exact_match:
            print("A student with a GPA within 0.1 of the requested GPA was not found.")

        print("You may, also, consider:")

        # Find the students within 0.25 of the requested GPA, but not 0.1 because we already found them earlier
        for s in students_dict.values():
            if (s.major == query_major and (s.gpa - 0.25) <= query_gpa <= (s.gpa + 0.25)
                    and not ((s.gpa - 0.1) <= query_gpa <= (s.gpa + 0.1))
                    and date(s.grad_date) > today and s.disc_action != "Y"):
                print(
                    f"ID: {s.student_id}\n"
                    f"First Name: {s.first_name}\n"
                    f"Last Name: {s.last_name}\n"
                    f"GPA: {s.gpa}\n"
                )
                within_quarter = True

        # If we can't, let the user know
        if not within_quarter:
            print("A student with a GPA within 0.25 of the requested GPA was not found, excluding students within 0.1"
                  " of the requested GPA.")

        # Build a list of GPAs in order to check which one is the closest.
        if not within_quarter and not exact_match:
            for s in students_dict.values():
                if s.major == query_major and date(s.grad_date) > today and s.disc_action != "Y":
                    gpa_list.append(s.gpa)

            # Returns the GPA that is closest to the requested one.
            min_diff = min_diff_value(gpa_list, query_gpa)

            # Finds the student with the GPA closest to the requested one.
            for s in students_dict.values():
                if s.major == query_major and date(s.grad_date) > today and s.disc_action != "Y":
                    if s.gpa == min_diff:
                        print(
                            "The student with the GPA closest to that requested is:\n"
                            f"ID: {s.student_id}\n"
                            f"First Name: {s.first_name}\n"
                            f"Last Name: {s.last_name}\n"
                            f"GPA: {s.gpa}\n"
                        )
