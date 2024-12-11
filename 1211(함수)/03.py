#여러 가지 형태의 함수
#매개변수가 존재하고 반환하는 함수
def avg1(a,b):
    result = (a+b)/2
    return result
x = int(input("정수1:"))
y = int(input("정수2:"))
print("평균:",avg1(x,y))
#매개변수가 존재하고 반환하지 않는 변수
def avg2(a,b):
    result = (a+b)/2
    print("평균: ",result)
x = int(input("정수1:"))
y = int(input("정수2:"))
avg2(x,y)

#매개변수가 존재하지 않고, 반환하는 함수
def avg3():
    x = int(input("정수1:"))
    y = int(input("정수2:"))
    result = (x+y)/2
    return result
print("평균:",avg3())

#매개변수가 존재하지 않고, 반환하지 않는 함수
def avg4():
    x = int(input("정수1:"))
    y = int(input("정수2:"))
    result = (x+y)/2
    print("평균:",result)
avg4()
