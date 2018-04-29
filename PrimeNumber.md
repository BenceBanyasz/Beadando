# Beadando
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def primeNo10001(n):
    numOfPrimes=0
    prime=1
    while numOfPrimes<n:
        prime+=1
        if isPrime(prime):
            numOfPrimes+=1
    return prime

print (primeNo10001(10001))
