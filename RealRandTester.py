
import datetime
import time
import statistics

def return_digits(num):

    x = 9

    outnum = ""

    for ctr in range(x):

        right_now = datetime.datetime.now().isoformat()    

        substr = ""

        for i in right_now:
            if i.isnumeric():
                substr += str(i)

        dg = substr[-1:]

        outnum += dg

        time.sleep(.00001)

    aval = (float(outnum) * .000000001)     

    bval = round(aval, x)

    return(bval)

def transpose(num, ranm):

    prod = int(num * ranm)

    return(prod)

def random_number(val):

    res1 = return_digits(val)

    numa = float(numin)

    res2 = transpose(numa, res1)

    return res2

print("")

numin = input("Please enter a number to act as a range for the randomness: ")

print("")

numrep = input("How many times would you like to test this?: ")

numr = int(numrep)

alst = []

for ctr in range(numr):

    print(str(ctr))

    #try: 
    ans = random_number(numin)
    alst.append(ans)

    #except:

        #print("Recursion Error.")

outval = statistics.mean(alst)

print("The mean is: ", outval)


