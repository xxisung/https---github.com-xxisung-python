num = int(input("출력할 별의 행 :"))

for i in range(num): #i는 몇 줄을 출력할 것인지?
    for j in range(i+1):
        print("☆",end=" ")
    print()


num1 = int(input("출력할 별의 행의 수 :"))
for i in range(num1):#i는 몇행을 출력할건지?
    #공 백 찍는 반복문
    for j in range(num1 - i - 1): #num1이 5일시 4-3-2-1
        print(" ",end="")
    #별 찍는 반복문
    for j in range(i + 1):
        print("☆",end=" ")      
    print()
            
num2 = int(input("출력할 별의 행의 수 :"))

for i in range(num2):#i는 몇행을 출력할건지?
    #공 백 찍는 반복문
    for j in range(num2 - i - 1): #num1이 5일시 4-3-2-1
        print(" ",end="")
    #별 찍는 반복문
    for j in range(i * 2 + 1):
        print("☆",end=" ")      
    print()
            