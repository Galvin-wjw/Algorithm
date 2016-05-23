__author__ = 'galvin'
#-*-coding:utf-8-*-
#菲波那切数列


def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))

if __name__ == '__main__':
   for i in range(1,51):
       print(fib(i))
