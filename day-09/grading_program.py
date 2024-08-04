student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        student_grades[key] = "outstanding"
        continue
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectation"
        continue
    elif student_scores[key] >= 71 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
        continue
    elif student_scores[key] <= 70 and student_scores[key] >= 0:
        student_grades[key] = "fail"
        continue
    else:
        print("Invalid score")
        break

print(student_grades)