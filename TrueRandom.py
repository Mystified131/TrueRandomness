
import datetime
import time

def return_digits(num):
    
    outlst = []

    for ctr in range(num):

        right_now = datetime.datetime.now().isoformat()    

        substr = ""

        for i in right_now:
            if i.isnumeric():
                substr += str(i)

        dg = substr[-1:]

        outlst.append(dg)

        time.sleep(.0001)

    return(outlst)

def transpose(num, ranlst):
    instr = []
    for elem in num:
        instr.append(elem)

    print(instr)

    x = len(instr)

    anstr = ""
    
    prd = ranlst[0]
    prod = (float(prd)) * .1
    var = int(num[0])
    produ = int(prod * var)
    anstr += str(produ)

    for ctr in range(1, x):
        valb = ranlst[ctr]
        anstr += valb

    if float(num) <= 1:
        anstr = 1

    if float(anstr) == 0:
        anstr = transpose(num, ranlst)
    
    return(anstr)


print("")

numin = input("Please enter a number to act as a range for the randomness: ")

va = len(numin)

res1 = return_digits(va)

print(res1)

res2 = transpose(numin, res1)

print(res2)

print("")

ans = int(res2)

print("The answer is: ", ans)


