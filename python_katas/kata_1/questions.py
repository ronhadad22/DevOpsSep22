
def sum_of_element(elements):

    s = 0
    for num in elements:
        s = s + num

    return s

def verbing(word):

    length = len(word)

    if length >= 3:
        if word[-3:] == 'ing':
            word = word + 'ly'
        else:
            word = word + 'ing'

    return word


def words_concatenation(words):

    concatenation = ' '
    for i in words:
        concatenation = concatenation + ' '+i
    return concatenation


def reverse_words_concatenation(words):

    words.reverse()
    return " ".join(words)


def is_unique_string(some_str):

    for i in range(len(some_str)):
        for j in range(i + 1, len(some_str)):
            if (some_str[i] == some_str[j]):
                return False;
    return True;


def list_diff(elements):

    new_list = []
    if elements == ' ':
        return elements
    for i in range(0, len(elements), 1):
        if i == 0:
            new_list.append(None)
        else:
            new_list.append(int(elements[i] - elements[i - 1]))
    return new_list


def prime_number(num):


    for i in range(2, num):
        if (num  % i) == 0:
            return False
        return True


def palindrome_num(num):

    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if temp == rev:
        return True
    return False

'''
def pair_match(men, women):
    """
    3 Kata

    This function gets two dictionaries of the type:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age
    The function returns a pair of names (tuple), of from men dict, the other from women dict,
    where their absolute age differences is the minimal

    e.g.
    men = {"John": 20, "Abraham": 45}
    women = {"July": 18, "Kim": 26}

    The returned value should be a tuple ("John", "July") since:

    abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
    abs(John - July) = abs(20 - 18) = abs(2) = 2
    abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
    abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

    :param men: dict mapping name -> age
    :param women: dict mapping name -> age
    :return: tuple (men_name, women_name) such their age absolute difference is the minimal
    """

    return None
'''

def bad_average(a, b, c):

    return (a + b + c) / 3

def best_student(grades):

    return max(zip(grades.values(), grades.keys()))[1]


def print_dict_as_table(some_dict):

    final = ""
    print("{:<10} {:<10}".format('KEY', 'VALUE'))
    for key, value in some_dict.items():
        final += (("{:<10} {:<10}".format(key, value)) + "\n")
    return final

def merge_dicts(dict1, dict2):

    dict1.update(dict2)
    return dict1

def seven_boom(n):

    SevenBoomList = []
    for j in range(1, n+1, 1):
        if j % 7 == 0 or "7" in str(j):
            SevenBoomList.append(j)
    return SevenBoomList

'''
def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    return None
'''

def sum_of_digits(digits_str):

    sum_of_digits= 0
    for i in digits_str:
        sum_of_digits = sum_of_digits + int(i)
    return sum_of_digits


if __name__ == '__main__':

    print('\nsum_of_element:\n--------------------')
    print(sum_of_element([1, 2, 3, 4, 5, 6]))
    
    print('\nverbing:\n--------------------')
    print(verbing('walk'))
    print(verbing('swimming'))
    print(verbing('do'))

    print('\nwords_concatenation:\n--------------------')
    print(words_concatenation(['take', 'me', 'home']))

    print('\nreverse_words_concatenation:\n--------------------')
    print(reverse_words_concatenation(['take', 'me', 'home']))

    print('\nis_unique_string:\n--------------------')
    print(is_unique_string('aasdssdsederd'))
    print(is_unique_string('12345tgbnh'))

    print('\nlist_diff:\n--------------------')
    print(list_diff([1, 2, 3, 8, 77, 0]))

    print('\nprime_number:\n--------------------')
    print(prime_number(5))
    print(prime_number(22))

    print('\npalindrome_num:\n--------------------')
    print(palindrome_num(12221))
    print(palindrome_num(577))

    print('\nbad_average:\n--------------------')
    print(bad_average(1, 2, 3))

    print('\nbest_student:\n--------------------')
    print(best_student({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nprint_dict_as_table:\n--------------------')
    print(print_dict_as_table({
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }))

    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))

    print('\nseven_boom:\n--------------------')
    print(seven_boom(30))

    print('\nsum_of_digits:\n--------------------')
    print(sum_of_digits('1223432'))

'''
    print('\npair_match:\n--------------------')
    print(pair_match(
        {
            "John": 20,
            "Abraham": 45
        },
        {
            "July": 18,
            "Kim": 26
        }
    ))
    
    print('\ncaesar_cipher:\n--------------------')
    print(caesar_cipher('Fly Me To The Moon'))
'''