# An ugly number is a positive integer whose prime factor are limited to 2, 3 or 5. Give an integer n, return "TRUE" if n is an ugly number

def findUglyNum(n):
    if n <= 0:
        return False
    
    for num in [2,3,5]:
        while n % num == 0:
         n= n // num
    return n == 1