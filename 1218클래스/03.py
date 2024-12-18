#잘못된 예
class Person:
    name = "동수"
    def say_hello(self):
        print("안녕 나는 ",self.name)
        
white = Person()
dongsu = Person()
jenny = Person()

white.say_hello()
dongsu.say_hello()
jenny.say_hello()

print()
print()
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def say_hello(self,to_name):
        print("안녕!", to_name, "나는",self.name)
white = Person("화이트",20) #white는 Person()클래스에 의해 만들어진 인스턴스
dongsu =Person("동수",19)
jenny = Person("제니",21)

white.say_hello("동수")
dongsu.say_hello("제니")
jenny.say_hello("화이트")


#자신을 소개하는 메소드를 제작하자 . introduce
#나의 이름은 화이트이고 나이는 20살이야.
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def say_hello(self,to_name):
        print("안녕!", to_name, "나는",self.name)
        
    def introduce(self):
        print("나의 이름은",self.name,"이고 나이는",self.age)
white = Person("화이트",20) #white는 Person()클래스에 의해 만들어진 인스턴스
dongsu =Person("동수",19)
jenny = Person("제니",21)

white.say_hello("동수")
dongsu.say_hello("제니")
jenny.say_hello("화이트")
white.introduce