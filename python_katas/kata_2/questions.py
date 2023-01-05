
  import json
  import os
  import pathlib
  import re
  import socket
  from _socket import gaierror
  from datetime import datetime

def valid_parentheses(s):
    """
    3 Kata

    This function gets a string containing just the characters '(', ')', '{', '}', '[' and ']',
    and determines if the input string is valid.

    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    e.g.
    s = '[[{()}](){}]'  -> True
    s = ']}'          -> False
    """
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif not stack:  # closing char
            top = stack.pop(-1)
            if top == '(' and char != ')':
                return False
            if top == '[' and char != ']':
                return False
            if top == '{' and char != '}':
                return False
        else:
            return False
    return True

    # David's solution
    while True:
        if '()' in s:
            s = s.replace('()', '')
        elif '{}' in s:
            s = s.replace('{}', '')
        elif '[]' in s:
            s = s.replace('[]', '')
        else:
            return not s


def fibonacci_fixme(n):
    """
    2 Kata

    A Fibonacci sequence is the integer sequence of 1, 1, 2, 3, 5, 8, 13....
    The first two terms are 1 and 1. All other terms are obtained by adding the preceding two terms.

    This function should return the n'th element of fibonacci sequence. As following:

    fibonacci_fixme(1) -> 1
    fibonacci_fixme(2) -> 1
    fibonacci_fixme(3) -> 2
    fibonacci_fixme(4) -> 3
    fibonacci_fixme(5) -> 5

    But it doesn't (it has some bad lines in it...)
    You should (1) correct the for statement and (2) swap two lines, so that the correct fibonacci element will be returned
    """
    a = 0
    b = 1
    for i in range(1, n):
        a = b
        tmp = a + b
        b = tmp

    return a


def most_frequent_name(file_path):
    """
    2 Kata

    This function gets a path to a file containing names (name in each line)
    The function should return the most frequent name in the file

    You can assume file_path exists in the file system

    :param file_path: str - absolute or relative file to read names from
    :return: str - the mose frequent name. If there are many, return one of them
    """

    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    names = {}
    max_count = 0
    name_of_max = ""
    for line in Lines:
        # count += 1
        # print("Line{}: {}".format(count, line.strip()))
        if line in names:
            names[line] += 1
        else:
            names[line] = 1
    for key, val in names.items():
        if val > max_count:
            max_count = val
            name_of_max = key
    print(f"most frequent name: {name_of_max}")
    return max_count


def files_backup(dir_path):
    """
    3 Kata

    This function gets a path to a directory and generated a .gz file containing all the files the directory contains
    The backup .gz file name should be in the form:

    'backup_<dir_name>_<yyyy-mm-dd>.tar.gz'

    Where <dir_name> is the directory name (only the directory, not the full path given in dir_path)
    and <yyyy-mm-dd> is the date e.g. 2022-04-10

    You can assume dir_path exists in the file system

    :param dir_path: string - path to a directory
    :return: str - the backup file name
    """

    now = datetime.now()
    year = now.strftime("%Y")
    print("year:", year)

    month = now.strftime("%m")
    print("month:", month)

    day = now.strftime("%d")
    print("day:", day)

    path = pathlib.PurePath(dir_path)
    cmd = f"cd {dir_path} ; tar -czvf backup_{path.name}_{year}-{month}-{day}.tar.gz *"
    os.system(cmd)
    return cmd


def replace_in_file(file_path, text, replace_text):
    """
    2 Kata

    This function gets a path of text file, it replaces all occurrences of 'text' by 'replace_text'.
    The function saves the replaces content on the same path (overwrites the file's content)

    You MUST check that file_path exists in the file system before you try to open it

    :param file_path: relative or absolute path to a text file
    :param text: text to search
    :param replace_text: text to replace with
    :return: None
    """

    path = pathlib.Path(file_path)
    if not path.is_file():
        print("file not found")
        return
    else:
        fin = open(file_path, "rt")
        data = fin.read()
        data = data.replace(text, replace_text)
        fin.close()
        fin = open(file_path, "wt")
        fin.write(data)
        fin.close()
    return None


def json_configs_merge(*json_paths):
    """
    2 Kata

    This function gets an unknown number of paths to json files (represented as tuple in json_paths argument)
    it reads the files content as a dictionary, and merges all of them into a single dictionary,
    in the same order the files have been sent to the function!

    :param json_paths:
    :return: dict - the merges json files
    """

    combine_json = {}
    for my_json_file in json_paths:
        with open(my_json_file) as json_file:
            data = json.load(json_file)
            for k, v in data.items():  # use d.iteritems() in python 2
                combine_json[k] = v
    return combine_json


def monotonic_array(lst):
    """
    1 Kata

    This function returns True/False if the given list is monotonically increased or decreased

    :param lst: list of numbers (int, floats)
    :return: bool: indicating for monotonicity
    """

    if all(x >= y for x, y in zip(lst, lst[1:])):
        non_inc = True
    else:
        non_inc = False
    if all(x <= y for x, y in zip(lst, lst[1:])):
        non_dec = True
    else:
        non_dec = False
    return non_inc or non_dec


def matrix_avg(mat, rows=None):
    """
    2 Kata

    This function gets a 3*3 matrix (list of 3 lists) and returns the average of all elements
    The 'rows' optional argument (with None as default) indicating which rows should be included in the average calculation

    :param mat: 3*3 matrix
    :param rows: list of unique integers in the range [0, 2] and length of maximum 3
    :return: int - the average values
    """

    if rows == None:
        num_of_elem = 9;
        rows = [0, 1, 2]
    else:
        num_of_elem = len(rows) * 3
    sum = 0
    for raw in rows:
        for col in range(3):
            sum += mat[raw][col]
    return sum / num_of_elem


def merge_sorted_lists(l1, l2):
    """
    1 Kata

    This function gets two sorted lists (each one of them is sorted)
    and returns a single sorted list combining both of them.

    Try to be as efficient as you can (hint - don't use Python's built in sort() or sorted() functions)

    :param l1: list of integers
    :param l2: list of integers
    :return: list: sorted list combining l1 and l2
    """

    c = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            c.append(l1[0])
            l1.pop(0)
        else:
            c.append(l2[0])
            l2.pop(0)
    while l1:
        c.append(l1[0])
        l1.pop(0)
    while l2:
        c.append(l2[0])
        l2.pop(0)
    return c


def longest_common_substring(str1, str2):
    """
    4 Kata

    This functions gets two strings and returns their longest common substring

    e.g. for
    str1 = 'Introduced in 1991, The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'
    since it's the longest string contained both in str1 and str2

    :param str1: str
    :param str2: str
    :return: str - the longest common substring
    """

    longestString = ""
    maxLength = 0
    for i in range(0, len(str1)):
        if str1[i] in str2:
            for j in range(i + 1, len(str1)):
                if str1[i:j] in str2:
                    if (len(str1[i:j]) > maxLength):
                        maxLength = len(str1[i:j])
                        longestString = str1[i:j]
    return longestString


def longest_common_prefix(str1, str2):
    """
    1 Kata

    This functions gets two strings and returns their longest common prefix

    e.g. for
    str1 = 'The Linux kernel is an amazing software'
    str2 = 'The Linux kernel is a mostly free and open-source, monolithic, modular, multitasking, Unix-like operating system kernel.'

    The returned value would be 'The Linux kernel is a'

    :param str1: str
    :param str2: str
    :return: str - the longest common prefix
    """

    len1, len2 = len(str1), len(str2)

    if len1 > len2:
        str1, str2 = str2, str1
        len1, len2 = len2, len1
    longest_prefix = ""
    for i in range(len1):
        if str1[i] == str2[i]:
            longest_prefix += str1[i]
        else:
            return longest_prefix


def rotate_matrix(mat):
    """
    2 Kata

    This function gets a matrix n*m (list of m lists of length n) and rotate the matrix clockwise
    e.g.
    for [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]] which represent the matrix

    1   2   3
    4   5   6
    7   8   9
    10  11  12

    The output should be:
    [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]

    10  7   4   1
    11  8   5   2
    12  9   6   3

    :param mat:
    :return: list of lists - rotate matrix
    """

    rotate_mat = []
    rot_raw = []
    num_rows = len(mat)
    num_col = len(mat[1])
    for i in range(num_col):
        for j in range(num_rows):
            rot_raw.append(mat[j][i])
        rot_raw.reverse()
        rotate_mat.append(rot_raw)
        rot_raw = []
    return rotate_mat


def is_valid_email(mail_str):
    """
    3 Kata

    This function returns True if the given mail is in the form:
    (username)@(domainname)

    Where
    * (username) must start with digit or an English character, and can contains only 0-9 a-z A-Z . or _
    * (domainname) is a real, existed domain - one that resolves to an actual ip address

    Hint: use socket.gethostbyname() to resolve a DNS in Python code

    :param mail_str: mail to check
    :return: bool: True if it's a valid mail (otherwise either False is returned or the program can crash)
    """

    result = re.search("(^[a-zA-Z0-9]+[a-zA-Z_0-9.]*)@([a-zA-Z]+.{1}[a-z]+)", mail_str)
    if result == None:
        return False
    username = result.group(1)
    domainname = result.group(2)
    try:
        ipAddress = socket.gethostbyname(domainname)
        print(f"domain IP: {ipAddress}")
        return True
    except gaierror:
        return False


def pascal_triangle(lines):
    """
    3 Kata

    This function gets an integer representing the number of lines to print in a Pascal Triangle
    e.g. For n = 10 then following would be printed

                 1
                1 1
               1 2 1
              1 3 3 1
             1 4 6 4 1
           1 5 10 10 5 1
         1 6 15 20 15 6 1
        1 7 21 35 35 21 7 1
      1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    You are allowed to print the numbers not in a triangle shape:
    1
    1 1
    1 2 1
    1 3 3 1
    1 4 6 4 1
    1 5 10 10 5 1
    1 6 15 20 15 6 1
    1 7 21 35 35 21 7 1
    1 8 28 56 70 56 28 8 1
    1 9 36 84 126 126 84 36 9 1

    :param lines: int
    :return: None
    """

    line1 = [1]
    line2 = [1, 1]
    if lines == 1:
        print(*line1)
        return
    elif lines == 2:
        print(*line1)
        print(*line2)
        return
    print(*line1)
    print(*line2)
    prev_line = line2
    cur_line = []
    for i in range(2, lines, 1):
        for j in range(len(prev_line) + 1):
            if j == 0:
                cur_line.append(1)
            elif j == len(prev_line):
                cur_line.append(1)
            else:
                cur_line.append(prev_line[j - 1] + prev_line[j])
        prev_line = cur_line
        print(*cur_line)
        cur_line = []


def list_flatten(lst):
    """
    2 Kata

    This function gets a list of combination of integers or nested lists
    e.g.
    [1, [], [1, 2, [4, 0, [5], 6], [5, 4], 34, 0], [3]]

    The functions should return a flatten list (including all nested lists):
    [1, 1, 2, 4, 0, 5, 6, 5, 4, 34, 0, 3]

    :param lst: list of integers of another list
    :return: flatten list
    """

    ret_list = []
    str_lst = str(lst)
    tmp_str = ""
    for i in str_lst:
        if i != ' ' and i != '[' and i != ']' and i != ',':
            tmp_str += i
        else:
            if tmp_str != "":
                ret_list.append(int(tmp_str))
                tmp_str = ""
    return ret_list


def str_compression(text):
    """
    2 Kata

    This function gets a text (string) and returns a list representing the compressed form of the text.
    e.g.
    text = 'aaaaabbcaasbbgvccf'

    The output will be:
    ['a', 5, 'b', 2, 'c', 'a', 2, 's', 1, 'b', 2, 'g', 'v', 'c', 2, 'f']

    Since 'a' appears 5 times in consecutively, 'b' 2 times etc...
    Note that sequences of length 1 don't necessarily have the number 1 after the character (like 'c' before 'a')

    :param text: str
    :return: list representing the compressed form of the string
    """

    ret_list = []
    if text == "":
        return ret_list
    count = 0
    prev_char = ""
    for i in text:
        if i == prev_char and count != 0:
            count += 1
            prev_char = i
        elif count == 0:
            count = 1
            prev_char = i
        elif i != prev_char:
            ret_list.append(prev_char)
            if count != 1:
                ret_list.append(count)
            count = 1
            prev_char = i
    ret_list.append(prev_char)
    if count != 1:
        ret_list.append(count)
    return ret_list


def strong_pass(password):
    """
    1 Kata

    A password is considered strong if it satisfies the following criteria:
    1) Its length is at least 6.
    2) It contains at least one digit.
    3) It contains at least one lowercase English character.
    4) It contains at least one uppercase English character.
    5) It contains at least one special character. The special characters are: !@#$%^&*()-+

    This function returns True if the given password is strong enough
    """

    if len(password) < 6:
        return False
    result = re.search("[0-9]+", password)
    if result == None:
        return False
    result = re.search("[a-z]+", password)
    if result == None:
        return False
    result = re.search("[A-Z]+", password)
    if result == None:
        return False
    result = re.search("[!@#$%^&*()-+]+", password)
    if result == None:
        return False
    return True


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))

    print('\nfibonacci_fixme:\n--------------------')
    print(fibonacci_fixme(6))

    print('\nmost_frequent_name:\n--------------------')
    print(most_frequent_name('names.txt'))

    print('\nfiles_backup:\n--------------------')
    print(files_backup('files_to_backup'))

    print('\nreplace_in_file:\n--------------------')
    print(replace_in_file('mnist-predictor.yaml', '{{IMG_NAME}}', 'mnist-pred:0.0.1'))

    print('\njson_configs_merge:\n--------------------')
    print(json_configs_merge('default.json', 'local.json'))

    print('\nmonotonic_array:\n--------------------')
    print(monotonic_array([1, 2, 3, 6, 8, 9, 0]))

    print('\nmatrix_avg:\n--------------------')
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=[0, 2]))
    print(matrix_avg([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    print('\nmerge_sorted_lists:\n--------------------')
    print(merge_sorted_lists([1, 4, 9, 77, 13343], [-7, 0, 7, 23]))

    print('\nlongest_common_substring:\n--------------------')
    print(longest_common_substring('abcdefg', 'bgtcdesd'))

    print('\nlongest_common_prefix:\n--------------------')
    print(longest_common_prefix('abcd', 'ttty'))

    print('\nrotate_matrix:\n--------------------')
    print(rotate_matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))

    print('\nis_valid_email:\n--------------------')
    print(is_valid_email('israel.israeli@gmail.com'))

    print('\npascal_triangle:\n--------------------')
    print(pascal_triangle(4))

    print('\nlist_flatten:\n--------------------')
    print(list_flatten([1, 2, [3, 4, [4, 5], 7], 8]))

    print('\nstr_compression:\n--------------------')
    print(str_compression('aaaabdddddhgf'))

    print('\nstrong_pass:\n--------------------')
    print(strong_pass('##$FgC7^^5a'))
