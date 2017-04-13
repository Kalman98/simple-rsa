from random import randint


class SRSA:
    def __init__(self):
        # p = int(input("Please enter a prime number: "))

        # if p == 0:
        #   print((65 ** 17) % 1003)
        #  return
        # if p == 1:
        #   print((745 ** 413) % 1003)
        #  return
        # q = int(input("Please enter another prime number: "))
        p = 279605045019893249881628621028381877897
        q = 210226533302810226362124704524479730699
        print("generating public key...")

        # n = pq. This will be our modulus when encrypting/decrypting later - so remember it!
        n = p * q
        print("n equals " + str(n))

        # self explanatory, 't' is equal to the least common multiple of (p - 1) and (q - 1)
        t = self.least_common_multiple(p - 1, q - 1)
        print("t equals " + str(t))

        # here we want 'e' to be equal to a number that has _no_ factors in common
        # with 't', besides the necessary '1' that all numbers have in common
        fail = True
        e = 0
        while fail:
            e = randint(1, t)
            if self.greatest_common_divisor(e, t) == 1:
                if e % t != 0:
                    fail = False

        print("e (public key) is " + str(e))
        print("generating private key...")

        # d is set to a modular inverse of (e % t). Simply put, this means that (ed % t) = 1
        # https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
        d = self.modular_inverse(e, t)

        print("d (private key) is " + str(d))

    # All of the following methods were copied from various places online. I will
    # work on them later to improve the readability and make them easier to
    # understand.
    # --------------------------------------------------------

    def greatest_common_divisor(self, *numbers):
        """Return the greatest common divisor of the given integers."""

        from math import gcd
        from functools import reduce
        return reduce(gcd, numbers)

    def least_common_multiple(self, *numbers):
        """Return lowest common multiple."""

        def lcm(a, b):
            return (a * b) // self.greatest_common_divisor(a, b)
        from functools import reduce
        return reduce(lcm, numbers, 1)

    # https: // en.wikipedia.org / wiki / Extended_Euclidean_algorithm
    def extended_greatest_common_divisor(self, a, b):
        """Returns the greatest common divisor and two other complicated numbers        """

        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.extended_greatest_common_divisor(b % a, a)
            return g, x - (b // a) * y, y

    def modular_inverse(self, a, m):
        """"Returns the modular inverse of a % m."""

        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
SRSA()
