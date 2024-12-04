eng_dict = {"money":"돈"
            ,"sky":"하늘"
            ,"school":"학교"
            ,"star":"별"
            ,"function":"함수"}
answer = input("영어 단어 입력 : ") #key 이름표
if answer in eng_dict:
    mean = input("영단어 뜻: ")
    if mean == eng_dict[answer]:
        print("정답입니다.")
    else:
        print("틀렸습니다.")
else:
    print("없는단어입니다.")