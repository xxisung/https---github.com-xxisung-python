# in 연산자
print('a' in ('a','b','c'))
print(7 in [1,2,3,4,5,6])
print('a' in "busanit")
print('b' in {1:'a',2:'b',3:'c'})
print(3 in {1:'a',2:'b',3:'c'})


pocket = ["phone", "card", "신사임당" ]

print("배떡을 먹고 싶은데 주머니에 현금이 있나?")

if "신사임당" in pocket:
    print("떡볶이에 라면 사리 추가")
else:
    print("카드 결제")