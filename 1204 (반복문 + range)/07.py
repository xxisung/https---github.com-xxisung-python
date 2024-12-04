print("★")
print("★★")
print("★★★")
print("★★★★")
print("★★★★★")
for i in range(1,6):
    for j in range(1,6):
        print("★",end = "")
    print("")
print("=====================") 
#별의 위치를 알아보자
for i in range(5):#바깥 루프, 줄을 담당
    for j in range(5):#안쪽 루프, 한줄당 몇개를 표시할지 결정
        print("j:",j,sep="",end="")
    print("i:",i,"\\",sep="")
print()    
#사각형으로 별 출력하기
for i in range(5): #행의 개수
    for j in range(5):#별의 개수
        print("★",end=" ")
    print()
print()

#한줄로 별 출력
for i in range(5):
    for j in range(5):
        if j == i:
            print("★",end="")
    print()
print()

#계단식으로 별 출력하기
for i in range(5):
    for j in range(5):
        if j <= i:
            print("★",end=" ")
    print()
print()

#뱔 한개를 대각선 방향으로 출력
for i in range(5):
    for j in range(5):
        if j == i:
            print("★",end=" ")
        else:
            print(" ",end=" ")
    print()
print()