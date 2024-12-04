print(range(5))
print(list(range(5)))
print(tuple(range(5)))
print(list(range(3,9)))
print(list(range(1,10,2)))

L = list(range(10))
print(L)
print(L[::2])
print(L[::-1])
print()
for i in range(5): #0부터 4까지의 리스트를 생성하고 하나씩 매개변수에 대입
    print("i는 ",i,"입니다.")
print()
for i in range(3,10):
    print("i",i)
    