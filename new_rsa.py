def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(e, phi):
    if e == 0:
        return phi
    else:
        return gcd(phi % e, e)

def main():
    # Get user input
    p = int(input("Enter the value of p: "))
    q = int(input("Enter the value of q: "))
    original_message = int(input("Enter the original message: "))

    # Check if p and q are prime
    if not is_prime(p) or not is_prime(q):
        print("Error: p and q must be prime numbers.")
        return

    n = p * q
    print("The value of n =", n)

    phi = (p - 1) * (q - 1)
    print("The value of phi =", phi)

    # Calculating e value
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Calculating d value
    for i in range(10):
        x = 1 + (i * phi)
        if x % e == 0:
            d = x // e
            break

    print("The value of d =", d)

    # Encrypted message
    c = pow(original_message, e, n)
    print("Encrypted message:", c)

    # Decrypted message
    m = pow(c, d, n)
    print("Decrypted message:", m)

if __name__ == "__main__":
    main()
