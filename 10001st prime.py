def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def _stPrime(n):
    numberOfPrimes=0
    prime=1
    while numberOfPrimes<n:
        prime+=1
        if isPrime(prime):
            numberOfPrimes+=1
    return prime

print(_stPrime(10001))