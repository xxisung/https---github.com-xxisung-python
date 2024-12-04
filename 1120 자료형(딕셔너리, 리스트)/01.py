dic = {"이름":"허지성","주소":"부산","성별":"남자","이메일":"o106704@gmail.com"}
print(dic)
print(dic["이름"])
#딕셔너리 변수에 있는 이름표(key)값만 출력
dic_key=dic.keys()
print(dic_key)
#딕셔너리 변수에 있는 값(value)만 출력
dic_value=dic.values()
print(dic_value)
#딕셔너리에서 키와 값을 튜플 형식으로 출력
dic_item = dic.items()
print(dic_item)
#key로써 그에 대응하는 값을 출력
print(dic.get("이름"))
#딕셔너리에 이름표(key)가 존재하는지 확인하는 방법 (T/F 판별)
print("전화번호" not in dic) #없으니 -> 참T (not)
print("이름" in dic)
print("이름" not in dic)

