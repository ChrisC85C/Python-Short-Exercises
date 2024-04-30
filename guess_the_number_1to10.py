from random import randint

# Generate a random number:
rand_number = randint(1,10)

#repeat code until correct number is guessed

while True:
    number = int(input("Input your number from 1 to 10: "))

    if rand_number < number:
        print(" Try again, too high")
    elif rand_number > number:
        print ("Try again, too low!")
    else:
        print("Correct, you guessed the number")
        break