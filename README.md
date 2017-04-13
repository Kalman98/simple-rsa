# simple-rsa
A very basic RSA key generator with encryptor and decryptor that is written in Python3.

#### Generating Keys
Generating your own keys is easy. Run [srsa.py](https://github.com/Kalman98/simple-rsa/blob/master/srsa.py) to get a pair of keys, along with some various other outputs.

#### Encrypting
Run [encrypt.py](https://github.com/Kalman98/simple-rsa/blob/master/encrypt.py), input your public key, modulus (`n` from the key generator), and then the number you want encrypted. No support for text or other characters (yet!).

#### Decrypting
Run [decrypt.py](https://github.com/Kalman98/simple-rsa/blob/master/decrypt.py), input your private key, modulus (`n` from the key generator), and encrypted number. That's it!


## About
I started this project for fun when I was learning about RSA encryption. I wanted to prove to myself that I understood how it worked, and once I had done that, I decided to clean it up and push it to GitHub so maybe somebody else could learn from what I have. This is mostly meant as an educational project - **I do not make any guarantees that this technology will keep your information safe!**  To the best of my knowledge on encryption so far, it *should* work fine if used properly. But don't use this project for anything important, please. Just learning. :) Whoa, my first ever text emoji. I must be changing.


If you want more information on RSA encryption, [Wikipedia's RSA page](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) is a great place to start. That's where I got all of the information I needed to create this project.
