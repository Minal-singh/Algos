from math import sqrt


def is_prime(n):
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    else:
        for i in range(5, int(sqrt(n)) + 1, 6):
            if (n % i == 0) or (n % (i + 2) == 0):
                return False
        else:
            return True


print(is_prime(97))
print(is_prime(99))
