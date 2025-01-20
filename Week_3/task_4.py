import string


def rot_n(plain_text, shift_by):

    encoded_text = ""

    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase

    for i in plain_text:
        if i.islower():
            idx = alpha_lower.index(i)
            shift_to_letter = (idx + shift_by) % 26
            encoded_text += alpha_lower[shift_to_letter]
        elif i.isupper():
            idx = alpha_upper.index(i)
            shift_to_letter = (idx + shift_by) % 26
            encoded_text += alpha_upper[shift_to_letter]
        elif i not in string.ascii_letters:
            encoded_text += i
    return encoded_text


print(rot_n("abcd!", 5))
