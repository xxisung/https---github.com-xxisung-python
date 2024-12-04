#continue문
#반복문 내 continue의 아래 코드를 실행하지 않고
#다시 조건식으로 올라가게 해 주는 역할
#정수를 입력받아 그 정수 사이의 3의 배수만을 출력하자.


# num = int(input("정수 입력 :"))
# print("3의 배수 출력 :")
# i = 0
# while i < num:
#     i += 1
#     if i % 3 != 0:
#         continue
#     print(i)
    


#1 ~ 10000까지의 합을 구하시오. 단 3의 배수는 제외하고 3의 배수이면서
#5의 배수는 제외하지 않는 조건으로 구하시오
# i = 0
# sum = 0
# while i < 10000:
#     i += 1
#     if i % 3 == 0 and i % 5 == 0:
#         sum += i
    
#     if i % 3 == 0:
#         continue
#     sum += i
    

# print("합계 : %d"%sum)

#자판기에 지폐와 동전들을 넣어 음료수를 선택하고, 거스름돈을 받으시오
#콜라 1200원 사이다 1200원 조지아 1000원 컨피던스 600원이며 종료를 누르면 잔액이 반환된다
# 자판기에 없는 메뉴를 선택 시 에러메시지 출력
menu = {"콜라":1200,"사이다":1200,"조지아":1000,"컨피던스":600}
price = int(input("돈을 넣으세요 : "))
while True:
    print("========자판기========")
    print("""     
    콜라 : 1,200원 
    사이다 : 1,200원 
    조지아 : 1,000원 
    컨피던스 : 600원
    >>>종료
    """)
    
    select = input("음료를 선택하세요 : ")
    if select == "종료"    :
        print("잔돈 : %d" %price)
        print("자판기 프로그램을 종료합니다.")
        break
    elif select not in menu:
        print("없는 음료수 입니다.")
    elif price >=menu[select]:
        price -= menu[select]
        print("%s를 샀어요"%select)
        print("잔액 : %d"%price)
    elif price < menu[select]:
        print("잔액이 부족합니다.")    