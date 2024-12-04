#절대값을 구하는 함수 abs
#print(abs(-7))

#현재 건물에는 엘레베이터 2대가 있고,
#A엘리베이터는 5층에 B 엘리베이터는 7층에 있다.
#현재 내가 있는 층수를 눌러 가장 가까운 엘리베이터를 움직이시오.
#(층 수의 개수의 차이가 같은 경우 B 엘리베이터가 움직인다.)
#(절대값을 사용해서 A와 B 엘리베이터의 차이를 구하여 움직인다.)

floor = int(input("층 입력:"))
A = 5
B = 7
if abs(A - floor) > abs(B - floor):
    print("B엘리베이터가 움직인다")
else:
    print("A엘리베이터가 움직인다")

#선생님 풀이
A = 5
B =7
current_floor = int(input("현재 층:" ))
A = abs(current_floor - A)
B = abs(current_floor - B)
if A< B:
    print("A엘리베이터가 움직여요")
else:
    print("B엘리베이터가 움직여요")