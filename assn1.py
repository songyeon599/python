life = 10
def random_word():
    word_list = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower',
             'peach', 'strawberry', 'watermelon']
    import random
    단어 = random.choice(word_list)
    return 단어
print(random_word())
def print_status(comp_word, used, life):
    print('-' * 20)
    print(f"Word: {reveal_word(comp_word, used)}")
    print("Used:", ' '.join(used))
    print(f"Life: {life}")
    print('-' * 20)
def is_word_guessed(comp_word, used):
    for i in comp_word:
        if i not in used:
            return False
    return True
def reveal_word(comp_word, used):
    blank = ""
    for i in comp_word:
        if i not in used:
            blank += '_' + ' '
        else:
            blank += i + ' '
    return blank
def main():
    print('Hangman game starts!')
    while True:
        comp_word = random_word()
        used = []
        life = 10
        while True:
            print_status(comp_word, used, life)
            inputWord = input("Choose a character: ")
            if inputWord in used:
                print("You have already checked this character. Try another one.")
                continue
            else:
                used.append(inputWord)
            if inputWord in comp_word:
                if is_word_guessed(comp_word, used):
                    print_status(comp_word, used, life)
                    print('Hangman survived!')
                    break
            else:
                life -= 1
                if life == 0:
                    print('Hangman Die!')
                    print(f'The answer was {comp_word}')
                    break
        answer = input('Do you want to play another game?: ')
        if answer == "yes":
            continue
        else:
            print('Quit the Hangman game')
            break
main()



        
        
        
        


                
        
