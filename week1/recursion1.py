#LOOP
#REVIEWSHEET
#IN
#RECURSIVE
#FUNCTIONS

#1
def factorial(x):
    x -= 1
    if x > 1:
        return factorial(x) * x
    else:
        return x

def factorial_call(x):
    return factorial(x + 1)

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
    #print(length)
    if length >= 0:
        divisor = (10 ** (length))
        truncated = int(x / divisor)
        digit_add = digit_add + truncated % 10
        #print(digit_add)
        return adddigits(x, length, digit_add)
    else:
        return digit_add;

def adddigits_call(x):
    place = len(str(x))
    print(adddigits(x, place + 1, 0))

#adddigits_call(12345) #should give 15

#5 wont work its too simple



def poweroftwo(x, result,  exponent):
    exponent = exponent + 1
    #print(exponent)
    result = 2 ** exponent
    if result < x:
        #print(result)
        return poweroftwo(x, result, exponent)
    else:
        return exponent



def poweroftwo_call(x):
    #call other function in here
    exponent = poweroftwo(x, 0, -1)
    return 2 ** (exponent - 1)

#print(poweroftwo_call(45))



def trianglenumber(x, counter, final):
    counter = counter + 1
    #print("counter: " + str(counter))
    if final + counter <= x:
        #print("final: " + str(final))
        final = final + counter
        return trianglenumber(x, counter, final)
    else:
        return final

def trianglenumber_call(x):
    counter = 0
    final = 0
    final = trianglenumber(x, counter, final)
    return final


#print(trianglenumber_call(16))

def gcf(a, b, gcfnumber):
    gcfnumber = gcfnumber - 1
    if a % gcfnumber == 0 and b % gcfnumber == 0:
        return gcfnumber
    else:
        return gcf(a, b, gcfnumber)






def gcf_call(x, y):
    if x < y:
        number = x
    else:
        number = y
    number = number + 1
    return gcf(x, y, number)

#print(gcf_call(20, 18))
def print2():
    num = 8
    string = ""
    for i in range(1, num):
        for j in range(1, num):
            if i <= (7 - j):
                string += "1"
            else:
                string += str(i)
        print(string)
        string = ""
print2()