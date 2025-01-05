# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# numbers = [1,2,1,3,4]

# first = set(numbers)
# print(first)

def check_duplicates(num):
    hashSet = set()

    for n in num:
        if n in hashSet:
            return True
        hashSet.add(n)
    return False 


def main():
    numbers = [1,2,3,4,4]
    print(check_duplicates(numbers))

main()