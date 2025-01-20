from re import sub
from string import punctuation


def is_palindrome(s: str):
    # word, phrase, or sequence that reads the same backward as forward, ignoring spaces, punctuation, and case.
    # return True if s is a palindrome and False otherwise.
    # ignore all non-alphanumeric characters and should not differentiate between uppercase and lowercase letters.

    clean_str = sub(r"[^a-zA-Z0-9]", "", s).lower()

    if len(clean_str) <= 1:
        return True
    else:
        if clean_str[0] == clean_str[-1]:
            return is_palindrome(clean_str[1:-1])
        else:
            return False

    # The following lines call the function and prints the return
    # value to the Console. This way you can check what it does.
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("No lemon, no melon"))
print(is_palindrome("This is not a palindrome"))
