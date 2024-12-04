Max_Weight=600
Object1=float(input("첫 번째 물건의 무게를 이렵하세요 : "))
Object2=float(input("두 번째 물건의 무게를 이렵하세요 : "))
Current_Weight=float(Max_Weight - (Object1+Object2))

print("현재 엘리베이터의 허용 무게는",Current_Weight,"kg 입니다")
