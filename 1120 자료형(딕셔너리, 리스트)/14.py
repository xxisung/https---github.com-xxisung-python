kor,eng,mat = int(input("국어:")),int(input("영어:")),int(input("수학:"))

sum = kor + eng + mat
avg = int(sum/3)

if kor < 0 or kor > 100 or eng < 0 or eng > 100 or mat < 0 or mat > 100:
    print("잘못 입력했어요")
elif avg <= 100 and avg >=90:
    print("A학점")
elif avg >= 80    :
    print("B학점")
elif avg >= 70:
    print("C학점")
elif avg >=60:
    print("D학점")
else:
    print("F학점")