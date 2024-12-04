#세 과목의 점수를 입력 받아 합계와 평균을 구하시오(단 소수점 2자리까지만 출력)
# kor = int(input("국어 : "))
# eng = int(input("영어 : "))
# math = int(input("수학 :"))
# sum = kor + eng + math 
# avr = sum / 3 
# print("합계:%d", "평균:%.2f" %(sum,avr) )

# print("합계:{}", "평균:{:.2f}" .format(sum,avr))


#두 수를 입력 받아 거듭제곱, 첫 번째 수를 두 번째 수로 나눴을 때 몫과 나머지를 각각 구하시오

num1=int(input("정수1: "))
num2=int(input("정수2: "))

print("%d ** %d = %d" %(num1,num2,num1**num2))
print("%d // %d = %d" %(num1,num2,num1//num2))
print("%d %% %d = %d" %(num1,num2,num1%num2))
# %%적어야지 이게 포맷팅 코드가 아니고 글자라고 인식하게 됨
