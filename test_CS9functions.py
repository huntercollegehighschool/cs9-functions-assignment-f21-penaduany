import part1
import part2
import part3
import part4

def test_distinct():
  assert part1.distinct(1,5,3) == True, "1, 5, 3 should return Boolean value True"

  assert part1.distinct(2, 2, 13) == False, '2, 2, 13 should return Boolean value False'

  assert part1.distinct(1, -8, 1) == False, '1, -8, 1 should return Boolean value False'

  assert part1.distinct(0, 3, 3) == False, '0, 3, 3 should return Boolean value False'

def test_celsius():
  assert int(part2.celsius(32)) == 0, '32 degrees F is 0 degrees C'

  assert int(part2.celsius(100)) == 37, '100 degrees F is about 37 degrees C'

def test_combination():
  assert part3.combination(5, 3) == 10, 'Combination(5, 3) should return 10'

  assert part3.combination(10, 2) == 45, 'Combination(10, 2) should return 45'

  assert part3.combination(3, 0) == 1, 'Combination(3, 0) should return 1'

def test_possibletriangle():
  assert part4.possibletriangle(3, 5, 4) == True, '3, 4, 5 is a possible triangle'

  assert part4.possibletriangle(7, 2, 3) == False, 'A triangle with side lenghts 7, 2, and 3 is not possible'

  assert part4.possibletriangle(6, 1, 7) == False, 'A triangle with side lengths 6, 1, and 7 is not possible'