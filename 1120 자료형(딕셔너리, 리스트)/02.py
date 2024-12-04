# a = {1:'a'}
# print(a)

# a[2] = 'b'
# print(a)

# a['name'] = "song"
# a[3] = [1,2,3]
# a['age'] = 20
# a = {[1,2,3]:'a'}
# print(a)

mart = {"다이제":1000,"메로나":500,"코카콜라":700,"츄파츕스":500}
#1.mart 딕셔너리 자료형의 key만 모아서 menu 변수에 튜플형으로 보관
#2. value값을 정로수로써 모두 더한 최종 금액을 price에 저장
#3. mart 딕셔너리에 input으로 직접 key와 value 추가 (2개)

#1.
menu = tuple(mart.keys())
print(menu)
price = sum(mart.values())
print(price)

#대입연산자(=)에서는 오른쪽 항의 연산을 완료하여 그 결과를 왼쪽 항에 대입
mart[input("과자이름:")] = int(input("가격:"))
print(mart)

#언패킹 : 오른쪽의 데이터를 왼쪽에 풀어준다
a, b = input("과자:"), int(input("가격:"))
mart[a] = b
print(mart)

