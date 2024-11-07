student_grades = []
passed = 0
grade_input = True

while True:
    grade = input("Type student grade (type 'done' to finish): ")
    
    if grade.lower() == 'done':
        break
    
    grade = float(grade)
    
    if grade < 40 or grade > 100:
        print("Invalid grade")
        grade_input = False
        break
    
    student_grades.append(grade)
    if grade >= 75:
        passed += 1

if grade_input and student_grades:
    average_grade = round(sum(student_grades) / len(student_grades), 2)
    passing_percentage = round(passed / len(student_grades) * 100, 2)
    
    print("Average grade:", average_grade)
    print("Number of students passed:", passed)
    print("Passing percentage:", passing_percentage)
