'''There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme.

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113".

Help the Commander assign these IDs by writing a function answer(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.'''

from math import log
def answer(n):
    primestring = generatePrimeString(20220) #hard coded Prime range to satisfy \									 #10000 index length
    return primestring[n:n+5]

def generatePrimeString(n):
	'''generate all prime number from 0 to N'''
    primes = [True]* (n + 1)
    for p in range(2, n + 1):
        if primes[p]:
            k = p
            while k * p <= n:
                primes[k * p] = [False]
                k += 1
    primeStr = ''.join(str(i) \
						for i, val in enumerate(primes) \
							if primes[i]==True and i >= 2)
    return primeStr





# More complex way of finding  prime range to satisfy given range

from math import log
def answer(n):
    # your code here
    if n >= 0 and n <= 10000:
        primestring = generatePrimeString(n)
        return primestring[n:n+5]

def nprimes(n):
    primes = [True]* (n + 1)
    for p in range(2, n + 1):
        if primes[p]:
            k = p
            while k * p <= n:
                primes[k * p] = [False]
                k += 1
    primeStr = ''.join(str(i) \
                        for i, val in enumerate(primes) \
                            if primes[i]==True and i >= 2)
    return primeStr



def generatePrimeString(n):
    return prime_range_str(n)

def prime_range_str(n):
    sin_dig_ln = (10 // log(10))
    dou_dig_ln = (100 // log(100)) * 2 + sin_dig_ln
    tri_dig_ln = (1000 // log(1000)) * 3 + dou_dig_ln
    fou_dig_ln = (10000 // log(10000)) * 4 + tri_dig_ln

    if n < dou_dig_ln:
        return nprimes(100)
    elif n < tri_dig_ln:
        return nprimes(1000)
    elif n < fou_dig_ln:
        return nprimes(10000)
    else:
        return nprimes(20220) # n / log(n) == 10000 ==> better value is 20220    
    return str(pri)
