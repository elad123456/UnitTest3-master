from unittest import TestCase
from objects_package.Cource import *
from Student import *
from unittest import TestCase, mock
from unittest.mock import patch


class TestCourse(TestCase):
    def setUp(self):
        self.course=Course(4,'QA',4)

    def test_add_student(self):
        # check that the function return false when the parameter is not student
        self.assertFalse(self.course.add_student('student'))
        # check if the function return false when the number of the students is bigger than the max students
        self.course.students_in_course=[Student(1,'a'),Student(2,'b'),Student(3,'c'),Student(4,'d')]
        self.assertFalse(self.course.add_student(Student(5,'e')))
        # check if the function insert into student list the specific student
        self.course.students_in_course = [Student(1, 'a'), Student(2, 'b'), Student(3, 'c')]
        self.assertTrue(self.course.add_student(Student(4, 'd')))

    def test_add_student_full_list(self):
        # check if the function add student untill the list is full
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        student3 = Student(3, 'c')
        student4 = Student(4, 'd')
        student5 = Student(5, 'e')
        self.course.add_student(student1)
        self.course.add_student(student2)
        self.course.add_student(student3)
        self.course.add_student(student4)
        self.assertFalse(self.course.add_student(student5))

    def test_add_student(self):
        # check if the student is added when the valied_student function return true
        with patch('objects_package.Cource.Course.valied_student') as mock_valied_student:
            mock_valied_student.return_value=True
            student1 = Student(1, 'a')
            self.assertTrue(self.course.add_student(student1))

        # check if the student is added when the valied_student function return true
        with patch('objects_package.Cource.Course.valied_student') as mock_valied_student:
            mock_valied_student.return_value = False
            student1 = Student(1, 'a')
            self.assertFalse(self.course.add_student(student1))



    # check if the function delete student from the list
    def test_del_student(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        list1=[student1]
        self.course.del_student(student2.id)
        self.assertEqual(list1,self.course.students_in_course)

    # check if the function delete student from the list if it get unexist ID
    def test_del_student_unexist_id(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        list1=self.course.students_in_course
        self.course.del_student(3)
        self.assertEqual(list1, self.course.students_in_course)

    # check if the function can get id that is not int
    def test_del_student_notint_arg(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        list1 = self.course.students_in_course
        # check if the function return a TypeError
        with self.assertRaises(TypeError):
            self.course.del_student('2')
        self.assertEqual(list1, self.course.students_in_course)

    # check if the function add factor for each student in the course
    def test_add_factor(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        print(self.course)
        self.course.students_in_course[0].add_grade('sql',80)
        self.course.students_in_course[0].add_grade('python', 80)
        self.course.students_in_course[1].add_grade('sql', 80)
        self.course.students_in_course[1].add_grade('python', 80)
        print(student1)
        print(student2)
        print(self.course)
        self.course.add_factor('sql',10)
        print(self.course)
        self.assertEqual(self.course.students_in_course[0].subjects_grades['sql'],88)
        self.assertEqual(self.course.students_in_course[0].subjects_grades['python'], 80)
        self.assertEqual(self.course.students_in_course[1].subjects_grades['sql'], 88)
        self.assertEqual(self.course.students_in_course[1].subjects_grades['python'], 80)

    # check if the function add factor for each student in the course for invalied cases
    def test_add_factor_invalied_cases(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        print(self.course)
        self.course.students_in_course[0].add_grade('sql', 80)
        self.course.students_in_course[0].add_grade('python', 80)
        self.course.students_in_course[1].add_grade('sql', 80)
        self.course.students_in_course[1].add_grade('python', 80)
        # check if the function return TypeError when the subject arg is invalied
        with self.assertRaises(TypeError):
            self.course.add_factor(2, 10)
        # check if the function return TypeError when the factor arg is invalied
        with self.assertRaises(TypeError):
            self.course.add_factor('sql', '10')
        # check if the function return TypeError when the factor arg isnt between 0-100
        self.assertFalse(self.course.add_factor('sql', -10))

    # check if the function return true when the student is not exist an false when he exists
    def test_valied_student(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        student3 = Student(3, 'c')
        self.assertTrue(self.course.valied_student(student3))
        self.course.add_student(student3)
        self.assertFalse(self.course.valied_student(student3))

    # invalied cases
    def test_valied_student(self):
        student1 = Student(1, 'a')
        student2 = Student(2, 'b')
        self.course.add_student(student1)
        self.course.add_student(student2)
        with self.assertRaises(TypeError):
            self.assertTrue(self.course.valied_student('student3'))





