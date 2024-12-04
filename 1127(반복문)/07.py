# numbers = [0,1,2,3,4]

# for num in numbers:
#     print("num은 ", num)
  
  
# 100이상 출력  
# numbers = [401,103,11,111,111,1109]
# for number in numbers:
#     if number >= 100:
#         print("100 이상의수 : {}" .format(number))
   

# 60점 이상 합격
# jumsu = (90,50,60,80,40)
# number = 1
# for i in jumsu:
#     if i >=60:
#         print("{}번쨰 학생 : 합격" .format(number))
#         number += 1

#     else:
#         print("{}번쨰 학생 : 불합격" .format(number))
#         number += 1
        


# people = {"송새봄":29,"송여름":16,"송가을":32,"겨울":5}
# minor = [] #미성년자
# adult =[]

# for a in people:
#     if people[a] <20:
#         print("{0}님 : {1}살 ==> 미성년자".format(a,people[a]))
#         minor.append(a)
#     else:
#         print("{0}님 : {1}살 ==> 성인".format(a,people[a]))
#         adult.append(a)
# print("\n성인 :",adult)
# print("\n미성년자 :",minor)



# a =[(1,2),(3,4),(5,6)]
# for(a,b) in a:
#     print("{0}+{1}={2}".format(a,b,a+b))
    


# filmFestival ={
#     '최우수 작품상':'택시운전사',
#     '감독상':'아이 캔 스피크',
#     '남우주연상':'송강호',
#     '여우주연상' :'나문희',
# }
# for prize in filmFestival.keys():
#     print(prize)
# for winner in filmFestival.values():
#     print(winner)
# for prize_winner in filmFestival.items():
#     print(prize_winner)
# for prize.winner in filmFestival.items():
#     print(prize,":",winner)
    

#while 무한반복문으로 0을 입력할 때 까지 list변수에 값을 입력 받고
#for문을 이용하여 그 값들을 출력하고 합계를 출력하시오


sumlist =[]
result = 0
while True:
    num =int(input("숫자를 입력하세요 (0입력시 종료)"))
    if num ==0:
        break
    sumlist.append(num)
    print(sumlist)
for i in sumlist:
    print(i)
    result += 1
print("합계 : %d" %result)