import random

def posmon_OX(posmons):
    blank = []
    cnt = 0
    for posmon in posmons:
        if posmon.get_health() == 0:
            blank.append('X')
        else:
            blank.append('O')
            cnt += 1
    return "".join(blank), cnt

def change_com_posmon(com_posmons):
    for posmon in com_posmons:
        if posmon.health > 0:
            print(f"컴퓨터 포스몬 {com_battle_posmon}로 교대")
            com_battle_posmon = posmon
            return com_battle_posmon
    return False

def change_our_posmon(our_posmons):
    for posmon in our_posmons:
        if posmon.health > 0:
            print(f"당신의 포스몬 {our_battle_posmon}로 교대")
            our_battle_posmon = posmon
            return our_battle_posmon
    return False



def main():
    while True:
        print("=============================================")
        print("0. 포스몬 선택")
        print("1. 배틀하기")
        print("2. 종료하기")
        print("=============================================")
        while True:
            answer = int(input("입력: "))
            if answer in [0, 1, 2]:
                break
            else:
                print("잘못된 입력입니다. 다시 입력하세요.")
        print()

        our_posmons = []
        com_posmons = [Ponix(), Rocky(), Swania(), Normie()]
        com_posmons_names = [posmon.name for posmon in com_posmons]
        com_posmons.remove(random.choice(com_posmons))
        
        if answer == 0:
            # 포스몬 선택
            while True:
                if len(our_posmons) == 3:
                    break
                print("=============================================")
                print(f"당신이 사용할 포스몬을 선택하세요. 현재 {len(our_posmons)} 마리/최대 3 마리")
                print("0. Ponix")
                print("1. Normie")
                print("2. Swania")
                print("3. Rocky")
                if len(our_posmons) >= 1:
                    print("-1. 그만두기")
                print("=============================================")
                while True:
                    answer_posmon = int(input("입력: "))
                    if answer_posmon in [-1, 0, 1, 2, 3]:
                        break
                    else:
                        print("잘못된 입력입니다. 다시 입력하세요.")
                if answer_posmon == -1 and len(our_posmons) >= 1:
                    break
                elif answer_posmon == 0:
                    our_posmons.append(Ponix())
                elif answer_posmon == 1:
                    our_posmons.append(Normie())
                elif answer_posmon == 2:
                    our_posmons.append(Swania())
                elif answer_posmon == 3:
                    our_posmons.append(Rocky())
            
            print("\n=============================================")
            our_posmons_names = [posmon.name for posmon in our_posmons]
            print(our_posmons_names)
            print("=============================================\n")

        elif answer == 1:
            print("\n=============================================")
            print(f"당신의 포스몬 목록: {" ".join(our_posmons_names)}")
            print(f"컴퓨터 포스몬 목록: {" ".join(com_posmons_names)}")
            print("=============================================\n")

            com_battle_posmon = com_posmons[0]
            our_battle_posmon = our_posmons[0]

            print("배틀이 시작됩니다.")
            print("##############################################")
            print(f"컴퓨터 포스몬: [{posmon_OX(com_posmons)[0]}] {posmon_OX(com_posmons)[1]} / 3")
            print(f"{com_battle_posmon.get_name()}            <|{com_battle_posmon.get_type()} {com_battle_posmon.get_health()} / {com_battle_posmon.get_max_health()}|")
            print("                                           VS")
            print(f"{our_battle_posmon.get_name()}            <|{our_battle_posmon.get_type()} {our_battle_posmon.get_health()} / {our_battle_posmon.get_max_health()}|")
            print(f"당신의 포스몬: [{posmon_OX(our_posmons)[0]}] {posmon_OX(our_posmons)[1]} / {len(our_posmons)}")
            print("++++++++++++++++++++++++++++++++++++++++++")
            print(f"기술: ", end="")
            for i, skill in enumerate(our_battle_posmon.moves):
                print(f"({i}) {skill.get_name()}", end=" ")
            print("##########################################")
            while True:
                answer_choice = input("입력: ")

                if answer_choice == "e":
                    print("#########################################")
                    for i, posmon in enumerate(our_posmons):
                        print(f"({i}) {posmon.get_name()} <|{posmon.get_type()} {posmon.get_health()} / {posmon.get_max_health()}|")
                else:
                    choice_split = answer_choice.split()
                    try:
                        choice_split[1] = int(choice_split[1])
                    except:
                        continue
                    if choice_split[0] == "o":
                        skill_num = choice_split[1]
                        our_choice_skill = our_battle_posmon.moves[skill_num]
                        com_choice_skill = random.choice(com_battle_posmon.moves)
                        if our_choice_skill.speed > com_choice_skill.speed:
                            our_choice_skill.use(our_battle_posmon,com_battle_posmon, True)
                            if com_battle_posmon.health <= 0:
                                print(f"컴퓨터 {com_battle_posmon}: 쓰러짐")
                                com_battle_posmon = change_com_posmon(com_posmons)
                                continue
                            com_choice_skill.use(our_battle_posmon,com_battle_posmon, False)
                        elif com_choice_skill.speed > our_choice_skill.speed:
                            com_choice_skill.use(our_battle_posmon, com_battle_posmon, True)
                            if our_battle_posmon.health <= 0:
                                print(f"당신의 {our_battle_posmon}: 쓰러짐")
                                our_battle_posmon = change_our_posmon(our_posmons)
                                continue
                            our_choice_skill.use(our_battle_posmon,com_battle_posmon, False)                      

                    elif choice_split[0] == "s":
                        posmon_num = choice_split[1]
                        if our_posmons[posmon_num].health() <= 0:
                            print("포스몬을 교대시킬 수 없습니다!")
                        else:
                            our_battle_posmon = our_posmons[posmon_num]
                    else:
                        continue

    



        

        

'''
빠져나가는 조건

1. 우리가 고른 포스몬의 수가 1마리 이상일 때 우리가 -1을 눌렀을 때 탈출
2. 우리가 고른 포스몬의 수가 3마리일 때 자동으로 탈출
'''
            





def type_multiply(attack_type, victim_type):
    if attack_type == "Scissors" and victim_type == "Paper":
        return 2
    elif attack_type == "Rock" and victim_type == "Sciccors":
        return 2
    elif attack_type == "Paper" and victim_type == "Rock":
        return 2
    else:
        return 1

class Posmon:
    def __init__(self, health, attack, defence, moves, name, type):
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defence = defence
        self.moves = moves
        self.name = name
        self.default_attack = attack
        self.default_defence = defence
        self.type = type
    
    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

    def get_max_health(self):
        return self.max_health
    
    def get_type(self):
        return self.type

    def reset_status(self, reset_health:bool = False):
        self.attack = self.default_attack
        self.defence = self.default_defence
        if reset_health == True:
            self.health = self.max_health

    def get_attack(self):
        return self.attack
    
    def get_defence(self):
        return self.defence
   
class Ponix(Posmon):
    def __init__(self):
        super().__init__(86, 20, 23, [Tackle(), Growl(), SwordDance()],"Ponix", "Paper" )

class Normie(Posmon):
    def __init__(self):
        super().__init__(80, 20, 20, [Tackle(), Swift(), TailWhip()], "Nomix", "Nothing")

class Rocky(Posmon):
    def __init__(self):
        super().__init__(80, 30, 10, [Tackle(), Growl()], "Rocky", "Rock")

class Swania(Posmon):
    def __init__(self):
        super().__init__(80, 30, 10, [ScissorsCross(), SwordDance()], "Swania", "Scissors")

class Move:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def get_name(self):
        return self.name
    
    def get_speed(self):
        return self.speed
    
    def use(self):
        pass

class PhysicalMove(Move):
    def __init__(self, name, speed, power):
        super().__init__(name, speed)
        self.power = power

    def get_power(self):
        return self.power

    def use(self, our_posmon:Posmon, opponent_posmon:Posmon, is_player_move=True):
        if is_player_move == True:
            multiply = type_multiply(our_posmon.get_type(), opponent_posmon.get_type())
            damage = max(0, self.power + our_posmon.get_attack()-opponent_posmon.get_defence()) * multiply
            print(f"당신의 {our_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 컴퓨터 포스몬의 [체력] {damage} 감소 ({opponent_posmon.get_health()} -> {opponent_posmon.get_health()} - {damage})")
            opponent_posmon.health -= damage

        else:
            multiply = type_multiply(opponent_posmon.get_type(), our_posmon.get_type())
            damage = max(0, self.power + opponent_posmon.get_attack()-our_posmon.get_defence()) * multiply
            print(f"컴퓨터 포스몬의 {opponent_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 당신 포스몬의 [체력] {damage} 감소 ({our_posmon.get_health()} -> {our_posmon.get_health()} - {damage})")
            our_posmon.health -= damage

class StatusMove(Move):
    pass

class Tackle(PhysicalMove):
    def __init__(self):
        super().__init__(power=25, speed=0, name="Tackle")
        
class ScissorsCross(PhysicalMove):
    def __init__(self):
        super().__init__(power=30, speed=0, name="ScissorsCross")

class Swift(PhysicalMove):
    def __init__(self):
        super().__init__(power=0, speed=3, name="Swift")
    
class Growl(StatusMove):
    def __init__(self):
        super().__init__(name = "Growl", speed = 1)

    def use(self, our_posmon, opponent_posmon, is_player_move=True):
        if is_player_move == True:
            print(f"당신의 {our_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 컴퓨터 포스몬의 [공격력] 5 감소 ({opponent_posmon.get_attack()} -> {opponent_posmon.get_attack() - 5})")
            opponent_posmon.attack -= 5
        else:
            print(f"컴퓨터 {opponent_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 당신의 [공격력] 5 감소 ({our_posmon.get_attack()} -> {our_posmon.get_attack() - 5})")
            our_posmon.attack -= 5

class TailWhip(StatusMove):
    def __init__(self):
        super().__init__(name = "TailWhip", speed = 1)

    def use(self, our_posmon, opponent_posmon, is_player_move=True):
        if is_player_move == True:
            print(f"당신의 {our_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 컴퓨터 포스몬의 [방어력] 5 감소 ({opponent_posmon.get_defence()} -> {opponent_posmon.get_defence() - 5})")
            opponent_posmon.defence -= 5
        else:
            print(f"컴퓨터 {opponent_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 당신의 [방어력] 5 감소 ({our_posmon.get_defence()} -> {our_posmon.get_defence() - 5})")
            our_posmon.defence -= 5

class SwordDance(StatusMove):
    def __init__(self):
        super().__init__(name = "SwordDance", speed = 0)

    def use(self, our_posmon, opponent_posmon, is_player_move=True):
        if is_player_move == True:
            print(f"당신의 {our_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 당신 포스몬의 [공격력] 10 증가 ({our_posmon.get_attack()} -> {our_posmon.get_attack() + 10})")
            our_posmon.attack += 10
        else:
            print(f"컴퓨터 {opponent_posmon.get_name()}: {self.name} 기술 사용")
            print(f"- 컴퓨터 [공격력] 10 증가 ({opponent_posmon.get_attack()} -> {opponent_posmon.get_attack() + 10})")
            opponent_posmon.attack += 10



class test:
    def __init__(self, name):
        self.name = name


list1 = [test("test1"), test("test2"), test("test3")]
list2 = [t.name for t in list1]
print(" ".join(list2))
print(list2)


