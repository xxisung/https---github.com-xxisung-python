#17시 이후에는 집에 간다. 이 미만은 계속 공부를 하자.

# time = int(input("현재 시간은?"))

# if time >= 17:
#     print("집에 가자")
# else:
#     print("공부합시다")


# age = int(input("당신의 나이를 입력하세요 : "))
# if age >= 19:
#     print("당신은 성인",end = " ")
# else:
#     print("당신은 미성년자",end = "")
# print("입니다")

money = True
print("케이크 집을 가서",end = "")

if money: #돈이 있으면(True)
    print("먹는다.")
    print("얌얌")
else: #돈이 없으면(fale)
    print("손가락만 빨고있어.")
    

num = int(input("정수 하나늘 입력하세요 : "))
if num < 0:
    print("%d는 음의 정수"%num,end ="")
else:
    print("%d는 양의 정수"%num,end ="")
print("입니다.")