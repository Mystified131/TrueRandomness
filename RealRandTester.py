
import datetime
import time
import statistics

#This function retrieves a product to use as a multiplier with with original number

def return_digits(num):

    x = 9
    
    if len(num) > 9:
        x = len(num)

    dv = "."

    for x1 in range(x - 1):
        dv += "0"

    dv += "1"

    div = float(dv)

    outnum = ""

    for ctr in range(x):

        right_now = datetime.datetime.now().isoformat()    

        substr = ""

        for i in right_now:
            if i.isnumeric():
                substr += str(i)

        dg = substr[-1:]

        outnum += dg

        time.sleep(.0000001)

    aval = (float(outnum) * div)     

    bval = round(aval, x)

    return(bval)

#This function uses the second argument to transform the first via multiplication

def transpose(num, ranm):

    prod = int(num * ranm)

    return(prod)

#This function sets up and calls the other two, from a simple original value. It returns a "randomized" integer.

def random_number(val):

    res1 = return_digits(val)

    numa = float(numin)

    res2 = transpose(numa, res1)

    return res2

##################################

#This code is for getting the input from the console and calling the function(s)

print("")

numin = input("Please enter a number to act as a range for the randomness: ")

print("")

numrep = input("How many times would you like to test this?: ")

numr = int(numrep)

alst = []

#This code calculates and shares the mean value to test the function

for ctr in range(numr):

    #print(str(ctr))
 
    ans = random_number(numin)
    print(ans)
    alst.append(ans)

outval = statistics.mean(alst)

print("The mean is: ", outval)


