#문제 1 1부터 입력 받은 숫자까지의 누적합계를 구하는 코드를 작성하시오.
# num = int(input("숫자 입력 :"))
# count = 1#초기값
# sum = 0 #누적 합계
# while count <= num:
#     sum += count
#     count += 1
# print("1부터 %d까지의 누적합계 : %d"%(num,sum))

# #문제2 While을 이용하여 Hello,Python을 10번 출력하시오
# i = 0
# while i< 10:
#     print("Hello,Python")
#     i += 1
    

#문제3 정수를 반복하여 입력 받아 입력 받은 모든 수의 합계를 출력하시오(0을 입력할 때까지 반복)

# num1 = 1
# sum = 0
# while num1: #num1이 0이되어야 종료
#     num1 = int(input("정수 입력(0입력시 종료) : "))
#     sum += num1
#     print("모든수의 합%d :"%sum)
#     print()
    
    
#문제4 입력된 수의 거꾸로 수를 출력하시오(//,%연산자 사용) 
#ex 정수를 입력하세요 : 1234
#거꾸로 수는 : 4321 입니다
#1234 % 10 -> 4
#1234 // 10 -> 123
#123 % 10 -> 3
#123 // 10 ->12
#12 % 10 ->1
#12 // 10->1
#1 % 10 ->1
#1 // 10 ->0


# num = int(input("정수 입력 :"))
# while num !=0:
#     print(num%10, end="")
#     num = num // 10
# print()


#문제5 정수를 입력 받아 그 수 만큼의 배수를 출력하시오.
#ex>정수를 입력하세요:4
#4 8 12 16 (4의 배수를 4개 까지 출력)
num = int(input("정수입력 : "))
count = 1
while count <= num:
    print("%d"%(num*count),end=" ")
    count += 1