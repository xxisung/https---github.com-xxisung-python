#현재 가진 돈으로 점심을 뭐 먹을건지 정하는 코드 작성
money = int(input("점심 먹자. 얼마있니? : "))

# if money >= 50000:
#     print("소고기 먹으러 가자.")
# if money >= 30000:
#     print("돼지고기 먹자.")
# if money >= 10000:
#     print("하나돈까스 먹자.")
# else:
#     print("알바를 해야 겠다.")

if money >= 50000:
    print("소고기 먹자")
else:
    if money >=30000:
        print("삼겹살 먹자")
    else:
        if money >= 10000:
            print("하나돈까스 먹자")
        else:
            print("편의점 도시락 먹자, 알바 하자.")
            

money = int(input("얼마있니? 머 먹을래?"))

if money >= 100000:
    print("초밥 먹자.")
elif money >= 70000:
    print("한우 먹자")
elif money >= 50000:
    print("곱창 먹자")
elif money >= 30000:
    print("김밥 먹자") 
else:
    print("용돈 받자")