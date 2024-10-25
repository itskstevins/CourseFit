import math
from courses import *
# Grade points mapping
grade_to_points = {
    "A": 12, "A-": 11, "B+": 10, "B": 9, "B-": 8,
    "C+": 7, "C": 6, "C-": 5, "D+": 4, "D": 3, "D-": 2, "E": 1
}


# Function to convert grades to points
def get_grade_point(grade):
    return grade_to_points.get(grade.upper(), 0)


# Function to calculate KUCCPS cluster points
def calculate_kuccps_cluster_points(grades, core_subjects, total_points):
    r = sum([get_grade_point(grades[subject]) for subject in core_subjects])  # Sum of core subjects points
    R = 48  # Maximum points for 4 subjects
    T = 84  # Maximum points for all 7 subjects

    # Apply the KUCCPS formula
    t = total_points  # Total points from 7 subjects
    cluster_points = math.sqrt((r / R) * (t / T)) * 48
    return round(cluster_points, 3)  # Round to 3 decimal places


# check if a student meets the subject minimum requirements
def meets_subject_requirements(grades, min_grades):
    try:
        for subject, min_grade in min_grades.items():
            if get_grade_point(grades[subject]) < get_grade_point(min_grade):
                return False
        return True
    except KeyError as e:
        print(f"Missing grade for subject: {e}")
        return False


# Sample courses and their requirements


# Function to check course qualification and return qualified universities
def check_qualification(grades, course_info, total_points):
    min_grades = course_info["min_grades"]
    core_subjects = course_info["core_subjects"]

    # Calculate student's cluster points for core subjects
    student_cluster_points = calculate_kuccps_cluster_points(grades, core_subjects, total_points)

    # Check if student meets subject requirements
    if not meets_subject_requirements(grades, min_grades):
        return []

    # Filter universities where student qualifies based on cluster points
    qualified_universities = {
        university_info["INSTITUTION NAME"]:university_info["2023CUTOFF"]
        for university_info in course_info["universities"]
        if student_cluster_points >= university_info["2023CUTOFF"]
    }

    return qualified_universities


# Student input: Enter grades for all subjects
student_grades = {
    "Math": input("Enter Math grade: "),
    "English": input("Enter English grade: "),
    "Kiswahili": input("Enter Kiswahili grade: "),
    "Physics": input("Enter Physics grade: "),
    "Chemistry": input("Enter Chemistry grade: "),
    "Biology": input("Enter Biology grade: "),
    "Computer Studies": input("Enter Computer Studies grade: "),
    "History": input("Enter History grade: "),
    "Geography": input("Enter Geography grade: "),
    "CRE": input("Enter CRE grade: "),
    "Agriculture": input("Enter Agriculture grade: "),
    "Business": input("Enter Business grade: "),

}

total_points = float(input("Enter total points for your 7 subjects: "))

# Compare student qualifications for all courses
qualified_courses = {}

for course_name, course_info in degree_clusters.items():
    qualified_universities = check_qualification(student_grades, course_info, total_points)
    if qualified_universities:
        qualified_courses[course_name] = qualified_universities


 #Output the qualified courses and respective universities
if qualified_courses:
    print("You qualify for the following courses and universities:")
    for course, universities in qualified_courses.items():
       print(f"\n{course}:")
       for index, university in enumerate(universities, start=1):
            print(f" {index}.  {university} ")
else:
    print("You do not qualify for any courses based on the provided grades.")

