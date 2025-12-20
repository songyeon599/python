# 스마트 에어컨 시뮬레이션

# 사용자 입력 받기
temperature = int(input("현재 실내 온도를 입력하세요 (°C): "))
person_present = input("실내에 사람이 있습니까? (y/n): ")

# 제어 로직
if person_present.lower() == 'y':
    if temperature >= 28:
        print("에어컨을 켭니다. 냉방을 시작합니다.")
    elif temperature <= 20:
        print("에어컨을 끕니다. 실내가 충분히 시원합니다.")
    else:
        print("현재 온도는 적절합니다. 에어컨을 유지합니다.")
else:
    print("사람이 없으므로 에어컨을 절전 모드로 전환합니다.")