#주차장에 주차를 하려고 한다. 30분까지의 기본요금은 1000원이고 10분당 500원씩의 추가요금을 받는다
#주차한 시간을 입력 받아 주차요금을 출력 하시오. (% 나머지기호를 적절하게 사용)

time = int(input("주차한 시간을 입력하세요 : "))
price = 1000

if time > 0 and time <= 30:
    print("주차요금은 %d원입니다."%price)
elif time>30:
    #time = time - 30
    time -= 30 # 추가 시간계산식 (복합 연산자)
    if time % 10 ==0:
        price += (time // 10 ) * 500
    else:
        price += (time // 10 ) * 500 +500
    print("주차요금은 %d원입니다."%price)
else:
    print("시간을 잘못 입력 했습니다.")