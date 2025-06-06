from itertools import cycle, product
from pathlib import Path

cipher_path = Path(__file__).parent / "cipher.txt"
cipher = [int(ascii) for ascii in cipher_path.read_text().split(",")]


def xor(ascii: int, key: int) -> int:
    return ascii ^ key


# Generate every possible 3 character key
alpha = "abcdefghijklmnopqrstuvwxyz"
keys = [(ord(a), ord(b), ord(c)) for a, b, c in product(alpha, alpha, alpha)]

for key in keys:
    key_cycle = cycle(key)
    decoded = "".join([chr(xor(c, next(key_cycle))) for c in cipher])

    # Lets assume 'the' is a common english word we'd expect to see in the plain text message
    if " the " in decoded:
        print(decoded)
        print(sum([ord(c) for c in decoded]))

"""
An extract taken from the introduction of one of Euler's most celebrated papers, "De summis serierum reciprocarum" [On the sums of series of reciprocals]: I have recently found, quite unexpectedly, an elegant expression for the entire sum of this series 1 + 1/4 + 1/9 + 1/16 + etc., which depends on the quadrature of the circle, so that if the true sum of this series is obtained, from it at once the quadrature of the circle follows. Namely, I have found that the sum of this series is a sixth part of the square of the perimeter of the circle whose diameter is 1; or by putting the sum of this series equal to s, it has the ratio sqrt(6) multiplied by s to 1 of the perimeter to the diameter. I will soon show that the sum of this series to be approximately 1.644934066842264364; and from multiplying this number by six, and then taking the square root, the number 3.141592653589793238 is indeed produced, which expresses the perimeter of a circle whose diameter is 1. Following again the same steps by which I had arrived at this sum, I have discovered that the sum of the series 1 + 1/16 + 1/81 + 1/256 + 1/625 + etc. also depends on the quadrature of the circle. Namely, the sum of this multiplied by 90 gives the biquadrate (fourth power) of the circumference of the perimeter of a circle whose diameter is 1. And by similar reasoning I have likewise been able to determine the sums of the subsequent series in which the exponents are even numbers.
"""
