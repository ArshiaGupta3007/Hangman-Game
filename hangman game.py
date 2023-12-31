import turtle
import random

# Function to draw the hangman figure based on the number of incorrect guesses
def drawMan(incorrect_guesses):
    if incorrect_guesses == 1: 
        # Draw head
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.right(90)
        turtle.circle(15, None, 100)
        turtle.penup()
    elif incorrect_guesses == 2:
        # Draw torso
        turtle.goto(-74, 140)
        turtle.pendown()
        turtle.left(90)
        turtle.penup()
        turtle.forward(30)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(180)
        turtle.forward(30)
        turtle.penup()
    elif incorrect_guesses == 3:
        # Draw first arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif incorrect_guesses == 4:
        # Draw second arm
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(70)
        turtle.forward(45)
        turtle.right(180)
        turtle.forward(45)
        turtle.penup()
    elif incorrect_guesses == 5:
        # Draw first leg
        turtle.goto(-74, 100)
        turtle.pendown()
        turtle.left(55)
        turtle.forward(30)
        turtle.right(30)
        turtle.forward(60)
        turtle.right(180)
        turtle.forward(60)
        turtle.penup()
    elif incorrect_guesses == 6:
        # Draw second leg
        turtle.goto(-74, 70)
        turtle.pendown()
        turtle.right(120)
        turtle.forward(60)
        turtle.penup()

# Initialize turtle
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)

# List of words for the game
wordbank = ['affix', 'bagpipes', 'bandwagon', 'banjo', 'buffalo',
            'cobweb', 'croquet', 'daiquiri', 'duplex', 'dwarves',
            'equip', 'exodus', 'fishhook', 'fixable', 'galaxy',
            'galvanize', 'ivy', 'juicy', 'kilobyte', 'megahertz',
            'oxygen', 'polka', 'quiz', 'rhubarb', 'schizophrenia',
            'unzip', 'uptown', 'vodka', 'whiskey', 'zombie']

bored = False
while not bored:
    # Draw the gallows
    turtle.home()
    turtle.pendown()
    turtle.left(90)
    turtle.forward(175)
    turtle.left(90)
    turtle.forward(74)
    turtle.left(90)
    turtle.forward(35)
    turtle.penup()
    turtle.goto(-135, -35)
    
    # Choose a random word
    chosen_word = random.choice(wordbank)

    # Display placeholders for each letter in the word
    for _ in chosen_word:
        turtle.write('_ ', True, font=("Courier", 14, "normal"))

    correct_guesses = []
    incorrect_guesses = 0
    terminate = False

    # Game loop for guessing letters
    while incorrect_guesses < 6 and not terminate:
        letter = turtle.textinput('Hangman', 'Guess a letter:')
        turtle.goto(-135, -35)

        # Check if the guessed letter is correct
        if letter not in correct_guesses:
            for char in chosen_word:
                if char == letter:
                    turtle.write(letter.upper() + ' ', True, font=("Courier", 14, "normal"))
                    correct_guesses.append(letter)
                else:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))

        # If the guessed letter is incorrect, increment the wrong count and draw the hangman figure
        if letter not in chosen_word:
            incorrect_guesses += 1
            drawMan(incorrect_guesses)

        # Check if the player has won or lost
        if incorrect_guesses == 6:
            turtle.goto(-135, -35)
            for char in chosen_word:
                if char in correct_guesses:
                    turtle.write('_ ', True, font=("Courier", 14, "normal"))
                else:
                    turtle.write(char.upper() + ' ', True, font=("Courier", 14, "normal"))
            turtle.goto(-74, -60)
            turtle.write('Sorry, you lose! The word was: {}'.format(chosen_word.upper()),
                         False, align='center', font=("Courier", 14, "normal"))
        elif set(correct_guesses) == set(chosen_word):
            turtle.goto(-74, -60)
            turtle.write('Congratulations!', False, align='center', font=("Courier", 14, "normal"))
            terminate = True

    # Ask the player if they want to play again
    response = turtle.textinput('Hangman', 'Would you like to play again? (y or n): ')

    while response.lower() not in ['y', 'n']:
        response = turtle.textinput('Hangman', 'Please enter "y" or "n": ')

    if response.lower() == 'n':
        turtle.clear()
        turtle.home()
        turtle.write('Thanks for playing!', False, align='center', font=("Courier", 25, "normal"))
        bored = True
    else:
        turtle.clear()

  
