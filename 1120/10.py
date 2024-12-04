# 정수 하나를 입력 받아 5의 배수인 경우 출력하시오

num = int(input("숫자를 입력하세요 : "))
if num %5 == 0:
    print("5의 배수 입니다." %num)
else:
    print("5의 배수가 아닙니다."%num)
    
#정수 하나를 입력 받아 짝수, 홀수를 구분하시오

num1 = int(input("숫자를 입력하세요 : "))
if num1 % 2 == 0:
    print("짝수 입니다."%num1)
else:
    print("홀수 입니다."%num1) 


# #두 수를 입력 받아 첫 번째 수가 두 번째 수의 배수인지 출력하시오
num2 = int(input("숫자를 입력하세요 : "))
num3 = int(input("숫자를 입력하세요 : "))
if num2 %num3 == 0:
    print("첫번째수는 두번째수의 배수입니다")
else:
    print("첫번째수는 두번쨰수의 배수가아닙니다")
    
#(언패킹) 방법
num9, num10 = int(input("첫번째 정수:")),int(input("두번째 정수:"))
if num9 % num10 == 0: 
    print("%d는 %d의 배수입니다."%(num9,num10))
else:
    print("%d는 %d의 배수가아닙니다."%(num9,num10))
#두 수를 입력 받아 더 큰 수가 짝수이면 출력하시오
num4 = int(input("첫번째 숫자를 입력하세요 : "))
num5 = int(input("두번쨰 숫자를 입력하세요 : "))
if num5 > num4:
    if num5 % 2 == 0:
        print(num5)
else:
    if num4 % 2 == 0:
        print(num4)        
#언패킹
num11, num12 = int(input("첫번째 정수:")),int(input("두번째 정수:"))
if num11 > num12:
    if num11 % 2 == 0:
        print("%d은 %d보다 크면서 2의 배수입니다." %(num11,num12))
if num11 < num12:
    if num11 % 2 == 0:
        print("%d은 %d보다 크면서 2의 배수입니다." %(num12,num11))


# 두 수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오
num6 = int(input("첫번째 숫자를 입력하세요 : "))
num7 = int(input("두번쨰 숫자를 입력하세요 : "))
sum = num6 + num7
if sum % 2 == 0:
    if sum % 3 ==0:
        print(sum)
#강사님 풀이
num13, num14 = int(input("첫번째 정수:")),int(input("두번째 정수:"))
sum1 = num13 + num14
if sum1 % 2 == 0 and sum1 %3 ==0:
    print("%d는 짝수이면서 3의 배수입니다." %sum1)
# 정수 하나를 입력 받아 절대값을 구하시오
num8 = int(input("숫자를 입력하세요 : "))
if num8 > 0:
    print(num8)
else:
    print(num8 * -1 )
#강사님 풀이
# 정수 하나를 입력 받아 절대값을 구하시오
num15 = int(input("정수 입력 : "))
if num8 < 0:
    print("%d의 절대값은 %d 입니다."&(num8, -num8))
else:
    print("%d의 절대값은 %d 입니다."&(num8, num8))
