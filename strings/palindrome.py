# Check palindrome

# def reverse_string(s):
#     return s[::-1]

# def check_palindrome(string):
#     reversedString = reverse_string(string)
#     if reversedString == string:
#         return True 
#     return False 

# def main():
#     string = "olo"
#     if check_palindrome(string):
#         print(f"'{string}' is a palindrome.")
#     else:
#         print(f"'{string}' is not a palindrome.")


# main()


# Time Complexity : O(n)
# Space complexity : O(n)



# ? Alternative approach : 2 pointers method

def check_palindrome(string):
    left,right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True

# Time complexity : O(n)
# Space complexity : O(1)

