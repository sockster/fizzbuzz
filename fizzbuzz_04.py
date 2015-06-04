# (text homework)
# run FizzBuzz sequence from either user-supplied number (variable) or from 1


# if sys.argv has more arguments than 1 (sys.argv[0] - filename), save to var "start"
# else, use supplied argument (stored in sys.argv[1], save to var "start"
# convert (var in) start to integer
# print (var) start
# while start is less than 101, do fizzbuzz routine beginning from (var) start 


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



















# this is my latest github attempt

# and now this line is created to see if
# git & github recognize this new version


#	2:11pm - 05/30/15 - FINALLY GOT GitHub (to work)!!!
#	pebcak ... 
#	first, changed default (per msg stating change for GitHub 2.0) because
#		"To squelch this message and maintain the current behavior after the default changes, use:
#	  git config --global push.default matching

#	To squelch this message and adopt the new behavior now, use:
#	  git config --global push.default simple
#	(I used "simple")

#	then set upstream master because  "The current branch master has no upstream branch":
#		git push --set-upstream origin master

