name = "마린"
hp = 40#마린 체력
damage = 5 #공격력
print("{}유닛이 생성되었습니다.".format(name))
print("체력:{0},공격력:{1}\n".format(hp,damage))

tank_name="탱크"
tank_hp = 150# 체력
tank_damage = 35 #공격력

tank2_name="탱크"
tank2_hp = 150# 체력
tank2_damage = 35 #공격력
#위의 방법으로는 한 두개는 몰라도 수십, 수백개는 무리다.
print("{}유닛이 생성되었습니다.".format(tank_name))
print("체력:{0},공격력:{1}\n".format(tank_hp,tank_damage))

def attack(name,location,damage):
    print("{0}:{1}시 방향으로 공격한다.[공격력{2}]".format(\
        name,location,damage))
attack(name,"1시",damage)
attack(tank_name,"12",tank_damage)
attack(tank2_name,"3",tank2_damage)