#두 수를 입력 받아 그 두 수로 사칙연산을 하는 함수 네 개를 만드시오
#sum,sub,mul,divi 함수를 선언하고 while 반복문과 if를 이용하여
#한 번 실행 후 다시 다른 수를 입력 받을 수 있도록 만드시오
#(계산 방식 5를 선택일시 종료)
def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def divi(a,b):
    return a // b

while 1:
    num1,num2 = int(input("첫번째 정수:")),int(input("두번째 정수:"))
    print("1.덧셈\n2.뺄셈\n3.곱셈\n4나눗셈\n5종료\n")
    select = int(input("계산할 방식을 선택하세요 : "))
    if select == 1:
        print("%d + %d = %d" %(num1,num2,sum(num1,num2)))
    elif select ==  2:
        print("%d - %d = %d" %(num1,num2,sub(num1,num2)))
    elif select ==  3:
        print("%d * %d = %d" %(num1,num2,mul(num1,num2)))    
    elif select ==  4:
        print("%d // %d = %d"%(num1,num2,divi(num1,num2)))
    elif select == 5:
        break
    else:#잘못 입력한경우
        print("다시 입력하세요.")

