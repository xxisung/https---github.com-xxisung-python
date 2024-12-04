#이중 구조 루프
for i in range(3): # 바깥쪽 루프
    print("========{}학년========".format(i+1))
    for j in range(5): #안쪽 루프
        print("---{0}학년-{1}반---".format(i+1,j+1))
        
        
a, b = 2, 1
while a < 10:
    while b < 10:
        print("%d * %d = %d"%(a,b,a*b))
        b +=1
    a += 1
    b = 1


for a in range(2,10):
    for b in range(1,10):
        print("%d * %d = %d "%(a,b,a*b))
        

