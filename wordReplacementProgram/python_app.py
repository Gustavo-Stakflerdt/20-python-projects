def replace_word():
    sentence = 'Hey there! I am Gustavo and I\'m making Python projects!'
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(sentence.replace(word_to_replace, word_replacement))


replace_word()
