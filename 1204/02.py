#1부터 10까지의 합계를 구해보자.
sum = 0
for i in range(1,11):
    sum += i
print("1부터 10까지의 합계 :",sum)

#놀이동장에 입장료 계산
total_price = 0
ages = [22,21,17,33,4,29,19,6]
#20세 이상은 8,000원이고 19~10세는 5,000원이며 9살 이하는 2,500원이다.
#총 입장료 합계는?
for age in ages:
    if age >= 20:
        total_price += 8000
    elif age >= 10:
        total_price += 5000
    else:
        total_price += 2500
print("총 입장료는 %d원 입니다."%total_price)

#범인을 찾아보세여
suspects = ["거위","새","암컷"],["푸들","개","수컷"],["비글","개","암컷"]
for suspect in suspects:
    if suspect[1] == "개" and suspect[2] == "암컷" :
        print("범인은",suspect[0],"입니다.") 
        
print()
for index, value in enumerate(range(3,10)):
    print(index,value)
    

#문제 : 1부터 10까지 홀수의 합게를 구하세요

sum = 0
for i in range(1,11):
    if i % 2 == 1:
        sum += i
print("1부터 10까지 홀수의 합계 :",sum)

    