def palindromo():
    word = input()
    palindromo1 = False
    for i in range(len(word)):
        if word[i] == word[-i-1]:
            palindromo1 = True
        else:
            palindromo1 = False
            break
    if palindromo1:
        print('es un palindromo')
    else:
        print('no es un palindromo')


def palindromo2():
    word = input()
    reverse_word = word[::-1]
    if word == reverse_word:
        print('es un palindromo')
    else:
        print('no es un palindromo')


palindromo2()
