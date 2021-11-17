from Student import *
class Course:
    def __init__(self,num,name,max):
        self.course_num=num
        self.course_name=name
        self.max_students=max
        self.subjects_teacher={}
        self.students_in_course=[]
    def __str__(self):
        return f"number of the course: {self.course_num}, name of the course {self.course_name}, subjects and their teachers: {self.subjects_teacher}, students:{self.students_in_course}"
    def add_student(self,student:Student):
        if type(student) is Student and len(self.students_in_course)<self.max_students and self.valied_student(student):
            self.students_in_course.append(student)
            return True
        else:
            return False

    def add_factor(self,sub,factor):
        if type(sub)==str and type(factor)==int:
            for student in self.students_in_course:
                if sub in student.subjects_grades:
                    student.calc_factor(sub, factor)

        else:
            raise TypeError("the argument must be int")

    def del_student(self,idp):
        if type(idp)!=int:
            raise TypeError("the argument must be int")
        for student in self.students_in_course:
            if student.id == idp:
                 self.students_in_course.remove(student)
    def valied_student(self,student:Student):
        if type(student)==Student:
            if student in self.students_in_course:
                return False
            else:
                return True
        else:
            raise TypeError("invalied student")