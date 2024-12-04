#메뉴를 보고 만두 개수를 입력 받아 결제 금액을 출력하시오
#예원 손만두 메뉴>
#안녕하새우 만두 1개: 1000원 10개 이상 구매시 15%할인, 100개 이상 구매시 25%할인 현금결제 시 결제금액의 10%할인
mandu = int(input("만두 개수를 입력하세요:"))
price= mandu * 1000
if mandu < 10:
    print("가격 : %d원, 현금결제가 : %d원"%(price,price * 0.90))
elif mandu < 100:
    print("가격 : %d원, 현금결제가 : %d원"%(price*0.85,(price *0.85)* 0.90))
else:
        print("가격 : %d원, 현금결제가 : %d원"%(price * 0.75,(price * 0.75)*0.90))

#선생님 해설
dumpling = int(input("만두 개수 입력 :"))

price = 1000 

if dumpling > 0 and dumpling <10:
    #price = price * dumpling
    price *=dumpling #복합연산자
elif dumpling >= 10 and dumpling <100:
    price*= 0.85 * dumpling
elif dumpling >= 100:
    price *= 0.75 * dumpling
else: #0보다 작은 경우
    print("잘못된 개수 입니다.")
    
print("가격%d원, 현금결제가:%d원" %(price, price*0.9))