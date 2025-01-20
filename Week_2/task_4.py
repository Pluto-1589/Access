def transform_string(s):
    index_colon = s.find(":")

    right = s[index_colon:].upper()
    left = s[:index_colon].lower()

    return left + right


print(transform_string("aB:cD"))
