import csv
import os
def loadcsv():
    csv_file = os.path.join(os.path.dirname(__file__), 'word.csv')
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data_dict = {}
        for rows in reader:
            data_dict[rows[0]] = rows[1]
    return data_dict
print(loadcsv())

def addWord():
    data_dict = {}
    retry = False
    while True:
        print('_' * 30)
        for item, value in data_dict.items():
            print(item, value)
        print('_' * 30)
        단어 = input("영단어와 한글 뜻을 입력하세요: ").split()
        data_dict[단어[0]] = 단어[1]
        while True:
            answer = input('단어를 더 추가하시겠습니까? Y/N: ')
            if answer == 'y' or answer == 'Y':
                retry = True
                break
            elif answer == 'n' or answer == 'N':
                return data_dict
            else:
                print('다시 입력하세요')
                continue
        if retry == True:
            continue

def testWord(deta_dict):
    for item, value in deta_dict.items():
        뜻 = input(f'{item}의 뜻을 입력하세요: ')
        if 뜻 == value:
            continue
        else:
            print(f'정답은 {value}입니다.')
deta_dict = loadcsv()
testWord(deta_dict)


    
                        