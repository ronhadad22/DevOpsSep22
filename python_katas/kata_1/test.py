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
        self.assertEqual(questions.list_diff(listToDiff), [2, 3, 4, 4, 11])

        listToDiff = [4, 1, 7, 2, 11, 0]
        self.assertEqual(questions.list_diff(listToDiff), [-3, 6, -5, 9, -11])

        listToDiff = [5000, 1, 10000, 10]
        self.assertEqual(questions.list_diff(listToDiff), [-4999, 9999, -9990])
        pass


#BIBI - START
###################################################################################################################
class TestPrimeNumber(unittest.TestCase):
    """
    1 Katas
    """

    def test_prime_1(self):
        number = 7
        self.assertEqual(questions.prime_number(number), True)

    def test_prime_2(self):
        number = 17
        self.assertEqual(questions.prime_number(number), True)

    def test_prime_3(self):
        number = 13
        self.assertEqual(questions.prime_number(number), True)

    def test_not_prime_1(self):
        number = 1
        self.assertEqual(questions.prime_number(number), False)

    def test_not_prime_2(self):
        number = -20
        self.assertEqual(questions.prime_number(number), False)

    def test_not_prime_3(self):
        number = 2.4
        self.assertEqual(questions.prime_number(number), False)


class TestPalindromeNum(unittest.TestCase):
    """
    1 Katas
    """
    def test_pal1True(self):
        num = 1441
        self.assertTrue(questions.palindrome_num(num), "the num is palindrome but you return False")

    def test_pal2True(self):
        num = 11
        self.assertTrue(questions.palindrome_num(num), "the num is palindrome but you return False")

    def test_pal1False(self):
        num = 113
        self.assertFalse(questions.palindrome_num(num),"the num is not palindrome but you return True")

    def test_pal1Zero(self):
        num = 0
        self.assertTrue(questions.palindrome_num(num)," 0 is palindrom num but you return False")


class TestPairMatch(unittest.TestCase):
    """
    3 Katas
    """

    def test_Pair1(self):
        men = {'Ben': 34, 'Ronaldo': 37, 'Ancelotti': 62}
        women = {'Yasmin': 22, 'Inbar': 18, 'Angelina': 52}
        self.assertEqual(questions.pair_match(men, women), ('Ancelotti', 'Angelina'))

    def test_Pair2(self):
        men = {'Roi': 65, 'Eran': 82, 'Ido': 20}
        women = {'Sivan': 70, 'Orly': 18, 'Neta': 65}
        self.assertEqual(questions.pair_match(men, women), ('Roi', 'Neta'))


class TestBadAverage(unittest.TestCase):
    """
    1 Katas
    """

    def test_easy_peasy(self):
        self.assertEqual(questions.bad_average(10, 20, 30), 20)

    def test_zeros(self):
        self.assertEqual(questions.bad_average(0, 3, 0), 1)

    def test_fractions_in_answer(self):
        self.assertEqual(questions.bad_average(1, 1, 1), 1)

    def test_mistake(self):
        self.assertNotEqual(questions.bad_average(10, 20, 30), 30)


class TestBestStudent(unittest.TestCase):
    """
    1 Katas
    """

    def test_best_student_original_example(self):

        dict1 = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
        }
        self.assertEqual(questions.best_student(dict1), 'Natan')

    def test_best_student_over_grades(self):
        dict1 = {
            "Ben": 178,
            "Hen": 188,
            "Natan": 299,
            "Efraim": 365,
            "Rachel": -95
        }
        self.assertEqual(questions.best_student(dict1), 'Efraim')

    def test_best_student_same_gardes(self):
        dict1 = {
            "Ben": 88,
            "Hen": 88,
            "Natan": 88,
            "Efraim": 88,
            "Rachel": 88
        }
        self.assertEqual(questions.best_student(dict1), 'Ben')

    def test_best_student_float_grades(self):
        dict1 = {
            "Ben": 7.5,
            "Hen": 8,
            "Natan": 9,
            "Efraim": 5.5,
            "Rachel": 9.1
        }
        self.assertEqual(questions.best_student(dict1), 'Rachel')

#BIBI - END
###################################################################################################################

class TestPrintDictAsTable(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):

        dict1 = {
            "Ben": 78,
            "Hen": 88,
            "Natan": 99,
            "Efraim": 65,
            "Rachel": 95
            }
        newString = ""
        for k, v in dict1.items():
            newString = newString + ("{:<10} {:<10}\n".format(k, v))

        self.assertEqual(questions.print_dict_as_table(dict1), newString)



class TestMergeDicts(unittest.TestCase):
    """
    1 Katas
    """

    def test_merge_dicts(self):
        # Test two empty dictionaries
        self.assertEqual(merge_dicts({}, {}), {})

        # Test a dictionary with keys and values and an empty dictionary
        self.assertEqual(merge_dicts({"a": 1, "b": 2}, {}), {"a": 1, "b": 2})

        # Test an empty dictionary and a dictionary with keys and values
        self.assertEqual(merge_dicts({}, {"a": 1, "b": 2}), {"a": 1, "b": 2})

        # Test two dictionaries with the same keys
        self.assertEqual(merge_dicts({"a": 1, "b": 2}, {"a": 3, "b": 4}), {"a": 3, "b": 4})

        # Test two dictionaries with different keys
        self.assertEqual(merge_dicts({"a": 1, "b": 2}, {"c": 3, "d": 4}), {"a": 1, "b": 2, "c": 3, "d": 4})


class TestSevenBoom(unittest.TestCase):
    """
    1 Katas
    """

    def test_seven_boom(self):
        # Test a number that is not a multiple of 7
        self.assertEqual(seven_boom(10), [])

        # Test a number that is a multiple of 7
        self.assertEqual(seven_boom(49), ["Boom!"])

        # Test a number that is a multiple of 7 and has a 7 in it
        self.assertEqual(seven_boom(77), ["Boom!", "Boom!"])

        # Test a number that is a multiple of 7 and has a 7 in it and ends in 7
        self.assertEqual(seven_boom(707), ["Boom!", "Boom!", "Boom!"])



class TestCaesarCipher(unittest.TestCase):
    """
    1 Katas
    """

    def test_caesar_cipher(self):
        # Test a string with only lowercase letters
        self.assertEqual(caesar_cipher("hello", 3), "khoor")

        # Test a string with only uppercase letters
        self.assertEqual(caesar_cipher("HELLO", 3), "KHOOR")

        # Test a string with both lowercase and uppercase letters
        self.assertEqual(caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")

        # Test a string with a shift value of 0
        self.assertEqual(caesar_cipher("Hello, World!", 0), "Hello, World!")


class TestSumOfDigits(unittest.TestCase):
    """
    1 Katas
    """

    def test_sum_of_digits(self):
        # Test a string with only digits
        self.assertEqual(sum_of_digits("12345"), 15)

        # Test a string with digits and non-digit characters
        self.assertEqual(sum_of_digits("a1b2c3d4e5"), 15)

        # Test an empty string
        self.assertEqual(sum_of_digits(""), 0)


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
