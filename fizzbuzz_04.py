# (text homework)
# run FizzBuzz sequence from either user-supplied number (variable) or from 1


# if sys.argv has more arguments than 1 (sys.argv[0] - filename), save to var "start"
# else, use supplied argument (stored in sys.argv[1], save to var "start"
# convert (var in) start to integer
# print (var) start
# while start is less than 101, do fizzbuzz routine beginning from (var) start 



"""
import sys

def fizzy():
	if len(sys.argv) >= 2:
		start = sys.argv[1]
	else:
		start = 1
	start = int(start)
	print start
	print " "
	while start < 101:
		if start % 3 == 0 and start % 5 == 0:
			print "FizzBuzz"
		elif start % 5 == 0:
			print "Buzz"
		elif start % 3 == 0:
			print "Fizz"
		else:
			print start
		start += 1

fizzy()
"""

# run FizzBuzz sequence beginning from user-supplied number using raw_input

def fizzbee():
	start = raw_input("Where do you want me to start FizzBuzzing from? > ")
	start = int(start)

	while start < 101:
		if start % 3 == 0 and start % 5 == 0:
			print "FizzBuzz"
		elif start % 5 == 0:
			print "Buzz"
		elif start % 3 == 0:
			print "Fizz"
		else:
			print start
		start += 1


fizzbee()





