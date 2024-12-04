#정수를 입력 받아 소수인지 판별하시오
#소수는 1과 자신으로만 나눠지는 수
#나눠지는 회수가 2번인 수
num = int(input("정수를 입력하세요 : "))
dcount = 0 #나눠진 횟수를 저장

for i in range(1, num+1):
    if num % i == 0:
        dcount += 1
if dcount == 2:
    print("%d 는 소수입니다."%num)
else:
    print("%d는 소수가 아닙니다."%num)  

#정수 두개를 입력 받아 두 수의 공약수를
#모두 출력하시오, 최대공약수도 구해주세요

#방법 1 리스트에 공약수를 저장
Max_list=[]
# MAX변수를 만들어서 공약수중에 가장 큰 수를 대입
# 12 : 1,2,3,4,6,12
# 15 : 1,3,5,15
MAX = 0 
num1,num2 = int(input("정수1:")),int(input("정수2:"))
if num1 > 0 and num2 > 0:
    for i in range(1, num1 + 1) :
        if num1 % i == 0 and num2 % i == 0: #공약수
            Max_list.append(i)#공약수를 리스트에 추가
            print(i, end = " ")
            MAX = i
print("")
print("최대공약수 : %d"%MAX)
print("최대공약수 : %d"%(max(Max_list)))