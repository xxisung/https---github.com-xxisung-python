# num = 0
# while True:
#     print("""
#           ======메뉴======
#             1. 정수 입력
#             2. 입력된 정수 출력
#             3. 종료
#             """)
#     select = int(input("메뉴 선택:(1,2,3) : "))
#     if select == 1:
#         num = int(input("정수 입력 : "))
#     elif select == 2:
#         print("입력된 정수 : {}" .format(num))
#     else:
#         #종료
#         break
    

# count = 0
# sum = 0
# num = 1
# while num != 0:
#     count += 1
#     num = int(input("정수 입력 : "))
#     sum += num
# count -= 1
# avg = sum/count
# print("평균 %.2f"%avg)


MonsterHP = 1000
turn = 0
while MonsterHP >=0:
    turn += 1
    print("[========{0}턴========]".format(turn))
    print("어떤 기술을 사용하시겠습니까?")
    print("1 : 기본공격\n2 : 기술공격")
    skill = int(input("선택 : "))
    if skill == 1:
        print("몬스터에게 300의 데미지를 입혔습니다.")
        MonsterHP -= 300
    elif skill == 2:
        print("몬스터에게 500의 데미지를 입혔습니다.")
        MonsterHP -=500
    print("몬스터 체력 : {0}\n".format(MonsterHP))
print("몬스터가 죽었습니다.")