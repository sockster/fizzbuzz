# 	fizzbuzz 2 uses "range"
# 	fizzbuzz 3 uses anything less than 101
#	- " += " is new



def Fizz():
    max = 0
    while max < 101:
        if max % 3 == 0 and max % 5 == 0:
            print "FizzBuzz"
        elif max % 5 == 0:
            print "Buzz"
        elif max % 3 == 0:
            print "Fizz"
        else:
            print max
        max += 1

Fizz()
