import random
randomNumber1 = random.randint( 1, 250)
randomNumber2 = random.randint( 1, 250)

def askQuestion():
    global randomNumber1
    global randomNumber2
    userAnswer = int(  input( "What is " + str(  randomNumber1 ) + " + " + str( randomNumber2 ) +
                              " ?:" ) )

    return userAnswer

def checkAnswer( userAnswer ):
    global randomNumber1
    global randomNumber2

    correctAnswer = randomNumber1 + randomNumber2
    if userAnswer == correctAnswer:
        print("Congratulations You Got It Right!")

    else:
        print("the correct answer was " + correctAnswer)



def main():
    userAnswer = askQuestion()
    checkAnswer( userAnswer )

main()
    
