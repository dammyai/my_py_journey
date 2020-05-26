import random

word_list = ["olayinka", "arinde", "oluwadamilola", "oluwateniara", "grace", "david", "teniara", "ade","ara","dammy", "yinka"]

word = word_list[random.randint(0, 10)]

print("Welcome to Hangman!!")
print()
print("You have 6 guesses until you lose")
word_len = len(word)
print("your word has:", word_len, "letters")
num_guess = 6
guessed = ""



guessing = ["-" for i in word]    
print(guessing)


while True:
    guess = input("Guess a letter in your word: ")

    if guess in word and guess not in guessed or word.count(guess)>1 and word.count(guess)!= guessed.count(guess):
        guessed += guess
        word_len = word_len -1
        print("your guess is in the word, you have", word_len, "more letters to guess" )
        index1=word.index(guess)
        
        guessing[index1] = guess

        
        print(guessing)
        
        if word_len == 0:
            print("Congratulations, you guessed all letters", word)
            
            break
   
    elif guess not in word:
        num_guess = num_guess-1
        print("your guess is not in the word, you have", num_guess, " guesses left")
        if num_guess == 0:
            print("You have guessed wrong 6 times game over")
            break

      


    else :
        print("you have already guessed letter", guess)
        
