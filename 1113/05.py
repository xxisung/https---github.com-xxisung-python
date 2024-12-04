# #list 변수에 3개의 정수를 입력받아 모두 더하세요
# # list = [int(input("정수: ")),int(input("정수: ")),int(input("정수: "))]
# # print(sum(list[:]))
# # print ()
# # print()
# # # 2개의 리스트에 <이름, 나이>을 입력받는다
# # # 2개의 나이 평균을 구해보세요
# # first_list = [str(input("이름: ")),
# #               int(input("나이: "))]
# # second_list = [str(input("이름: ")),
# #               int(input("나이: "))]
# # print((int(first_list[1]+second_list[1]))//2)

# #리스트 관련 함수
# #요소 추가 : 마지막에 추가됨(기억)
# a = [1,2,3]
# a.append(4)
# a.append([5,6])
# print(a)

# #정렬

# #오름차순정렬
# a = [4,8,2,7,6]
# a.sort()
# print(a)
# #뒤집기
# a = ['a','c','b']
# a.reverse()
# print(a)

# #위치 찾기 : 인덱스 값을 되돌려준다(알려준다)
# a = [1,2,3]
# print(a.index(2))

# #요소 중간 삽입 : 원하는 위치에 넣는다
# a = [1,2,3,4,5]
# a.insert(0,6)
# print(a)

# a = [3,2,3,1,2,3]
# a.remove(3) #첫번째 3을 삭제
# print(a)

# #끄집어 내기
# a =[1,2,3,4,5] #마지막 요소 제거
# a.pop()
# print(a)

# a =[1,2,3,4,5]
# a.pop(2) #해당 인덱스 값을 제거
# print(a)

# a = [1,2,3]
# a.extend([4,5])
# print(a)


#각 라인이 한 조가 되어 각 사람 별로 리스트를 생성한다
#각 리스트에 [이름, 나이, 왼쪽 눈 시력, 오른쪽 눈 시력]을 입력 받는다(안경 끼신 분은 안낀 시력)
list1 = [input("이름 : ",),int(input("나이 : ")),float(input("왼쪽 눈 시력 : ")),float(input("왼쪽 눈 시력 : "))]
list2 = [input("이름 : ",),int(input("나이 : ")),float(input("왼쪽 눈 시력 : ")),float(input("왼쪽 눈 시력 : "))]
list3 = [input("이름 : ",),int(input("나이 : ")),float(input("왼쪽 눈 시력 : ")),float(input("왼쪽 눈 시력 : "))]
age_avg = (list1[1]+list2[1]+list3[1]) / 3
leye = (list1[2]+list2[2]+list3[2])/3
reye = (list1[3]+list2[3]+list3[3])/3

print("조원 평균 나이:{0}세, 왼쪽 시력:{1:.2f},오른쪽 시력:{2:.2f}").format(age_avg,leye,reye)


