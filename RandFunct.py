
def return_digits(num):

    import datetime
    import time

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

        time.sleep(.0001)

    out = float(outnum)

    aval =  out * .000000001    

    bval = round(aval, x)

    return(aval)

def transpose(num, ranm):

    prod = int(round(num * ranm))

    return(prod)

def random_number(val):

    res1 = return_digits(val)

    numa = float(numin)

    res2 = transpose(numa, res1)

    return res2

print("")

numin = input("Please enter a number to act as a range for the randomness: ")

print("")

ans = random_number(numin)

print("The number is: ", ans)


