# function to check string is palindrome or not
def display(string):
    if isPalindrome(string):
        print("Yes")
    else:
        print("No")
def isPalindrome(s):
    length = len(s)
    i = length - 1
    for j in range(length//2):
        if s[i] != s[j]:
            return False
        i -= 1
    return True
s = "hinih"
display(s)
s = "hindi"
display(s)
