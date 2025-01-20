# The signatures of this class and its public methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    # When instantiated, the ProfanityFilter gets initialized with a list of offensive keywords and a replacement template
    def __init__(self, keywords, template):
        self.keywords = sorted(keywords, key=len, reverse=True)
        self.template = template

    def clean(self, word):

        repeated_template = (self.template * (len(word) //
                             len(self.template) + 1))[:len(word)]
        return repeated_template

    def filter(self, msg):
        # A filter method should take a string that may contain offensive language and replace any occurrence of the keywords with a string that is generated from the template

        # If the word size is shorter than the template, a substring should be used that starts from the beginning, while for longer sizes, the template characters should be repeated as often as necessary

        for word in self.keywords:
            censored = self.clean(word)

            msg = msg.replace(word, censored)
            msg = msg.replace(word.capitalize(), censored)
            msg = msg.replace(word.upper(), censored)

        return msg


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
