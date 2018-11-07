from time import sleep
def countdown():
    number = int(input("Enter a number to count down from:   "))
    while number != 0:
        #sleep(1)
        print(number)
        number = number - 1
countdown()
