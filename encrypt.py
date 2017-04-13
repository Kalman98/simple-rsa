class Encrypt:
    def __init__(self):
        pub = int(input("Please enter the public key: "))
        mod = int(input("Please enter the modulus: "))
        num = int(input("Please enter the number to be encrypted: "))

        # when pow has a third argument, it uses it as a modulus - so the actual math
        # we're doing here is (num^pub % mod). The result is printed to the user, and
        # it is pretty much undecryptable (assuming your keys are secure enough)
        # without the twin private key
        print(pow(num, pub, mod))

Encrypt()
