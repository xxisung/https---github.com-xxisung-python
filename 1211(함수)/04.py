# num = int(input("정수 입력:"))
# if num % 2== 0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
# num = int(input("정수 입력: "))
# if num % 2 ==0:
#     print("짝수입니다.")
# else:
#     print("홀수입니다.")
    


# def odd_even(num):
#     if num % 2 == 0:
#         print("짝수입니다.")
#     else:
#         print("홀수입니다.")
# num = int(input("정수 입력:"))
# odd_even(num)
# odd_even(int(input("정수 입력:")))

def total(a):
    sum = 0
    for i in range(1,a+1):
        sum += i
    return sum
result = total(10)
print("누적합계1 :",result)
print("누적합계2 :",total(20))

def power(a,b):
    result = 1
    for i in range(b):
        result*=a
    return result
print(power(2,4))
print(power(2,10))
print(power(10,4))
