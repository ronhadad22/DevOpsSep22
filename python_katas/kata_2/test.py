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
        print(merge_sorted_lists([1, a, 9, 77, 13343], [-7, 0, 7, 23]))our code here
        pass

#vitaly
class TestMergeSortedLists(unittest.TestCase):
    """
    1 Katas
    """
     def merge_sorted_lists(l1, l2):
        return ("The combined sorted list is : " + str(res))


     def test_empty_lists(self):
          l1 = []
          l2 = []
     self.assertEqual(questions.merge_sorted_lists(l1, l2), [ ])

     def test_zero_lists(self):
          l1 = [0]
          l2 = [0]
     self.assertEqual(questions.merge_sorted_lists(l1, l2), [0,0])

     def test_same.num_lists(self):
         l1 = [1, 3, 8]
         l2 = [2, 3, 9]
     self.assertEqual(questions.merge_sorted_lists(l1, l2), [1, 2, 3, 3, 8, 9])

      def test_negative.num_lists(self):
         l1 = [-8, -3, 8]
         l2 = [-2, 3, 9]
      self.assertEqual(questions.merge_sorted_lists(l1, l2), [-8, -3, -2, 3, 8, 9])



#vitaly
class TestLongestCommonSubstring(unittest.TestCase):
    """
    4 Katas
    """
    def test_empty_strings(self):
       str1, str2 = ('','')
    self.assertEqual(questions.longest_common_substring(str1, str2), )

    def test_CapitalwithRegular_strings(self):
        str1, str2 = ('AbbZD', 'abZd')
    self.assertEqual(questions.longest_common_substring(str1, str2), bZ)

    def test_empty_strings(self):
        str1, str2 = ('a2a', 'a2a')
    self.assertEqual(questions.longest_common_substring(str1, str2), a)


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
