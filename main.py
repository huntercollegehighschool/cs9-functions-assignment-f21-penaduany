"""
Any user inputs and console outputs (input and print) is handled below. The code you write should not involve input or print.
"""

import os

def main():
  program = input("Enter 1, 2, 3, or 4: ")
  while program not in ['1', '2', '3', '4']:
    os.system('clear')
    print("That's not a valid input.")
    program = input("Enter 1, 2, 3, or 4: ")

  os.system('clear')
  program = int(program)
  
  if program == 1:
    from part1 import distinct
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    num3 = int(input("Enter a number: "))
    print(distinct(num1, num2, num3))

  elif program == 2:
    from part2 import celsius
    fahrenheit = float(input("Enter fahrenheit: "))
    print(celsius(fahrenheit))
  
  elif program == 3:
    from part3 import combination
    objects = int(input("n: "))
    choices = int(input("r: "))
    print(combination(objects, choices))
  
  elif program == 4:
    from part4 import possibletriangle
    s1 = float(input("First side length: "))
    s2 = float(input("Second side length: "))
    s3 = float(input("Third side length: "))
    print(possibletriangle(s1, s2, s3))

if __name__ == '__main__':
  main()