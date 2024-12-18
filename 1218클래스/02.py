#클래스 속성 : 체력,공격력,주문력
#클래스 메소드 : 베기, 찌르기
class Unit:
    def __init__(self,name,hp,damage): # 생성자 : 클래스 겍체를 만드는 생성자
        self.name = name #멤버변수 : 클래스 안에서 정의된 변수
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력{0},공격력{1}".format(self.hp,self.damage))
        
marine1 = Unit("마린",50,5) #인스턴스 생성 : 멤버변수 개수와 같아야 함
marine2 = Unit("마린",50,5)
marine3 = Unit("마린",50,5)
tank = Unit("탱크",150,35)
vulture = Unit("벌처",100,25)
