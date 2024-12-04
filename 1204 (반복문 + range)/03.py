# num = int(input("정수 입력: "))
# for i in range (num, 0, -1):
#     print(i, end="")

# for i in range(1, num+1)[::-1]:
#     print(i, end="")
# print()
# for i in range(4):
#     num = int(input("양수 입력:"))
#     if num < 0:
#         print("0을 입력하셨습니다.")
#     elif num == 0:
#         print("0을 입력하셨습니다.")
#     elif num % 2 ==0:
#         print("짝수입니다")
#     elif num % 2 !=0:
#         print("홀수입니다")

#첫 날에 1원을 예금하고, 다음날에는 전날의 두 배를 예금하는
#방식으로 한달(30일)동안 저축한 금액은?

result = 0 #저금합계
money = 1 #저금할 돈
for i in range(30): # 30번 반복
    result += money
    money *= 2
print("저금한 금액 :%d" %result)

print()
result = 0
for i in range(30):
    result += 2 ** i
print (result)
    