'''
******
PART 1
******
The function distinct() below takes three numbers as arguments, and returns True (Boolean value, not the string, so no quotes necessary) if the three numbers are all different, and False (Boolean value, not the string, so no quotes necessary) if not.

However, there are (at least) 7 errors in the code. Fix them so that it runs properly.
'''
def distinct(a, b, c):
  if a != b and b!= c and a != c:
    return True
  else:
    return False