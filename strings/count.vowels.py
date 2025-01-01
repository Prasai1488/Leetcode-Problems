# count total number of vowels in a string

def countVowels(str):
    vowel = "aeiouAEIOU"
    count = 0

    for char in str:
        if char in vowel:
            count += 1
    return count

def main():
    string = "hll"
    result = countVowels(string)
    print(f"Number of vowels in '{string}' : {result}")

main()


# Time Complexity : O(n)
#  Space complexity : O(1)
