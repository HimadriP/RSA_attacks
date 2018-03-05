from random import randint

def miller_rabin(n, k=20):
    s, d = 0, n-1

    while d % 2 == 0:
        s += 1
        d /= 2

    for i in xrange(k):
        a = randint(2, n-1)
        x = pow(a, d, n)
        if x == 1:
            continue
        for r in xrange(s):
            if x == n-1:
                break
            x = (x*x) % n
        else:
            return False

    return True

n = input("Enter the number n :")
#a=attack({'n':570541})

print miller_rabin(570541)
