#딕셔너리 기본

people = {"name":"홍길동", "age":23}
print(people)
people["name"] = "아이유"
print(people)
people["job"] = ["가수","연기자","호텔주인"]
# print(people["job"])

#_______의 직업은 __________ 입니다.


print("{}의 직업은 {}입니다." .format(people["name"],people["job"]))
print("{0}의 직업은 {1}입니다." .format(people["name"],people["job"]))
