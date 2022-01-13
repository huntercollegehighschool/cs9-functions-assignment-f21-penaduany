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

def combination(n, r):
  new_n = 1
  for i in range (1, n + 1):
    new_n *= i
  new_r = 1
  for w in range (1, r+1):
    new_r *= w
  n_minus_r = 1
  for y in range (1, n-r + 1):
    n_minus_r *= y
  answer = new_n / (new_r * n_minus_r)
  return answer
  
