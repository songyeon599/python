# Developed by Song-yeon Lim / 2026-03-09

import random
from tkinter import * # GUI Library

# 프로그램 객체 생성 및 설정(창 제목, 크기, 리사이즈)
root = Tk()
root.title("보은고등학교 2-4 자리뽑기")
root.geometry("800x600")
root.resizable(False, False)

board_display = Label(root, borderwidth=2, padx=330, pady=20, relief="sunken", text="칠판", font='Helvetica 18 bold', bg="green", fg="white")
board_display.place(x=50, y=30)

# 자리 라벨 리스트
seat_labels = []

# 자리 좌표: (row, col)
for row in range(4):
    for col in range(5):
        # 자리 번호
        seat_num = row * 5 + col + 1
        
        # 자리 라벨
        lbl = Label(root, borderwidth=2, padx=30, pady=15, relief="sunken", text=str(seat_num), font='Helvetica 16 bold', bg="gray", fg="white", width=4)
        
        # 자리 위치
        lbl.place(x=50 + (col * 145), y=150 + (row * 100))
        
        # 자리 라벨 리스트에 추가
        seat_labels.append(lbl)

name_list = [
    '임송연',
    '구자웅',
    '김강근',
    '김민서',
    '김예건',
    '김진민',
    '김진용',
    '박리안',
    '박시훈',
    '박이솔',
    '박정우',
    '박지우',
    '신영환',
    '유세현',
    '윤아단',
    '이병열',
    '이채호',
    '조유완',
    '박지윤',
    '황제율'
]

def seat_select():
    available_seats = list(range(20)) # 사이즈 20인 자리 리스트
    temp_names = name_list[:]         # 이름 리스트 복사
    
    random.shuffle(temp_names)        # 이름 리스트 섞기

    for name in temp_names:
        
        # 남은 자리가 없으면 종료
        if not available_seats:
            break
        
        # 자리를 랜덤으로 선택하여 이름 표시
        seat_idx = random.choice(available_seats) # 랜덤으로 자리 인덱스 선택
        seat_labels[seat_idx].config(text=name)   # 해당 자리에 이름 표시
        available_seats.remove(seat_idx)          # 가능한 자리 제거(이미 할당)

button_play = Button(root, text="실행", command=seat_select, font='Helvetica 12 bold', padx=20)
button_play.place(x=350, y=550)

root.mainloop()
