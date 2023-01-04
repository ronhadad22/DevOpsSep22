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
            self.assertEqual(questions.fibonacci_fixme(number), 5)

            number = 0
            self.assertEqual(questions.fibonacci_fixme(number), 0)

            number = 7
            self.assertEqual(questions.fibonacci_fixme(number), 13)
#Gil
class TestMostFrequentName(unittest.TestCase):



   def most_frequent_name(file_path):
       return file_path

   def test_out_of_folder_directory(self):
       file_path = "names2.txt"
       self.assertEqual(questions.most_frequent_name(file_path), "Most repeated name: danny")
       return file_path

   def test_in_folder_directory(self):
       file_path = "names.txt"
       self.assertEqual(questions.most_frequent_name(file_path), "Most repeated name: Tawsha")
       return file_path
   def test_emptyinput(self):
       file_path = "No_file_here.txt"
       self.assertRaises(FileNotFoundError, questions.most_frequent_name, file_path)
       return file_path

   def test_None_inputut(self):
       file_path = None
       self.assertRaises(TypeError, questions.most_frequent_name,  None)
       return file_path
#Gil
class TestFilesBackup(unittest.TestCase):
    """
    3 Katas
    """
    def files_backup(dir_path):
        return dir_path

    def test_infolder_directory(self):
        dir_path = "files_to_backup"
        self.assertEqual(questions.files_backup(dir_path), "files_to_backup")
        return dir_path

    def test_out_of_folder_directory(self):
        dir_path = "/Users/gil/katas/DevOpsSep22/python_katas"
        self.assertEqual(questions.files_backup(dir_path), "/Users/gil/katas/DevOpsSep22/python_katas")
        return dir_path

    def test_empty_path(self):
        dir_path = ''
        self.assertRaises(FileNotFoundError, questions.files_backup, dir_path)
        return dir_path

    def test_Capital_Letters(self):
        dir_path = "TRALLALLA"
        self.assertEqual(questions.files_backup(dir_path), "TRALLALLA")
        return dir_path


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


#vitaly
class TestMonotonicArray(unittest.TestCase):
    """
    1 Katas
    """

    def test_empty_monotonic_array(self):
        self.assertEqual(questions.monotonic_array([ ])), True)

    def test_zero_monotonic_array(self):
        self.assertEqual(questions.monotonic_array([0])), True)

    def test_negative_num_monotonic_array(self):
        self.assertEqual(questions.monotonic_array([[-1, -3, -5]])), True)

    def self.test_negative_and_positive_monotonic_array(self):
            self.assertEqual(questions.monotonic_array([[[-10, -5, 11, 1000]]])), True)


#vitaly
class TestMatrixAvg(unittest.TestCase):
    """
    2 Katas
    """
    def test_negativenum_matrix_avg(mat, rows=None):
        self.assertEqual(questions.matrix_avg([[1, 2, 3], [4, -5, 6], [7, 8, 9]]), [3.888888888888889])

    def test_empty_matrix_avg(mat, rows=None):
            self.assertEqual(questions.matrix_avg([[], [], []]), [])

    def test_allzeros_matrix_avg(mat, rows=None):
        self.assertEqual(questions.matrix_avg([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [0])

#Vitaly
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

#Vitaly
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
            self.assertEqual(questions.rotate_matrix(mat), [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]])

            mat = []
            self.assertEqual(questions.rotate_matrix(mat), [])

            mat = [[1, 8, 9], [20, 60, 5], [2, 39, 5], [19, 100, 12]]
            self.assertEqual(questions.rotate_matrix(mat), [[19, 2, 20, 1], [100, 39, 60, 8], [12, 5, 5, 9]])

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

#Arthur
class TestListFlatten(unittest.TestCase):
    """
    2 Katas
    """
    def TestListFlatten(self):
        lst = [1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0], [3]]
        self.assertEqual(questions.list_flatten(lst), [1, 1, 2, 4, 0, 5, 6, 5, 4, 34, 0, 3])

    def EmptyListFlatten(self):
        lst = []
        self.assertEqual(questions.list_flatten(lst), [])


#Arthur
class TestStrCompression(unittest.TestCase):
    """
    2 Katas
    """
    def SampleTextTest(self):
        text = 'aaaaabbcaasbbgvccf'
        self.assertEqual(questions.str_compression(text), ['a', 5, 'b', 2, 'c', 'a', 2, 's', 1, 'b', 2, 'g', 'v', 'c', 2, 'f'])
    def EmptyTextTest(self):
        text = ''
        self.assertEqual(questions.str_compression(text), '')
#Arthur
class TestStrongPass(unittest.TestCase):
    """
    1 Katas
    """
    def NotEnoughChars(self):
        password = 'Ad5&'
        self.assertEqual(questions.strong_pass(password), False)
    def NoDigitsAtAll(self):
        password = 'Ajs!@gr@@#'
        self.assertEqual(questions.strong_pass(password), False)
    def NoLowerCase(self):
        password = 'AJK!@VO9@#'
        self.assertEqual(questions.strong_pass(password), False)
    def NoUpperCase(self):
        password = 'tja!@jq7@#'
        self.assertEqual(questions.strong_pass(password), False)
    def NoSpecialChar(self):
        password = 'ASDrh12647'
        self.assertEqual(questions.strong_pass(password), False)
    def StrongPassFTW(self):
        password = 'A@Drh12$47'
        self.assertEqual(questions.strong_pass(password), True)




if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
