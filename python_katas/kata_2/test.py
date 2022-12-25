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
        # your code here
        pass



class TestFibonacciFixme(unittest.TestCase):
    """
    2 Katas
    """

    def test_sample(self):
        # your code here
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
        str1 = 'The Linux kernel is an amazing software'
        str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'
        self.assertEqual(questions.longest_common_prefix(str1, str2),"The Linux kernel is a")

        str1 = 'Hello World'
        str2 = 'Have a wonderful day'
        self.assertEqual(questions.longest_common_prefix(str1, str2), "H")

        str1 = 'Wonder'
        str2 = 'Wonderful'
        self.assertEqual(questions.longest_common_prefix(str1, str2), "Wonder")

        str1 = "What's going on"
        str2 = 'Hi everybody'
        self.assertEqual(questions.longest_common_prefix(str1, str2), "")


class TestRotateMatrix(unittest.TestCase):
    """
    2 Katas
    """
    def TestRotateMatrix(self):
        mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(questions.TestRotateMatrix(mat), [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]])

        mat=[]
        self.assertEqual(questions.TestRotateMatrix(mat), [])

        mat = [[1, 8, 9], [20, 60, 5], [2, 39, 5], [19, 100, 12]]
        self.assertEqual(questions.TestRotateMatrix(mat), [[19, 2, 20, 1],[100, 39, 60, 8],[12, 5, 5, 9]])


    #def test_sample(self):



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
