dict = {}
while True:
    word = input('Enter word: ')
    if word in dict:
        print(f'Translation {word} is {dict[word]}')
    else:
        dict[word] = input('Enter tranlation of the word: ')
