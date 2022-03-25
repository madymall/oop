def palindrome():
    x = input('Enter your number: ')
    if x == x[::-1]:
        return True
    else:
        return False

print(palindrome())



