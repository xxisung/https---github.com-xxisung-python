Current_Height=float(input("당신의 키는? "))
Man_StandardWeight=float(Current_Height-100)*0.9
Woman_StandardWeight=float(Current_Height-105)*0.9
result1= round(Man_StandardWeight, 2)
result2= round(Woman_StandardWeight, 2)

print("당신의 표준체중은 남성일시 ",result1, "이고 여성일시 " ,result2, "kg입니다." )

