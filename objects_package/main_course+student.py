from Cource import *
from Student import *
course=Course(123,'python',4)
'''מכניס לתוך קורס נושאים ואת המרצים שלהם'''
sub=input("enter a subject: ")
while sub!='stop':
    teacher=input("enter the name of the teacher: ")
    course.subjects_teacher[sub]=teacher
    sub = input("enter a subject: ")
print(course)


'''מכניס לתוך קורס רשימה של תלמידים כאשר לכל תלמיד אני מכניס את הנושאים של הקורס ואת הציונים'''
id=int(input("enter an id: "))
while id!=0:

    if len(course.students_in_course)<course.max_students:
        name=input("enter the name of the student: ")
        student=Student(id,name)
        for i in course.subjects_teacher:
            grade=int(input(f"enter the grade of {name} in {i}:"))
            student.add_grade(i,grade)
    else:
        break
    print(student)
    course.add_student(student)
    print(course.students_in_course)
    id = int(input("enter an id: "))
print(course)


subject=input("enter a subject: ")
factor=input("enter a factor: ")
course.add_factor(subject,factor)

'''בודק למי יש את הממוצע המינימלי ומוחק אותו מהרשימה במידה ויש כמה אני מוחק את כולם'''
min=course.students_in_course[0].average()
index=[]
counter=0
for student in course.students_in_course:
    if student.average()==min:
        index.append(counter)
    if student.average()<min:
        index=[counter]
        min=student.average()
    counter+=1
    for i in index:
        del course.students_in_course[i]

print(course)





