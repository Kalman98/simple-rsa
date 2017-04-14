class Decrypt:
    def __init__(self):
        pri = int(input("Please enter the private key: "))
        mod = int(input("Please enter the modulus: "))

        # putting a while loop here allows the user to use the same key/modulus
        # for multiple messages with ease. This makes it much easier to have
        # an encrypted conversation with someone for fun
        while True:
            num = int(input("Please enter the encrypted number to decrypt, or type 'exit' to quit: "))
            # if the user wishes to quit, we do so here
            if num == "exit":
                break
            # when pow has a third argument, it uses it as a modulus - so the actual math
            # we're doing here is (num^pri % mod). This is the _only_ way to decrypt a
            # message that was encrypted with the twin public key (assuming your keys
            # are secure enough)
            data = str(pow(num, pri, mod))
            print("Decrypted ASCII number: " + data)

            # we just need to do some fancy formatting to convert the ASCII numbers
            # back into readable text
            res = ""
            char = ""
            for count in range(len(data)):
                if (count + 1) % 3 == 0:
                    char += data[count]
                    res += chr(int(char))
                    char = ""
                else:
                    char += data[count]

            # print the final results - obviously
            print("Decrypted result: " + res)
Decrypt()
