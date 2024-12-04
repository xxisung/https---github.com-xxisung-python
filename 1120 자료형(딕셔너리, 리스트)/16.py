#첫글자가 1,2이면 1900년대
#3,4 이면 2000년대
#901129 1 901129 // 10000 => 2024 - (90 + 1900)
#080823 4 080823 // 10000 => 2024 - (08 + 2000)

year = int(input("생년월일 6자리 : "))
reginum = int(input("주민번호 뒷자리의 첫글자 : "))
birth_year = year //10000
if reginum == 1 or reginum == 2:
    print("성별번호가 %d이므로,%d년생, %d살 입니다."%(reginum,birth_year+1900,2024 -(birth_year+1900)))
elif reginum == 3 or reginum == 4:
    print("성별번호가 %d이므로,%d년생, %d살 입니다."%(reginum,birth_year+2000,2024 -(birth_year+2000)))
else:
    print("잘못된 입력입니다.")
