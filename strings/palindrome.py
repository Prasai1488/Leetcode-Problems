# Check palindrome

def reverse_string(s):
    return s[::-1]

def check_palindrome(string):
    reversedString = reverse_string(string)
    if reversedString == string:
        return True 
    return False 

def main():
    string = "dad"
    if check_palindrome(string):
        print(f"'{string}' is a palindrome.")
    else:
        print(f"'{string}' is not a palindrome.")

if __name__ == "__main__":
    main()
