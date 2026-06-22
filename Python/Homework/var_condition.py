# Exercise 1:
# 1. Create a variable a and get an integer input using input().
# 2. Create a variable b and get an integer input using input().
# 3. Print the result of a + b.
# 4. Print the result of a * b.
#
# Hint:The input() function returns a string. You need to use int() to convert it to an integer.
#
# Exercise 2:
# 1. Create a variable a and get an integer input using input().
# 2. Create a variable b and get an integer input using input().
# 3. Compare the values of a and b, and print "a is greater than b", "a is less than b", or "a is equal to b" based on the result.
#
# Exercise 3:
# 1. Create a variable temperature and get an integer input using input().
# 2. Check the range of temperature:
# If temperature < 0, print "It's too cold".
# If 0 ≤ temperature < 15, print "It's a bit cold".
# If 15 ≤ temperature < 25, print "It's comfortable".
# If temperature ≥ 25, print "It's too hot".

t = 25
if t >= 25:
    print('too hot')
elif t >= 15:
    print('comfortable')

