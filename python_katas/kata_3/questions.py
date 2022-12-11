from __future__ import unicode_literals

import itertools
import re
import calendar
from datetime import datetime
from python_katas.kata_2.questions import rotate_matrix
from python_katas.kata_3.utils import open_img, save_img
import requests  # to be used in simple_http_request()
import youtube_dl

ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
import os.path


def knapsack(items, knapsack_limit=50):
    """
    5 Kata

    Consider a thief gets into a home to rob and he carries a knapsack.
    There are fixed number of items in the home — each with its own weight and value —
    Jewelry, with less weight and highest value vs tables, with less value but a lot heavy.
    To add fuel to the fire, the thief has an old knapsack which has limited capacity.
    Obviously, he can’t split the table into half or jewelry into 3/4ths. He either takes it or leaves it

    Given a set of items, dict of tuples representing the (weight, value), determine the items to include in a collection
    so that the total weight is less than or equal to a given limit and the total value is as large as possible.

    :param items: dict of tuples e.g. {"bed": (100, 15), "iphone13": (1, 1500)}
    :param knapsack_limit:
    :return: set of items
    """
    wi = []
    vi = []
    itemsi = []
    for i in items:
        wi.append(items[i][0])
        vi.append(items[i][1])
        itemsi.append(i)
    num = len(items)
    Weight = knapsack_limit

    def my_knapsack(n, v, w, W, ii):
        t = []
        iit = []
        for i in range(n+1):
            row = []
            irow = []
            for j in range(W+1):
                row.append(0)
                irow.append([])
            t.append(row)
            iit.append(irow)
        for j in range(W+1):
            t[0][j] = 0

        for i in range(1, n+1):
            for j in range(W+1):
                if w[i-1] > j:
                    t[i][j] = t[i - 1][j]
                    iit[i][j] = iit[i - 1][j]
                else:
                    t[i][j] = max(t[i - 1][j], t[i - 1][j - w[i-1]] + v[i-1])
                    if t[i][j] == t[i - 1][j]:
                        iit[i][j] = iit[i - 1][j]
                    else:
                        iit[i][j] = []
                        for k in (iit[i - 1][j - w[i-1]]):
                            iit[i][j].append(k)
                        iit[i][j].append(ii[i-1])

        return iit[n][W]

    max_items_list = my_knapsack(num, vi, wi, Weight, itemsi)
    return set(max_items_list)


def time_me(func):
    """
    2 Kata

    Given func - a pointer to sime function which can be executed by func()
    Return the number of time it took to execute the function. Since execution time may vary from time to time,
    execute func 100 time and return the mean

    :param func:
    :return:
    """
    sum_dur = 0
    for i in range(100):
        st = time.time()
        func()
        et = time.time()
        duration = et - st
        sum_dur += duration

    return sum_dur / 100


def youtube_download(video_id):
    """
    3 Kata

    Youtube video url is in the form https://www.youtube.com/watch?v=<video id>
    This function get a youtube video id and downloads this video to the local fs

    hint: https://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php

    :param video_id: str
    :return: None
    """
    # from youtube_dl import YoutubeDL

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        url = f"https://www.youtube.com/watch?v={video_id}"
        ydl.download([url])
    # return None


def tasks_scheduling(tasks):
    """
    5 Kata

    Consider a list of n tasks (tuples), each has starting and ending time (datetime object), as following:
    [(s_1, e_1), (s_2, e_2), ..., (s_n, e_n)]
    where s_* and e_* are Python datetime objects

    Only one task can be performed every time.
    This function returns the index of tasks to perform such the total completed tasks is as large as possible

    :param: tasks: list of tuple (start, end) while start and end are datetime objects
    :return: list of tasks indexes to perform
    """
    task_dict = {}
    tasks_permutation = list(itertools.permutations(tasks, len(tasks)))
    total_solution = []
    count = 0
    for i in tasks:
        task_dict[count] = i
        count += 1

    for tasks_elem in tasks_permutation:
        start = []
        finish = []
        for i in tasks_elem:
            start.append(calendar.timegm(i[0].timetuple()))
            finish.append(calendar.timegm(i[1].timetuple()))
        index = list(range(len(start)))
        max_set = []
        curr_solution = []
        prev_event_time = 0
        for i in index:
            if start[i] >= prev_event_time:
                max_set.append(i)
                prev_event_time = finish[i]
        for i in max_set:
            task_in_cur_solution = tasks_elem[i]
            value = [j for j in task_dict if task_dict[j] == task_in_cur_solution][0]
            curr_solution.append(value)
        total_solution.append(curr_solution)

    max_len_solution = 0
    for i in total_solution:
        if len(i) > max_len_solution:
            max_solution = i
            max_len_solution = len(i)

    return max_solution


def valid_dag(edges):
    """
    5 Kata

    Given a DAG (https://en.wikipedia.org/wiki/Directed_acyclic_graph) in the form:
    [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]

    where a, b, c, d, e are vertices and ('a', 'b') etc... are edges
    This function determine whether the graph is a valid DAG

    :param edges: list of tuples of string 'a', 'b'....
    :return: bool - True if and only if it is a valid DAG
    """

    # A class to represent a graph object
    class Graph:
        # Constructor
        def __init__(self, edges, n):
            # A list of lists to represent an adjacency list
            self.adjList = [[] for _ in range(n)]

            # add edges to the directed graph
            for (src, dest) in edges:
                self.adjList[src].append(dest)

    # Perform DFS on the graph and set the departure time of all vertices of the graph
    def DFS(graph, v, discovered, departure, time):

        # mark the current node as discovered
        discovered[v] = True

        # do for every edge (v, u)
        for u in graph.adjList[v]:
            # if `u` is not yet discovered
            if not discovered[u]:
                time = DFS(graph, u, discovered, departure, time)

        # ready to backtrack
        # set departure time of vertex `v`
        departure[v] = time
        time = time + 1

        return time

    # Returns true if the given directed graph is DAG
    def isDAG(graph, n):

        # keep track of whether a vertex is discovered or not
        discovered = [False] * n

        # keep track of the departure time of a vertex in DFS
        departure = [None] * n

        time = 0

        # Perform DFS traversal from all undiscovered vertices
        # to visit all connected components of a graph
        for i in range(n):
            if not discovered[i]:
                time = DFS(graph, i, discovered, departure, time)

        # check if the given directed graph is DAG or not
        for u in range(n):

            # check if (u, v) forms a back-edge.
            for v in graph.adjList[u]:

                # If the departure time of vertex `v` is greater than equal
                # to the departure time of `u`, they form a back edge.

                # Note that `departure[u]` will be equal to `departure[v]`
                # only if `u = v`, i.e., vertex contain an edge to itself
                if departure[u] <= departure[v]:
                    return False

        # no back edges
        return True

    int_edges = []
    for i in edges:
        t_edge = ()
        for j in i:
            t_edge += ((ord(j) - 97),)
        int_edges.append(t_edge)

    vrtices_dict = {}
    for i in int_edges:
        for j in i:
            vrtices_dict[j] = True

    n = len(vrtices_dict)

    # build a graph from the given edges
    graph = Graph(int_edges, n)

    # check if the given directed graph is DAG or not
    if isDAG(graph, n):
        print('The graph is a DAG')
    else:
        print('The graph is not a DAG')


def rotate_img(img_filename):
    """
    3 Kata

    Rotates image clockwise

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    image = open_img(img_filename)
    file_name = os.path.basename(img_filename)
    rot_image = rotate_matrix(image)
    save_img(rot_image, f"rotated_{file_name}")
    pass  # use rotate_matrix from previous kata 2 or implement....

    # use the below line to save list as image
    # save_img(rotated_img, f'rotated_{img_filename}')


def img_blur(img_filename):
    """
    4 Kata

    Blurs an image (every pixel is an average of its nearest neighbors)

    :param img_filename: image file path (png or jpeg)
    :return: None, the rotated image should be saved as 'rotated_<original image filename>'
    """
    tmp_arr = []
    tmp_row = []
    image = open_img(img_filename)
    file_name = os.path.basename(img_filename)
    rows = len(image)
    col = len(image[1])
    for i in range(rows):
        for j in range(col):
            if i - 1 < 0 and j - 1 < 0:
                tmp_row.append((image[i + 1][j] + image[i][j + 1] + image[i + 1][j + 1]) / 3)
            elif i - 1 < 0 and j + 1 >= col:
                tmp_row.append((image[i][j - 1] + image[i - 1][j - 1] + image[i - 1][j]) / 3)
            elif i + 1 >= rows and j - 1 < 0:
                tmp_row.append((image[i - 1][j] + image[i][j + 1] + image[i - 1][j + 1]) / 3)
            elif i + 1 >= rows and j + 1 >= col:
                tmp_row.append((image[i][j - 1] + image[i - 1][j - 1] + image[i - 1][j]) / 3)
            elif i - 1 < 0:
                tmp_row.append((image[i][j - 1] + image[i + 1][j - 1] + image[i + 1][j] + image[i + 1][j + 1] +
                                image[i][j + 1]) / 5)
            elif i + 1 >= rows:
                tmp_row.append((image[i][j - 1] + image[i - 1][j - 1] + image[i - 1][j] + image[i - 1][j + 1] +
                                image[i][j + 1]) / 5)
            elif j - 1 < 0:
                tmp_row.append((image[i - 1][j] + image[i - 1][j + 1] + image[i][j + 1] + image[i + 1][j + 1] +
                                image[i + 1][j]) / 5)
            elif j + 1 >= col:
                tmp_row.append((image[i - 1][j] + image[i - 1][j - 1] + image[i][j - 1] + image[i + 1][j - 1] +
                                image[i + 1][j]) / 5)
            else:
                tmp_row.append((image[i - 1][j - 1] + image[i - 1][j] + image[i - 1][j + 1] + image[i][j + 1] +
                                image[i + 1][j + 1] + image[i + 1][j] + image[i + 1][j - 1] + image[i][j - 1]) / 8)
        tmp_arr.append(tmp_row)
        tmp_row = []
    save_img(tmp_arr, f"blured_{file_name}")
    pass  # use matrix_avg from previous kata 2 or implement....

    # use the below line to save list as image
    # save_img(blured_img, f'blured_{img_filename}')


def apache_logs_parser(apache_single_log):
    """
    3 Kata

    Parses apache log (see format here https://httpd.apache.org/docs/2.4/logs.html)
    e.g.
    [Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico

    the parsed log data should be:
    date (datetime object), level (str), pid (int), thread_id (int), client_ip (str), log (str)

    Hint: use regex

    :param apache_single_log: str
    :return: parsed log data as tuple
    """
    date_pattern = "^\[(.*?)\].*"
    result = re.search(date_pattern, apache_single_log)
    date = result.group(1)

    level_pattern = "^\[(.*?)\] \[core:(.*?)\].*"
    result = re.search(level_pattern, apache_single_log)
    level = result.group(2)

    pid_pattern = "^\[(.*?)\] \[core:(.*?)\] \[pid (.*):tid .*\].*"
    result = re.search(pid_pattern, apache_single_log)
    pid = result.group(3)

    tid_pattern = "^\[(.*?)\] \[core:(.*?)\] \[pid (.*):tid (.*?)\].*"
    result = re.search(tid_pattern, apache_single_log)
    tid = result.group(4)

    client_ip_pattern = "^\[(.*?)\] \[core:(.*?)\] \[pid (.*):tid (.*?)\] \[client (.*?)\].*"
    result = re.search(client_ip_pattern, apache_single_log)
    client_ip = result.group(5)

    log_pattern = "^\[(.*?)\] \[core:(.*?)\] \[pid (.*):tid (.*?)\] \[client (.*?)\] (.*)"
    result = re.search(log_pattern, apache_single_log)
    log = result.group(6)

    return date, level, pid, tid, client_ip, log


def simple_http_request():
    """
    2 Kata

    This function returns Binance market data JSON by performing a simple HTTP request to '/api/v3/exchangeInfo' endpoint

    Hint: use requests.get(...)
    Hint: Binance api docs https://binance-docs.github.io/apidocs/spot/en/#market-data-endpoints

    :return: json of market exchange information
    """
    r = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    r_dictionary = r.json()
    print(r.json())
    return r.json()


class SortedDict(dict):
    """
    8 Kata

    Implement SortedDict class which is a regular Python dictionary,
    but the keys are maintained in sorted order

    Usage example:
    x = SortedDict()

    x['banana'] = 'ccc'
    x['apple'] = 'aaa'
    x['orange'] = 'bbb'

    list(x.keys())
    >> ['apple', 'banana', 'orange']

    list(x.values())
    >> ['aaa', 'ccc', 'bbb']

    list(x.items())
    >> [('apple', 'aaa'), ('banana', 'ccc'), ('orange', 'bbb')]
    """

    def __init__(self):
        super().__init__()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        l = sorted(self)
        temp_dict = {}
        for key in self:
            temp_dict[key] = self[key]
        self.clear()
        for key in l:
            self.__setattr__(key, temp_dict[key])
            # self[key] = temp_dict[key]
        pass

    def __setattr__(self, key, value):
        super().__setattr__(key, value)

    def items(self):
        return self.__dict__.items()

    def clear(self):
        return self.__dict__.clear()

    def values(self):
        return self.__dict__.values()

    #
    def keys(self):
        return self.__dict__.keys()


class CacheList(list):
    """
    8 Kata

    Implement CacheList class which is a regular Python list,
    but it holds the last n elements only (old elements will be deleted)

    Usage example:
    x = CacheList(3)

    x.append(1)
    x.append(2)
    x.append(3)

    print(x)
    >> [1, 2, 3]

    x.append(1)
    print(x)
    >> [2, 3, 1]

    x.append(1)
    print(x)
    >> [3, 1, 1]
    """

    def __init__(self, cache_size=5):
        super().__init__()
        self.size = cache_size
        self.list = []
        pass

    def __repr__(self):
        return str(self.list)

    def append(self, element):
        if len(self.list) < int(self.size):
            self.list.append(element)
        else:
            self.list.append(element)
            self.list.pop(0)


if __name__ == '__main__':
    import time
    from random import random
    from datetime import datetime

    print('\nknapsack\n--------------------')
    res = knapsack({
        'book': (3, 2),
        'television': (4, 3),
        'table': (6, 1),
        'scooter': (5, 4)
    }, knapsack_limit=8)
    print(res)

    # print('\ntime_me\n--------------------')
    # time_took = time_me(lambda: time.sleep(5 + random()))
    # print(time_took)

    print('\nyoutube_download\n--------------------')
    youtube_download('Urdlvw0SSEc')

    print('\ntasks_scheduling\n--------------------')
    tasks = tasks_scheduling([
        (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:30:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T11:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T16:00:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T14:05:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T12:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T13:30:00Z', ISO_FORMAT)),
        (datetime.strptime('2022-01-01T10:00:00Z', ISO_FORMAT), datetime.strptime('2022-01-01T10:10:00Z', ISO_FORMAT))
    ])
    print(tasks)

    print('\nvalid_dag\n--------------------')

    # valid
    print(valid_dag([('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e')]))

    # invalid
    print(valid_dag([('a', 'b'), ('c', 'a'), ('d', 'a'), ('a', 'e'), ('b', 'd'), ('c', 'd'), ('c', 'e'), ('d', 'f')]))

    print('\nrotate_img\n--------------------')
    rotate_img('67203.jpeg')

    print('\nimg_blur\n--------------------')
    img_blur('67203.jpeg')

    print('\napache_logs_parser\n--------------------')
    date, level, pid, tid, client_ip, log = apache_logs_parser(
        '[Fri Sep 09 10:42:29.902022 2011] [core:error] [pid 35708:tid 4328636416] [client 72.15.99.187] File does not exist: /usr/local/apache2/htdocs/favicon.ico')
    print(date, level, pid, tid, client_ip, log)

    print('\nsimple_http_request\n--------------------')
    info = simple_http_request()

    print('\nSortedDict\n--------------------')
    s_dict = SortedDict()
    s_dict['a'] = None
    s_dict['t'] = None
    s_dict['h'] = None
    s_dict['q'] = None
    s_dict['b'] = None
    print(s_dict.items())

    print('\nCacheList\n--------------------')
    c_list = CacheList(5)
    c_list.append(1)
    c_list.append(2)
    c_list.append(3)
    c_list.append(4)
    c_list.append(5)
    c_list.append(6)
    print(c_list)
    c_list.append(7)
    print(c_list)
    c_list.append(8)
    print(c_list)
