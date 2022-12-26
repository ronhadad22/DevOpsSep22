import gzip
import os
import time
import json
import socket
import re
from math import factorial


def valid_parentheses(s):

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


def most_frequent_name(file_path):

    names_dict = {}

    with open('names.txt', 'r') as f:
        file_path = f.read().splitlines()

    # Count the frequency of each name
    for name in file_path:
        if name in names_dict:
            names_dict[name] += 1
        else:
            names_dict[name] = 1

    # Find the name with the maximum count
    most_frequent = None
    max_count = 0
    for name, count in names_dict.items():
        if count > max_count:
            most_frequent = name
            max_count = count

    return most_frequent


def files_backup(dir_path):
    # Get the current date and name in the desired format
    current_time = time.strftime("%Y-%m-%d", time.gmtime())
    dir_name = os.path.basename(dir_path)
    # Create the backup file name
    backup_file = "backup_" + dir_name + "_" + current_time + ".gz"

    # Open the backup file in write mode
    with gzip.open(backup_file, "wb") as f:
        # Iterate through all the files in the directory
        for file in os.listdir(dir_path):
            # Open the file in read mode
            with open(os.path.join(dir_path, file), "rb") as input_file:
                # Write the contents of the file to the backup file
                f.write(input_file.read())
    return backup_file


def replace_in_file(file_path, text, replace_text):

    with open(file_path, "r") as file:
        # read the contents of the file
        contents = file.read()

    contents = contents.replace(text, replace_text)

    with open(file_path, "w") as file:
        # write the replaced contents to the file
        file.write(contents)

    return None


def json_configs_merge(*json_paths):

    merged_config = {}

    for path in json_paths:
        with open(path, 'r') as f:
            config = json.load(f)
    merged_config = {**merged_config, **config}

    return merged_config


def monotonic_array(lst):

    if len(lst) < 2:
        return True
    if lst[0] > lst[1]:
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                return False
    else:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return False
    return True


def matrix_avg(mat, rows=None):

    if rows is None:
        rows = [0, 1, 2]
    total = 0
    count = 0
    for row in rows:
        for element in mat[row]:
            total += element
    count += 1
    return total / count


def merge_sorted_lists(l1, l2):

    result = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    while i < len(l1):
        result.append(l1[i])
        i += 1
    while j < len(l2):
        result.append(l2[j])
        j += 1
    return result


def longest_common_substring(str1, str2):
    # Create a table to store results of sub-problems
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    max_len = 0
    ending_index = 0

    # Fill dp[][] in bottom up manner
    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                if dp[i + 1][j + 1] > max_len:
                    max_len = dp[i + 1][j + 1]
                    ending_index = i

    # return the longest common substring
    return str1[ending_index - max_len + 1:ending_index + 1]

'''
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
    return None
'''

def rotate_matrix(mat):

    n = len(mat)
    m = len(mat[0])
    rotated_matrix = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n - 1 - i] = mat[i][j]
    return rotated_matrix


def is_valid_email(mail_str):

    username, domain = mail_str.split("@")
    if not username[0].isdigit() and not username[0].isalpha():
        return False
    for char in username:
        if not char.isdigit() and not char.isalpha() and char != "." and char != "*":
            return False
    try:
        ip_address = socket.gethostbyname(domain)
    except socket.gaierror:
        return False
    return True


def pascal_triangle(lines):
    for i in range(lines):
        for j in range(lines - i + 1):
            # for left spacing
            print(end=" ")

        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

        # for new line
        print()


def list_flatten(lst):

    if len(lst) == 0:
        return lst
    if isinstance(lst[0], list):
        return list_flatten(lst[0]) + list_flatten(lst[1:])
    return lst[:1] + list_flatten(lst[1:])


def str_compression(text):
    res = ""
    count = 1
    # Add in first character
    res += text[0]

    # Iterate through loop, skipping last one
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            if count > 1:
                # Ignore if no repeats
                res += str(count)
            res += text[i + 1]
            count = 1
    # print last one
    if count > 1:
        res += str(count)
    return list(res)


def strong_pass(password):

    if len(password) <= 6:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*()-+]", password):
        return False
    return True


if __name__ == '__main__':
    print('\nvalid_parentheses:\n--------------------')
    print(valid_parentheses('[[{()}](){}]'))

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
