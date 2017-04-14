class Encrypt:
    def __init__(self):
        pub = int(input("Please enter the public key: "))
        mod = int(input("Please enter the modulus: "))

        # putting a while loop here allows the user to use the same key/modulus
        # for multiple messages with ease. This makes it much easier to have
        # an encrypted conversation with someone for fun
        while True:
            num = input("Please enter the number to be encrypted, or 'exit' to quit: ")
            # if the user wants to stop, we do it here
            if num == "exit":
                break

            # we need to do some fancy formatting to convert the string into a big long
            # number made up of each character's individual ASCII ID
            data = ""
            for i in num:
                if len(str(ord(i))) <= 2:
                    # on the chance that the character ID is only two numbers long, we here insert
                    # a 0 so that the decryptor can easily find all of the three-number segments
                    # without having changed any values
                    data += "0"
                data += str(ord(i))

            print("ASCII number: " + data)
            data = int(data)

            # when pow has a third argument, it uses it as a modulus - so the actual math
            # we're doing here is (num^pub % mod). The result is printed to the user, and
            # it is pretty much undecryptable (assuming your keys are secure enough)
            # without the twin private key
            res = pow(data, pub, mod)

            print("Encrypted result: " + str(res))
Encrypt()
