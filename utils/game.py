import random
possible_words = ['becode', 'learning', 'mathematics', 'sessions']
random_word = random.choice(possible_words)
print(random_word)
number_of_dash = "_" * len(random_word)
word_in_dash = list(number_of_dash)
print(word_in_dash)
correctly_guessed_letters= ""
guessed_letter = input("Guess a letter: ")
while "_" in word_in_dash:
    correctly_guessed_letters = ""
    if guessed_letter in random_word:
        for i in range(0,len(random_word)):
            if random_word[i] == guessed_letter:
                 word_in_dash[i] = random_word[i]
            correctly_guessed_letters +=word_in_dash[i]
        print(correctly_guessed_letters)
        if "_" in word_in_dash:
            guessed_letter = input("Guess a letter: ")
        else:
            print("Done")
            break

    else:
        guessed_letter = input("Guess a letter: ")