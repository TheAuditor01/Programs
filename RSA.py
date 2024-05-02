import math

def e_sel(phi):
    e = 2
    while (e < phi):
        if math.gcd(phi, e) == 1:
            break
        e += 1
    return e

def d_sel(e,phi):
    d = 1
    while True:
        if (e*d) % phi == 1:
            break
        d += 1
    return d

def encrypt(m,e,n):
    c = (m**e) % n
    return c

def decrypt(c,d,n):
    d_m = (c**d) % n
    return d_m

def isprime(num):
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def string_to_int(s):
    return [ord(c) for c in s]

def int_to_string(int_list):
    return ''.join(chr(i) for i in int_list)


p = int(input("Enter value for p (prime number only) - "))
q = int(input("Enter value for q (prime number only) - "))
m = int(input('Enter value for m - '))

if isprime(p) and isprime(q):
    n = p * q
    phi_n = (p-1) * (q-1)
    e = e_sel(phi_n)
    d = d_sel(e,phi_n)
    encrypted = encrypt(m,e,n)
    decrypted = decrypt(encrypted,d,n)

    print("\n--------------------------------------")
    print("Public Key - ", e)
    print("Private Key - ",d)
    print("--------------------------------------")

    print("\nCipher Text - ",encrypted)
    print("Decrypted Text - ",decrypted)
    print("\n--------------------------------------")

