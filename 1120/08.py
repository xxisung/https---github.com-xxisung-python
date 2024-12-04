성별 = input("당신의 성멸은[남/여]? : ")
age = int(input("당신의 나이는? : "))

if 성별 == "남" and age >= 19:
    print("군대 입영대상자 입니다.")
if 성별 == "여" or age < 19:
    print("군대 입영대상자가 아닙니다.")