import unittest
from python_katas.kata_2 import questions
from python_katas.utils import unittest_runner

testers = ['dariakalugny',
 'gilberger1234',
 'trzh55',
 'mortis1983',
 'vitvizel',
 'shaniben1',
 'daniataal',
 'HappyToast17']


#Dria
class TestValidParentheses(unittest.TestCase):
    """
    3 Katas
    """
    def test_sample(self):
        def test_sample(self):
            testparentheses = ["[[{()}](){}]"]
            self.assertEqual(questions.valid_parentheses(testparentheses), True)

            testparentheses = [""]
            self.assertEqual(questions.valid_parentheses(testparentheses), False)

            testparentheses = ["]}"]
            self.assertEqual(questions.valid_parentheses(testparentheses), False)

            testparentheses = ["[]}"]
            self.assertEqual(questions.valid_parentheses(testparentheses), False)

#Dria
class TestFibonacciFixme(unittest.TestCase):
    """
    2 Katas
    """
    def test_sample(self):
            number = 6
            self.assertEqual(questions.fibonacci_fixme(number), 8)

            number = 5
            self.assertEqual(questions.fibonacci_fixme(number), 8)

            number = 0
            self.assertEqual(questions.fibonacci_fixme(number), 0)

            number = 7
            self.assertEqual(questions.fibonacci_fixme(number), 8)

class TestMostFrequentName(unittest.TestCase):
    """
    2 Katas
    """
    def test_sample(self):
        # your code here
        pass

class TestFilesBackup(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestReplaceInFile(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestJsonConfigsMerge(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestMonotonicArray(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestMatrixAvg(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestMergeSortedLists(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestLongestCommonSubstring(unittest.TestCase):
    """
    4 Katas
    """

    def test_sample(self):
        # your code here
        pass

#Shani
class TestLongestCommonPrefix(unittest.TestCase):
        """
        1 Katas
        """

        def test_sample(self):
            str1 = 'The Linux kernel is an amazing software'
            str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'
            self.assertEqual(questions.longest_common_prefix(str1, str2), "The Linux kernel is a")

            str1 = 'Hello World'
            str2 = 'Have a wonderful day'
            self.assertEqual(questions.longest_common_prefix(str1, str2), "H")

            str1 = 'Wonder'
            str2 = 'Wonderful'
            self.assertEqual(questions.longest_common_prefix(str1, str2), "Wonder")

            str1 = "What's going on"
            str2 = 'Hi everybody'
            self.assertEqual(questions.longest_common_prefix(str1, str2), "")

#Shani
class TestRotateMatrix(unittest.TestCase):
        """
        2 Katas
        """
        def TestRotateMatrix(self):
            mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
            self.assertEqual(questions.TestRotateMatrix(mat), [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]])

            mat = []
            self.assertEqual(questions.TestRotateMatrix(mat), [])

            mat = [[1, 8, 9], [20, 60, 5], [2, 39, 5], [19, 100, 12]]
            self.assertEqual(questions.TestRotateMatrix(mat), [[19, 2, 20, 1], [100, 39, 60, 8], [12, 5, 5, 9]])

#Dani
class TestIsValidEmail(unittest.TestCase):
    """
    3 Katas
    """

    def is_valid_email(mail_str):
        return (mail_str)


    def test_valid_email(self):
        mail_str = 'dani.atalla@cnvrg.io'
        self.assertEqual(questions.is_valid_email(mail_str), True)

    def test_invalid_email(self):
        mail_str = 'dani22.atalla@cnvrg.io'
        self.assertEqual(questions.is_valid_email(mail_str), False)

    def test_bad_syntax(self):
        mail_str = '@gmail.com'
        self.assertRaises(ValueError, questions.is_valid_email, mail_str)
#Dani
class TestPascalTriangle(unittest.TestCase):
    """
     3 Katas
     """

    def pascal_triangle(lines):
        return (lines)

    def test_positive_lines(self):
        lines = 7
        self.assertEqual(questions.pascal_triangle(lines), 7)

    def test_negative_lines(self):
        lines = -7
        self.assertEqual(questions.pascal_triangle(lines), -7)

    def test_huge_amount_of_lines(self):
        lines = 100
        self.assertEqual(questions.pascal_triangle(lines), 100)

    def test_zero_as_input(self):
        lines = 0
        self.assertIsNotNone(questions.pascal_triangle(lines))

    def test_no_input(self):
        lines = ''
        self.assertRaises(ValueError, questions.pascal_triangle, lines)

class TestListFlatten(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass



class TestStrCompression(unittest.TestCase):
    """
    2 Katas
    """
    def test_sample(self):
        # your code here
        pass



class TestStrongPass(unittest.TestCase):
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
