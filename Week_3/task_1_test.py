from unittest import TestCase
import task_1 as script


class MyTestSuite(TestCase):
    def test_words_with_length(self):
        self.assertTrue(script.words_with_length(4) == ["jazz"])

    def test_words_containing_string(self):
        self.assertTrue(len(script.words_containing_string("pp"))
                        == 3)  # apple, pineapple and sapphire

    def test_words_starting_with_character(self):
        self.assertTrue(script.words_starting_with_character("c") == ["cloud"])

    def test_words_with_matching_ends(self):
        expected = ["river"]

        self.assertEqual(script.words_with_matching_ends(), expected)

    def test_words_with_unique_characters(self):
        expected = ['asteroid', 'guitar', 'keyboard',
                    'planet', 'mango', 'wizard', 'cloud']

        self.assertEqual(script.words_with_unique_characters(), expected)

    def test_count_unique_characters(self):
        expected = {'apple': 4, 'mountain': 7, 'river': 4, 'asteroid': 8, 'armadillo': 7, 'guitar': 6, 'sapphire': 7, 'keyboard': 8, 'planet': 6,
                    'mango': 5, 'mirror': 4, 'jazz': 3, 'robot': 4, 'lighthouse': 9, 'pineapple': 6, 'wizard': 6, 'cloud': 5, 'penguin': 6, 'spaghetti': 8}

        self.assertEqual(script.count_unique_characters(), expected)

    def test_dictionary(self):
        self.assertTrue(script.dictionary()["a"] == [
                        'apple', 'asteroid', 'armadillo'])
