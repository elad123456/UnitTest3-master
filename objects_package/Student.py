class Student:
    def __init__(self,id,name):
        self.name=name
        self.id=id
        self.subjects_grades={}
    def add_grade(self,subject,grade):
        if 0<=grade<=100 and type(subject) is str and subject not in self.subjects_grades:
            self.subjects_grades[subject]=grade
        else:
            return False
    def __repr__(self):
        return f"name: {self.name} id: {self.id} subjects+grades: {self.subjects_grades}"
    def calc_factor(self,sub,percent):
        if 0<=percent<=100:
            a = float(percent / 100) + 1
            if int(self.subjects_grades[sub]*a)>100:
                self.subjects_grades[sub]=100
            else:
                self.subjects_grades[sub]=int(self.subjects_grades[sub]*a)
        else:
            return False
    def average(self):
        sum=0
        if len(self.subjects_grades)>0:
            for i in self.subjects_grades:
                sum+=self.subjects_grades[i]
            return sum/len(self.subjects_grades)
        else:
            return False
    def __eq__(self, other):
        if self.id==other.id and self.name==other.name:
            return True
        else:
            return False

