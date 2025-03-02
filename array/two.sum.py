# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


#using Hashmap approach :

def two_sum(num,target):
    prevMap = {}

    for i, n in enumerate(num):
        diff =  target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i

