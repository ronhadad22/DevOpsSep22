import unittest
from python_katas.kata_1 import questions
from python_katas.utils import unittest_runner


testers = ['arikgraif', 'Dean Sorie', 'Rosin1992','gad', 'bibi']


class TestSumOfElements(unittest.TestCase):
    """
    1 Katas
    """

    def sum_of_element(elements):
        return sum(elements)

    def test_empty_list(self):
        lst = []
        self.assertEqual(questions.sum_of_element(lst), 0)


    def test_integers_list(self):
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(questions.sum_of_element(lst), 15)

    def test_negative_numbers(self):
        lst = [1, -6, 7, 0, 99]
        self.assertEqual(questions.sum_of_element(lst), 101)

    def test_all_zeros(self):
        lst = [0] * 50000
        self.assertEqual(questions.sum_of_element(lst), 0)


class TestVerbing(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        shortStringTest = "ha"
        self.assertEqual(questions.verbing(shortStringTest), "ha")

        addIngTest = "spray"
        self.assertEqual(questions.verbing(addIngTest), "spraying")

        addLyTest = "amazing"
        self.assertEqual(questions.verbing(addLyTest), "amazingly")

        testEmptyString = ""
        self.assertEqual(questions.verbing(testEmptyString), "")
        pass
class TestWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        testWords = ["take", "on", "me"]
        self.assertEqual(questions.words_concatenation(testWords), "take on me")

        testWords = ["hi", "mom"]
        self.assertEqual(questions.words_concatenation(testWords), "hi mom")

        testWords = []
        self.assertEqual(questions.words_concatenation(testWords), "")
        pass


class TestReverseWordsConcatenation(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        testReverseWord = ["hello", "my", "friend"]
        self.assertEqual(questions.reverse_words_concatenation(testReverseWord), "friend my hello")

        testReverseWord = ["go", "to", "the", "gym"]
        self.assertEqual(questions.reverse_words_concatenation(testReverseWord), "gym the to go")

        testReverseWord = []
        self.assertEqual(questions.reverse_words_concatenation(testReverseWord), "")
        pass

class TestIsUniqueString(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        testUnique = "abcdef"
        self.assertEqual(questions.is_unique_string(testUnique), True)

        testUnique = "aa"
        self.assertEqual(questions.is_unique_string(testUnique), False)

        testUnique = "ENJOY THIS-PARK"
        self.assertEqual(questions.is_unique_string(testUnique), True)

        testUnique = "asdfghjklzxcvbnma"
        self.assertEqual(questions.is_unique_string(testUnique), False)
        pass



class TestListDiff(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        listToDiff = [1, 3, 6, 10, 14, 25]
        self.assertEquals(questions.list_diff(listToDiff), [2, 3, 4, 4, 11])

        listToDiff = [4, 1, 7, 2, 11, 0]
        self.assertEqual(questions.list_diff(listToDiff), [-3, 6, -5, 9, -11])

        listToDiff = [5000, 1, 10000, 10]
        self.assertEqual(questions.list_diff(listToDiff), [-4999, 9999, -9990])
        pass

class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass




class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """
    def test_sample(self):
        # your code here
        pass

class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass

class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass

class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass



class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass

class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestCaesarCipher(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass
class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
