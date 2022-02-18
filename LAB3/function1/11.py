s = input()

def palindrome(s):
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("not Palindrome")

palindrome(s)