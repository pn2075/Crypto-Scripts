from RSA_129 import *
from inverseMod import *

plain = 738384834077855068695095698649685178675141
digit_prime = 70139406590594083983359939509724561365896181483069
print("\n")
cipher = caculate_rsa(digit_prime, 7, 257, plain)
print("Cipher text", cipher)
decrpyt = backward_rsa(digit_prime, 7, 257, cipher)
print("plaintext:", decrpyt)
totient= (digit_prime-1)*6
print("totient:",totient)
print(inverseMod(257,totient))
