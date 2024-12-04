# while 1:
#     answer = input("런던,파리,서울 중 영국의 수도는 ?")
    
#     if answer =="런던":
#         print("정답입니다. 런던은 영국의 수도입니다.")
#         break
#     elif answer == "파리":
#         print("파리는 프랑스의 수도입니다.")
#     elif answer == "서울":
#         print("서울은 한국의 수도입니다.")
#     else:
#         print("보기에서 고르세요")
# print()

# #최소공배수
# num1 = int(input("정수 1 입력:")) 
# num2 = int(input("정수 2 입력:"))
# a = 1

# while True:
#     if a % num1 == 0 and a % num2 == 0:
#         break
#     a += 1
    
# print("최공배수는 ",a)


#구구단

while True:
    i = 1
    num = int(input("몇 단?(0을 입력시 구구단 프로그랩 종료) : "))
    if num ==0:
        print("구구단 프로그램을 종료합니다.")
        break
    while i < 10:
        print("%d X %d = %d"%(num,i,num * i))
        i += 1
        