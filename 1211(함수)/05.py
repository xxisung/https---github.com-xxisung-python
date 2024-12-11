#정수 하나를 전달받아 1부터 입력 받은 수까지의 누적 합계를 구하는 함수를 만드시오
#(매개 변수(입력값)과 반환값(출려값)이 모두 있는 함수
def total(a):
    sum = 0
    for i in range(a+1):
        sum += i
        return sum
num = int(input("정수 입력:"))
print("1부터 {}까지의 합계는 : {}".format(num,total(num)))


#정수 하나를 전달 받아 해당 정수가 3의 배수인지 출력해주는 함수를 만드시오
#(매개변수 (입력값)는 있고 반환값(출려값)이 없는 함수
def ThreeMul(a):
    if a % 3 == 0:
        print("%d는 3의 배수입니다." %a)
    else:
        print("%d는 3의 배수가 아닙니다." %a)
num1 = int(input("정수 입력:"))
ThreeMul(num1)
#두 수를 입력 받아 더 큰 수를 return 하는 함수를 만드시오.
#(매개변수(입력값)는 없고 반환값(출려값)은 있는 함수)
def Compare():
    #a = int(input("정수1:"))
    #b = int(input("정수2:"))
    a,b = map(int(input("정수 두 개 입력:").split))
    if a >= b:
        return a
    else:
        return b
print("두 수 중에 큰 수는 : %d" %Compare())

#map(함수,입력값들) 함수에 여러 개의 데이터를 한번에 적용
#map(int, "5 6".split())


#정수 하나를 입력 받아 절대값을 구하는 함수를 만드시오
#(매개변수(입력값)와 반환값(출력값)이 없는 함수)

def Abs():
    a = int(input("정수 입력:"))
    if a< 0:
        print("%d의 절대값 : %d" %(a,-a))
    else:
        print("%d의 절대값 : %d" %(a,-a))
Abs()