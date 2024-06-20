# Given a string s, return the
# longest palindromic substring in s.

def longestPalindrome(s: str) -> str:
    result = ''
    resLen = 0
    long = len(s)
    for i in range(long):
        l, r = i, i + 1
        while l >= 0 and r < long and s[l] == s[r]:
            if r - l + 1 > resLen:
                result = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
        l, r = i, i
        while l >= 0 and r < long and s[l] == s[r]:
            if r - l + 1 > resLen:
                result = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return result
