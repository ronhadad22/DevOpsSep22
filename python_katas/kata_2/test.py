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



class TestValidParentheses(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):

       testparentheses = ["[[{()}](){}]"]
       self.assertEqual(questions.valid_parentheses(testparentheses), True)

       testparentheses = [""]
       self.assertEqual(questions.valid_parentheses(testparentheses), False)

       testparentheses = ["]}"]
       self.assertEqual(questions.valid_parentheses(testparentheses), False)

       testparentheses = ["[]}"]
       self.assertEqual(questions.valid_parentheses(testparentheses), False)



pass
pass
'''
    self.testparentheses = ('[[{()}](){}]')
self.bool = questions.valid_parentheses('testparentheses')

if self.bool is 'true':
    print("the sting '[[{()}](){}]' is pass")

self.testparentheses = ('')
bool = questions .valid_parentheses('testparentheses')
if self.testparentheses is 'true':
    print("the sting ' ' is none")

self.testparentheses = (']}')
bool = questions.valid_parentheses('testparentheses')

if self.bool is 'false':
    print("The is faild")

    pass

pass
'''


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
        pass
    pass

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


class TestLongestCommonPrefix(unittest.TestCase):
    """
    1 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestRotateMatrix(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestIsValidEmail(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


class TestPascalTriangle(unittest.TestCase):
    """
    3 Katas
    """

    def test_sample(self):
        # your code here
        pass


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
