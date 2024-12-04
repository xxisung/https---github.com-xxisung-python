#집합이라는 자료형은 이전의 수학에서의 집합이다.
setValue = set([1,2,3])
print(setValue)
#문자열도 리스트 형태로 사용한다.
setValue2 = set(["TEST"])
setValue3 = set(["Hello","Python","TEST"])
print(setValue3)
#교집합 : 두 집합에서 같은 것 추출 
print(setValue2.intersection(setValue3))
print(setValue2 & setValue3)

#합집합
print(setValue2.union(setValue3))
print(setValue2 | setValue3)

#차집합 : 좌변의 집합을 기준으로 우변에 같은 값을 뺀 결과
print(setValue3.difference(setValue2))
print(setValue3 - setValue2)