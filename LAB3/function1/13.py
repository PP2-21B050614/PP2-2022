print("Hello! What is your name?")
name = input()
from random import *
print("Well, KBTU, I am thinking of a number between 1 and 20.")
a=randint(1,20)
k=0
while True:
    k+=1
    print("Take a guess.")
    n=int(input())
    if n<a:
        print("Your guess is too low.")
    elif n>a:
        print("Your guess is too high")
    else:
        print("Good job, KBTU! You guessed my number in",k,"guesses!")
        break