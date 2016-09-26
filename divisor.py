def gcd(a, b):
    while a != 0 and b != 0:
        remainder = a % b
        a = b
        b = remainder
    else:
        print(str(a) + " is the greatest common divisor")
gcd(270, 192)
