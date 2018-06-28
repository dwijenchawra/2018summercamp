#LOOP
#REVIEWSHEET
#IN
#RECURSIVE
#FUNCTIONS

#1
def factorial(x):
    x-=1
    if x>1:
        return factorial(x) * x
    else:
        return x

def factorial_call(x):
    return factorial(x+1)

#print(factorial_call(1000))

#2 skipped

#3

def stars(x, starz):
    star = "*"
    if x >= starz:
        print(star * starz)
        starz = starz + 1
        stars(int(x), starz)
#    else:

def star_call(x):
    starcount = 1
    stars(x, starcount)


#star_call(5)

# 4
#write a loop that adds the digits of an input eg. 16214 gives you 14
def adddigits(x, length, digit_add):
    digit_add = digit_add
    length = length - 1
    if length >= 1:
        divisor = (10 ** (length))
        truncated = int(x / divisor)
        digit_add = digit_add + truncated % 10
        print(digit_add)
        adddigits(x, length, digit_add)


def adddigits_call(x):
    place = len(str(x))
    adddigits(x, place + 1, 0)

print(adddigits_call(16214))
