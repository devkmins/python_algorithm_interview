def reverseString(s) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        print(s)
        left += 1
        right -= 1
        
reverseString(["h", "e", "l", "l", "o"])
