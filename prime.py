__author__ = 'galvin'
#-*-coding:utf-8-*-

import math
def isPrime(n):  #判断是是否为素数
    if(n<0 or n==1 or n==0):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
        else:
            continue
    return True

if __name__ == '__main__':
    k = 1
    n = 0
    while True:
        if isPrime(k):
            M = 2**k-1
            if isPrime(M):
                print(M)
                n+=1
            k+=1
        elif(n==5):
            break
        else:
            k+=1
