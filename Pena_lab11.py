student_grade = []
grade = input("type student grade (type 'done' to finish): ")
passed = 0
average_grade = 0
passing_percentage = 0

while grade.lower() != 'done':
    student_grade.append(float(grade))
    grade = float(grade)
    if 100>=grade>=40:
        if grade >= 75:
            passed += 1
            passing_percentage = round (passed / len(student_grade), 2)
            grade = input ("type student grade (type 'done' to finish): ")
    else:
        print ("Error: Invalid Grade")
        break
        
    grade = str(grade)
    
    average_grade = round(sum(student_grade) / len(student_grade), 2)
    
print ("Average grade:" , average_grade)  
print ("Number of student passed:" , passed)
print ("Passing %:" , passing_percentage)
