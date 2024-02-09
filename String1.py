def isPalindrome(X):
    return X == X[::-1]


# Driver code
x = "maharajah"
ans = isPalindrome(x)

if ans:
    print("Yes")
else:
    print("No")
