# check if two strings are anagrams to each other


# method to sort string
# sortedString = ''.join(sorted(string))


# sorting approach:
# def check_anagrams(str1,str2):
#     sorted1 = ''.join(sorted(str1.lower()))
#     sorted2 = ''.join(sorted(str2.lower()))

#     if sorted1 == sorted2:
#         return True
#     else:
#         return False


# def main():
#     string1 = "Lemon"
#     string2 = "meonl"

#     if check_anagrams(string1, string2):
#         print("The strings are anagrams.")
#     else:
#         print("The strings are not anagrams.")


# main()


# Counter approach :
from collections import Counter

def check_anagrams(str1, str2):

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return Counter(str1) == Counter(str2)  

def main():
    if check_anagrams("hellO world", "ollhe rwdol"):
        print("Anagram")
    else:
        print("Not anagrams")

main()
