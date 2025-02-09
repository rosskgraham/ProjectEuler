"""
https://projecteuler.net/problem=67
Same solution as Problem 18 but wih a much bigger pyramid.
It is not possible to try every route to solve this problem, as there are 2^99 altogether!
If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all
"""
from pathlib import Path

pyramid = (Path(__file__).parent / "pyramid.txt").read_text()
pyramid = [[int(n) for n in row.split()] for row in pyramid.splitlines()]
 
for row in range(len(pyramid) - 2, -1, -1):
    for ele in range(row + 1):
        pyramid[row][ele] = pyramid[row][ele] + max(
            pyramid[row + 1][ele], pyramid[row + 1][ele + 1]
        )
    pyramid.pop()
print(pyramid[0][0])
