def chat(name1,name2,age):
    print("%s : 너는 몇살이니?" %name1)
    print("%s : 나는 %d살이야." %(name2,age))
    
chat ("알렉스","윤하",27)
print()

def dsum(a,b):
    result = a + b
    return  result
    #너가 왔던 곳으로 돌아가라
print(dsum(1,2))
print()
print()
def funcion():
    print("A")
    print("B")
    return 
    print("C")
    print("D")
    
print(funcion())
#인사하는 함수를 작성해보자
#나이가 10살 미만이면 안녕, 20살 이하 안녕하세요
#21살 이상은 안녕하십니까
def hello(name,age):
    if age < 10:
        print("안녕,",name)
    elif age <= 20:
        print("안녕하세요,",name)
    else:
        print("안녕하십니까?",name)
hello("민지",9)
hello("예원",23)
hello("해린",19)
