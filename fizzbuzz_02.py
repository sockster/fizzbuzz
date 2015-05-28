# want a loop, so need to define routine
# save zero in a var
# "if var % 3 == 0 AND var % 5 == 0"
# then print FizzBuzz
# elif var % 5 == 0
# then print Buzz
# elif var % 3 == 0
# then print Fizz
# else print var
# var = var + 1



def fizzbuzz():
	for num in range(0, 102):
		num == (num + 1)
		if num > 100:
			print "WooHOO! We're done here!"
		else:
			if (num % 3) == 0 and (num % 5) == 0:
				print "FizzBuzz"
			elif (num % 5) == 0:
				print "Buzz"
			elif (num % 3) == 0:
				print "Fizz"
			else:
				print num

num = 0

fizzbuzz()
