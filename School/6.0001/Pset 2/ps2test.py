secret_word = 'Code'
letters_guessed = []

'''print (secret_word.lower())
print (secret_word.isalpha())
word_progress = list(secret_word)
word1 = []
yesno = 0
for count2 in range(len(word_progress)):
    for count1 in range(len(letters_guessed)):
        if letters_guessed[count1] == word_progress[count2]:
            word1.append(word_progress[count2])
            yesno = 0
            break
        elif letters_guessed[count1] != word_progress[count2]:
            yesno = 1
    if yesno == 1:
        word1.append('_')
if len(word1) == 0:
    for count3 in range(len(secret_word)):
        word1.append('_')
word_progress_complete = ''.join(word1)
print (word_progress_complete)'''

a = "a"

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print (list(alphabet).count(a))