# Authored by Roc Zhang - github:Zhang-Haipeng - email:roc_zhang@hotmail.com
# date: 2020-02-23
from test_script.test import test_longest_palindrome

def longestPalindrome(s):
    """
    The idea is to iterate and check through all possible combinations, and return the longest palindrome.
    """    
    longest = ''
    for i in range(len(s),1,-1):
        for j in range(len(s)):
            n = s[j:(i+j)]
            if (n == n[::-1]):
                if len(n) > len(longest): # update the longest
                    longest = n
    return longest

if __name__ == '__main__':
    test_longest_palindrome(longestPalindrome)