class Student:
    def __init__(self,data):
        tmp = data.split("|")
        self.name = tmp[0]
        self.age = tmp[1]
        self.grade = tmp[2]
    def print_age(self):
        print(self.age)
    def print_grade(self):
        print("%s님 당신의 점수는 %s입니다."%(self.name,self.grade))
student1 = Student("송진우|29|A")
student1.print_age()
student1.print_grade()
