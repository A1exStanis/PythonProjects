# 5. Find missing subjectsYou are a teacher at a school, and you have just finished grading a set of exams for your students.
# Each student's exam is represented as a tuple containing their name, their score, and the subject of the exam. 
# You want to identify which subjects were not passed by all students so that you can give extra attention to those subjects in your future lessons. 
# Passing is defined as a score of 60 or higher. Your task is to write a Python program that reads in a list of student exams, 
# identifies the subjects that were not passed by all students, and outputs a set of those subjects.

def get_subjects_not_passed_by_all_students():
    student_exams = [
        ("Alice", 85, "Math"),
        ("Bob", 59, "Math"),
        ("Charlie", 65, "Math"),
        ("Alice", 90, "Science"),
        ("Bob", 80, "Science"),
        ("Charlie", 32, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]
    exams = {}
    for name, mark, subject in student_exams:
        exams[mark] = name, subject
        if mark < 60:
            print(f"{name} didn`t pass {subject}")            

get_subjects_not_passed_by_all_students()