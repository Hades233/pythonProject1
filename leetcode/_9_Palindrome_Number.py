def isPalindrome(x):
    temp = str(x)
    if temp == temp[::-1]:
        return True
    else:
        return False


y = input()
print(isPalindrome(y))
