"""
******
PART 3
******
The factorial function is defined below.

Define the combination function which takes two integer arguments, n and r, which represent the number of objects and the number to choose respectively. The function RETURNS (not print) how many combinations are possible. Return it as an integer (// may help here)

You are expected to call the defined factorial function inside the combination definition

The combination formula: n! / (r! * (n-r)!)  (! is factorial)
"""

# do not change the factorial function
def factorial(number):
  product = 1
  for i in range(1, number + 1):
    product *= i
  return product

def combination(n, r):  # do not change this line
  pass  # delete the word pass when you start writing your code
