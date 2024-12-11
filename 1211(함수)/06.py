#자신의 이름 전체를 영어로 입력 받고 '성'과 '이름'을 바꾸는 함수를 만들어
#해당 함수를 통해 바뀐 영문 일므을 출력하시오
def change_name(a,b):
    print(b + " " + a)
firstname = input("성 입력 :")
lastname = input("이름 입력 :")
change_name(firstname, lastname)

def change_name2(a):
    x,y = a.split()
    return y + " " + x
    
    
name = input("이름 성 입력:")
print(change_name2(name))

#numlist 리스트에 정수를 5개 입력 받고 5보다 큰 수만 result리스트에 추가하는 함수를 만드시오

def fiveover(a): #a매개변수에 리스트형이 입력된다
    result = []
    for i in a:
        if i > 5:
            result.append(i)
    return result

numlist = []
for i in range(5):
    numlist.append(int(input("%d번째 정수 입력 : "%(i+1))))
    #numlist에 정수 5개 입력
print(fiveover(numlist))

