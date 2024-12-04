# #문자열 함수
# a = ","
# str = "Hello World"
# slicing = str[:5]
# print(slicing.index("l")) # 해당 문자의 인덱스 번호
# print(a.join(slicing))
# print(slicing.upper())
# print(slicing.lower())
# str2 = "hello_World"
# print(str2.capitalize())
# str3 = "     ABCDE        "
# print(str3.lstrip())
# print(str3.rstrip())
# print(str3.strip())
# str4 = "Life is too short"
# print(str4.split())#공백을 기준으로 단어를 분리하여 리스트 변수에 저장
# print(str4.split(":"))
# print(str4.startswith("Life")) #true
# print(str4.endswith("Life")) #false
# print(str4.center(50))
# print(str4.center(50,'#'))
# print(str4.ljust(50,'#'))
# print(str4.rjust(50,'#'))

# a = "현재 통장의 잔고는 1억원입니다"
# now = a[0:11]
# end = a[-3:]
# print(now + "20억원 " + end )


# a = "현재 통장의 잔고는 1억원입니다"
# a = a[:11] + "5" + a[-6:]
# a= a.replace("20","30")
# print(a)

# b= "현재 통장의 잔고는 %d억원입니다."
# print(b %100)
# print(b %700)
# print(b %777)

# #s나는 점심으로 빵을 __개 먹었습니다.
# print("나는 점으로 빵을 %d개 먹었습니다" % 3.5)
# print("나는 점으로 빵을 %f개 먹었습니다" % 3.5)
# print("나는 점으로 빵을 %s개 먹었습니다" % "세")

# print("I eat %s cakes"%"two")

# num=3
# print("I eat %s cakes" %num)

# num = 5
# disert = "cakes"
# print("I eat%s %s"(num,disert))



# 







a=3.14159265358978
print("%.8f"%a)
print("%.4f"%a)
print("%.2f"%a)
print("%.3f"%a)
print("%.3s"%a)