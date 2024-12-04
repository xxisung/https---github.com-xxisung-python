it="BusanIT"
address="부산광역시 수영구 민락동"
start=9
name="송진우"
end=16
height=192.123456
age=29
Phone="010-5567-1430"

print("""☆☆☆☆☆☆☆☆☆☆{}☆☆☆☆☆☆☆☆☆☆
파이썬 강의 : {}시 ~ {}시
본인 이름 : {}
본인 나이 : {}
핸드폰 : {}
주소 : {}
키 : {}
☆☆☆☆☆☆☆☆☆☆*10{}☆☆☆☆☆☆☆☆☆☆""".format(it,start,end,name,age,Phone,address,height,it))

#왼쪽정렬
print("이름:{:<5}, 나이:{:<3}".format("홍길동", 27))
#오른쪽정렬
print("이름:{:>5}, 나이:{:>3}".format("홍길동", 27))
#가운데정렬
print("이름:{:^5}, 나이:{:^3}".format("홍길동", 27))