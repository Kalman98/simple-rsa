class Decrypt:
    def __init__(self):
        pri = int(input("Please enter the private key: "))
        mod = int(input("Please enter the modulus: "))
        num = int(input("Please enter the encrypted number to decrypt: "))

        # when pow has a third argument, it uses it as a modulus - so the actual math
        # we're doing here is (num^pri % mod). This is the _only_ way to decrypt a
        # message that was encrypted with the twin public key (assuming your keys
        # are secure enough)
        print(pow(num, pri, mod))

Decrypt()
