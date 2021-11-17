from unittest import TestCase
from objects_package.Student import *


class TestStudent(TestCase):
    def setUp(self):
        print("began")
        self.student=Student(123,'elad')
    def test_add_grade(self):
        # check if the add succeed
        self.student.add_grade('sql', 100)
        self.assertEqual(self.student.subjects_grades,{'sql':100})
        # check if the function return false if the grade is over 100
        self.assertFalse(self.student.add_grade('sql', 101))
        # check if the function return false if the grade is under 0
        self.assertFalse(self.student.add_grade('sql', -1))
        # check if the function return false if the subject is under not string
        self.assertFalse(self.student.add_grade([], 50))

    def test_calc_factor(self):
        #check if the function update the grade corractly
        self.student.subjects_grades={'sql':90,'python':50}
        self.student.calc_factor('sql', 10)
        self.student.calc_factor('python', 10)
        self.assertEqual(self.student.subjects_grades,{'sql':99,'python':55})
        # check if the factor is over 100 the grade will be 100
        self.student.subjects_grades = {'sql': 90}
        self.student.calc_factor('sql', 50)
        self.assertEqual(self.student.subjects_grades, {'sql': 100})
        # check if the percents more than 0
        self.student.subjects_grades = {'sql': 90}
        self.student.calc_factor('sql', -10)
        self.assertNotEqual(self.student.subjects_grades, {'sql': 81})

    def test_average(self):
        #check if the function update the grade corractly
        self.student.subjects_grades = {'sql': 90, 'python': 50}
        self.assertEqual(self.student.average(),70)
        #check what happend if the diraction is empty
        self.student.subjects_grades = {}
        self.assertFalse(self.student.average())