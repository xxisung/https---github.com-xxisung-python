#반복문
for i in range(10):#반복 횟수가 명시적으로 나타난 경우
    print("안녕 민지야 머해?")
    print("안녕 동수야 그냥 있어")
print()
i = 0
while i < 5: #조건이 참일때까지 반복한다.
    print(i)
    print("안녕 민지야 머해?")
    print("안녕 동수야 그냥 있어")
    i += 1
print()
while True:#무한 반복 : 조건에 변수가 없기 때문에 계속 반복하는 구조
    print(i)
    print("안녕 민지야 머해?")
    print("안녕 동수야 그냥 있어")
    i += 1
    if i > 10:
        break

print("열 번 찍어 안 넘어가는 나무 없다")
hit = 0
while hit < 10:
    hit += 1
    print("나무를 %d번 찍었습니다."%hit)
print("나무가 넘어갔습니다.")