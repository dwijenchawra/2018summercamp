# question 4
def double(x):
    print(x * 2)


double(2)

#question 5
def q5():
    number = int(input("Enter a number:  "))
    if number > 0:
        print(number + 1)
    else:
        print(number - 1)
q5()

def spam():
    word = ""
    while word != "stop":
        word = input("Enter a word:  ")
spam()

def star():
    star = "*"
    num = 0
    while num < 5:
        print(star)
        star = star + "*"
        num = num + 1
star()

def factorial():
    fact = 1
    number = int(input("Enter a number:  "))
    for i in range(1, number + 1):
        fact = fact * i
    print(fact)


factorial()
