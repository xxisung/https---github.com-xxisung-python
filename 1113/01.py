# format_a = "나의 희망연봉 {}만원입니다" .format(3000)
# print(format_a)
# format_b = "{0} {1} {2}" .format(1000,2000,3000)
# print(format_b)
# format_c = "{1} {2} {0}" .format(1000,2000,3000)
# print(format_c)
# format_d = "{1} {1} {1}" .format(1000,"문자열",True)
# print(format_d)

# a="Pen"
# print("""I have a {0}, I have a Apple,
# Apple{0},
# I have {0}, I have PineApple,
# PineApple{0}""".format(a))

# a="Pen"
# b="Apple"
# print("""I have a {0}, I have a {1},
# {1}{0},
# I have {0}, I have Pine{1}
# Pine{1}{0}""".format(a,b))

# print("""I ate {number} cakes.
# so I was sick for {day} days.""".format(number = 10, day =3)      )

# print("""I ate {0} cakes.
# so I was sick for {day} days.""".format(10, day =3)      )

#format함수를 사용하면 자료형을 명시할 필요가 없다
format_a = "나의 희망연봉 {}만원입니다.".format(3000)
print(format_a)
format_b = "{0} {1} {2}".format(1000,2000,3000)
print(format_b)
format_c = "{1} {2} {0}".format(1000,2000,3000)
print(format_c)
format_d = "{1} {1} {1}".format(1000,"문자열",True)
print(format_d)
#정수형
print("{:d}" .format(52))
#특정 (빈)칸에 출력하기
print("{:5d}" .format(52))
print("{:15d}" .format(52))
#빈 칸을 0으로 채우기
print("{:05d}" .format(52))
print("{:05d}" .format(-52))
#실수형
print("{:15.3f}" .format(52.27386))
print("{:15.2f}" .format(52.27386))
print("{:15.1f}" .format(52.27386))

# print("""☆☆☆☆☆☆☆☆☆☆{}☆☆☆☆☆☆☆☆☆☆
# 파이썬 강의 :{} {}
# 본인 이름 : {}
# 본인 나이 :
# 핸드폰 : {})