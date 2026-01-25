import random
class Station:
    def __init__(self):
        self.day = 1 # 현재까지의 총 영업일(Day XX)을 표시하는 변수 
        self.rating = 0 # 주유소의 평판
        self.money = 1000 # 보유 금액
        self.today_num = 0 # 오늘의 고객 수
        self.total_num = 0 # 전체 고객 수
        self.customer = 0 # 현재 응대 중인 고객. 없는 경우 None
        self.diesel_left = 100
        self.gasoline_left = 100
        self.diesel_price = 10
        self.gasoline_price = 15

    def state_update(self):  # 고객 응대에 따라 보유 금액, 평판 등을 업데이트하는 함수 
        pass

    def refill(self):  # 상점으로부터 기름을 구매하는 함수 
        print("\nWhich one do you want to refill?")
        print("0. Diesel")
        print("1. Gasoline")
        while True:
            select = int(input("select: "))
            if select in [0, 1]:
                break
            else:
                print("Wrong input!")

        discount = min(max(0, self.rating/2), 30)
        if select == 0:
            selling_price = self.diesel_price * 0.9
            fuel_type = "Diesel"
            tank = self.diesel_left
        else:
            selling_price = self.gasoline_price * 0.9
            fuel_type = "Gasoline"
            tank = self.gasoline_left
        
        discount_price = selling_price - selling_price * discount/100

        print(f"\nBased on your rating {self.rating}, the discount ratio is {discount}%")
        print(f"The base unit buying price of Gasoline for today is")
        print(f"{selling_price}$, so the discount unit buying price will be ${discount_price}")
        while True:
            amount = int(input(f"\nYou have ${self.money}. Amount of {fuel_type} to buy (liters): "))
            total_price = discount_price * amount
            if total_price > self.money:
                print("You don't have enough money\n")
            else:
                if select == 0:
                    self.diesel_left += amount
                else:
                    self.gasoline_left += amount
                print(f"${self.money} -> {self.money - total_price}")
                print(f"{fuel_type} refilled: {tank} Liters -> {tank + amount} Liters")
                self.money -= total_price
            break

    def print_status(self):  # 현재 상태를 출력하는 함수 
        print("\n---------STATUS---------")
        print(f"Day {self.day}")
        print(f"Rating: {self.rating}")
        print(f"Money: ${self.money}")
        print(f"# Customers handled for today: {self.today_num}")
        print(f"Diesel left: {self.diesel_left} Liters")
        print(f"Gasoline left: {self.gasoline_left} Liters")
        print()

    def default_screen(self): # 초기화면 출력 및 초기화면에서 (0. Wait for a vehicle)  
        while True:
            print("\n---------GAS STATION---------")
            print("0. Wait for a vehicle")
            print("1. Refill tanks")
            print("2. Show current status")
            print("3. Go to the next day")
            print("4. End Game")
            while True:
                select = int(input("Select: "))
                if select in [0, 1, 2, 3, 4]:
                    break
                else:
                    print("Wrong input!")

            if select == 0:
                self.serve()
            
            elif select == 1:
                self.refill()

            elif select == 2:
                self.print_status()

            elif select == 3:
                if self.today_num >= 3:
                    self.next()
                else:
                    print(f"You have to handle at least at three customers. ({self.today_num} / 3)")

            else:
                if self.money >= 5000:
                    print(f"\n------Summary------")
                    print(f"Rating: {self.rating}")
                    print(f"Money: {self.money}")
                    print(f"Total customers handled: {self.total_num}")
                    print(f"-----------------------")
                    print(f"You win!")
                else:
                    print(f"You should have at least $5000 to finish the game.")
                    print(f"You have ${self.money}")

    def serve(self):  # 초기화면에서 (0. Wait for a vehicle) 선택 시, 실행되는 함수 
        self.customer += 1
        self.today_num += 1
        import time
        print("\nWaiting...", end='')
        for i in range(3):
            print(".", end='')
            time.sleep(0.3)
        print()
        cars = [SUV(), Hybrid(), Bus(), Truck()]
        car = random.choice(cars)
        car.printInfo()
        if random.choice([1, 2, 3, 4, 5]) == 1:
            if car.vehicle_type == "Bus" or car.vehicle_type == "Truck":
                print("\nDriver: some DEF for free? (costs $50 yet increases rating by 3)")
                print("0. Yes")
                print("1. No")
                select = int(input("Select: "))
                if select == 0:
                    if self.money >= 50:
                        print(f"\nMoney: ${self.money} -> ${self.money - 50}")
                        self.money -= 50
                        print("Driver: I'm blessed to have all of these. Thanks!")
                        print(f"Rating: {self.rating} -> {self.rating + 3}")
                        self.rating += 3
                        return
                    else:
                        print("\nYou don't have enough money!")
                        print(f"Money: ${self.money}, Required: $50")
                        print("\nOwner: Currently, we are not available for that")
                        print("Driver: Well, see you then!")
                        print(f"Rating: {self.rating} -> {self.rating - 1}")
                        self.rating -= 1
                        return
                else:
                    print("\nOwner: Currently, we are not available for that")
                    print("Driver: Well, see you then!")
                    print(f"Rating: {self.rating} -> {self.rating - 1}")
                    self.rating -= 1
                    return
            elif car.vehicle_type == "SUV":
                print("\nDriver: An oil change, please")
                print("\nChange the engine oil for free? (costs $100 yet increases rating by 3)")
                print("0. Yes")
                print("1. No")
                answer = int(input("Select: "))
                if answer == 0:
                    print("You provided some engine oil for free!")
                    print(f"Money: ${self.money} -> {self.money - 100}")
                    self.money -= 100
                    print("Driver: I'm blessed to have all of these. Thanks!")
                    print(f"Rating: {self.rating} -> {self.rating + 3}")
                    self.rating += 3
                    return

                else:
                    print("Owner: Currently, we are not available for that.")
                    print("Driver: Well, see you then!")
                    print(f"Rating: {self.rating} -> {self.rating -1}")
                    self.rating -= 1
                    return
            else:
                print("\nDriver: my tire is flattend")
                print("\nProvide a tire for free? (costs $300 yet increases rating by 3)")
                print("0. yes")
                print("1. No")
                answer = int(input("Select: "))
                if answer == 0:
                    print(f"Money: ${self.money} -> {self.money - 300}")
                    self.money -= 300
                    print(f"Driver: I'm blessed to have all of these. Thanks!")
                    print(f"Rating: {self.rating} -> {self.rating + 3}")
                    self.rating += 3
                    return
                else:
                    print("Owner: Currently, we are not available for that.")
                    print("Driver: Well, see you then!")
                    print(f"Rating: {self.rating} -> {self. rating - 1}")
                    self.rating -= self.rating 
                    return
        else:
            if car.full == True:
                print(f"Driver: please make it full!")
            else:
                print(f"I'd like {car.needed} liters, please.")
            print(f"Diesel left: {self.diesel_left} Liters, Gasoline left: {self.gasoline_left} Liters")
            
        current_method_fuel = "Diesel"
        current_method_liter = 10
        current_selling_price = self.diesel_price
        fuel_left = self.diesel_left
    
        while True:
            print("\n0. Change fueling method")
            print("1. Start fueling")
            print("2. Let go")
            while True:
                choice = int(input("Select: "))
                if choice in [0, 1, 2]:
                    break
                else:
                    print("Wrong input!")
            if choice == 0:
                print(f"\nCurrent Method: {current_method_fuel} / {current_method_liter} Liters.")
                while True:
                    print(f"\n0. Toggle fuel type")
                    print(f"1. Change the amount of fuel")
                    print(f"2. Finish")
                    choice_method = int(input("Select: "))
                    if choice_method == 0:
                        if current_method_fuel == "Diesel":
                            current_method_fuel = "Gasoline"
                            current_selling_price = self.gasoline_price
                            fuel_left = self.gasoline_left
                        else:
                            current_method_fuel = "Diesel"
                            current_selling_price = self.diesel_price
                            fuel_left = self.diesel_left
                        print(f"\nFuel type changed: {current_method_fuel}")
                    elif choice_method == 1:
                        choice_liter = input(f"Enter 'F' (full), or the amount of liters to fuel: ")
                        if choice_liter == 'F':
                            print(f"\nFueling method changed: Full")
                            current_method_liter = choice_liter
                        else:
                            print(f"\nFueling method changed: {choice_liter} Liters")
                            current_method_liter = int(choice_liter)

                    elif choice_method == 2:
                        break
                    else:
                        print(f"Wrong input!")
            
            elif choice == 1:
                if car.fuel_type == current_method_fuel:
                    if (car.full == True and current_method_liter == "F") or (car.needed == current_method_liter):
                        if car.needed <= fuel_left:
                            print('\nChecking the conditions...')
                            print(f'Money: ${self.money} -> {self.money + car.needed * current_selling_price}')
                            self.money += car.needed * current_selling_price
                            if current_method_fuel == "Diesel":
                                print(f'Diesel: {self.diesel_left} -> {self.diesel_left - car.needed}')
                                self.diesel_left -= car.needed
                            else:
                                print(f'Gasoline: {self.gasoline_left} -> {self.gasoline_left - car.needed}')
                                self.gasoline_left -= car.needed
                            print("\nDriver: Thanks a lot!")
                            print(f"Rating: {self.rating} -> {self.rating + 1}")
                            self.rating += 1
                            return
                        else:
                            print("\nChecking the conditions...")
                            print(f"Fuel type: {car.fuel_type}")
                            print(f"Amount of {car.fuel_type} in the  tank: {fuel_left}, Tried: {current_method_liter}")
                            print("\nSystem: There is not enough fuel in the tank!")
                            print(f"Rating: {self.rating} -> {self.rating - 1}")
                            self.rating -= 1
                            return
                    elif current_method_liter >= car.capacity - car.cur_fuel:
                        print("\nChecking the conditions...")
                        print(f"Fuel type: {car.fuel_type}")
                        print(f"Maximum amount to fuel: {car.capacity - car.cur_fuel} Liters, Tried: {current_method_liter} Liters")
                        print("\nDriver: Hey, it overflows! Stop there!")
                        print(f"Money: ${self.money} -> ${self.money + (car.capacity - car.cur_fuel) * current_selling_price}")
                        self.money -= (car.capacity - car.cur_fuel) * current_selling_price
                        if current_method_fuel == 'Diesel':
                            print(f"Diesel: {self.diesel_left} -> {self.diesel_left - (car.capacity - car.cur_fuel)}")
                            self.diesel_left -= car.capacity - car.cur_fuel
                        else:
                            print(f"Gasiline: {self.gasoline_left} -> {self.gasoline_left - (car.capacity - car.cur_fuel)}")
                            self.gasoline_left -= car.capacity - car.cur_fuel
                        print(f"Rating: {self.rating} -> {self.rating -3}")
                        self.rating -= 3
                        return
                    else:
                        print("\nChecking the conditions...")
                        print(f"Fuel type: {car.fuel_type}")
                        print(f"Requested: {car.needed}, Tried: {current_method_liter}")
                        print(f"\nDriver: well, not the exact amount, but thanks anyway!")
                        print(f"Money: ${self.money} -> ${self.money + current_method_liter * current_selling_price}")
                        self.money += current_method_liter * current_selling_price
                        if current_method_fuel == "Diesel":
                            print(f"Diesel: {self.diesel_left} -> {self.diesel_left - current_method_liter}")
                            self.diesel_left -= current_method_liter
                        else:
                            print(f"Gasoline {self.gasoline_left} -> {self.gasoline_left - current_method_liter}")
                            self.gasoline_left -= current_method_liter
                        print(f"Rating: {self.rating} -> {self.rating - 1}")
                        self.rating -= 1
                        return
                else:
                    print("\nChecking the condition...")
                    print(f"Requested: {car.fuel_type}, Selected: {current_method_fuel}")
                    print(f"\nSystem: This is not the right fuel type!")
                    print(f"Rating: {self.rating} -> {self.rating - 5}")
                    self.rating -= 5
                    return
            else:
                print("\nOwner: Currently, we are not available for that.")
                print("Driver: Well, see you then!")
                print(f"{self.rating} -> {self.rating - 1}")
                self.rating -= 1
                return

    def next(self): # 다음 날로 이동하는 함수
        print('\n다음 날로 이동합니다')
        self.day += 1
        self.today_num = 0
        self.update_price()

    def update_price(self):
        self.diesel_price *= (1 + random.uniform(-0.1, 0.1))
        self.gasoline_price *= (1 + random.uniform(-0.1, 0.1))

class Car:
    # 인스턴스 변수
    def __init__(self, fuel_type, vehicle_type, capacity): 
        self.fuel_type = fuel_type # 연료 종류(가솔린, 디젤)
        self.vehicle_type = vehicle_type # 자동차 종류(트럭, 버스, SUV, 하이브리드)
        self.capacity = capacity # 연료통 크기
        self.cal_fuel()

    def cal_fuel(self):
        self.cur_fuel = int(self.capacity * random.uniform(0.1, 0.4))
        if random.randint(1, 4) == 1:
            self.full = True
            self.needed = self.capacity - self.cur_fuel
        else:
            self.full = False
            self.needed = ((self.capacity - self.cur_fuel) * random.uniform(0.5, 0.8)
                           // 5) * 5
            
    def printInfo(self):
        print("\n<<Vehicle Info>>")
        print(f"Fuel type: {self.fuel_type}, Vehicle type: {self.vehicle_type}, Fuel: {self.cur_fuel} / {self.capacity}")
        
class Gasoline_Car(Car):
    def __init__(self, vehicle_type, capacity):
        super().__init__("Gasoline", vehicle_type, capacity)

class Diesel_Car(Car):
    def __init__(self, vehicle_type, capacity):
        super().__init__("Diesel", vehicle_type, capacity)

class SUV(Gasoline_Car):
    def __init__(self):
        super().__init__("SUV", 80)

class Hybrid(Gasoline_Car):
    def __init__(self):
        super().__init__("Hybrid", 60)

class Bus(Diesel_Car):
    def __init__(self):
        super().__init__("Bus", 100)

class Truck(Diesel_Car):
    def __init__(self):
        super().__init__("Truck", 300)

station = Station()
station.default_screen()
