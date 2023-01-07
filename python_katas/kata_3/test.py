import unittest
from python_katas.kata_3 import questions
from python_katas.utils import unittest_runner


class TestKnapsack(unittest.TestCase):
    """
    5 Kata
    """
    def test_sample(self):
        items = {
        'bed': (43, 10),
        'iphone': (5, 200),
        'ring': (2, 150),
        'chair': (20, 5),
        'table': (32, 8),
        'tv': (22, 200),
        'ring2': (2, 300),
        'pc': (20, 530)
        }
        self.assertEqual(questions.knapsack(items, knapsack_limit=50))

        def test_empty_house(self):
            items = {}
            self.assertEqual(questions.knapsack(items, knapsack_limit=50))

            def test_overload(self):
                items = {
                    'bed': (52, 10),
                    'iphone': (51, 200),
                    'ring': (52, 150),
                    }
                self.assertEqual(questions.knapsack(items, knapsack_limit=50))

        def test_hole_items(self):
            items = {
                'bed': (1, 10),
                'iphone': (5, 200),
                'ring': (2, 150),
                'chair': (1, 5),
                'table': (1, 8),
                }
            self.assertEqual(questions.knapsack(items, knapsack_limit=50))



        pass


class TestTimeMe(unittest.TestCase):
    """
    2 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestYoutubeDownload(unittest.TestCase):
    """
    3 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestTasksScheduling(unittest.TestCase):
    """
    5 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestValidDag(unittest.TestCase):
    """
    5 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestRotateImg(unittest.TestCase):
    """
    3 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestImgBlur(unittest.TestCase):
    """
    4 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestApacheLogsParser(unittest.TestCase):
    """
    3 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestSimpleHttpRequest(unittest.TestCase):
    """
    2 Kata
    """
    def test_sample(self):
        # your code here
        pass


if __name__ == '__main__':
    import inspect
    import sys
    unittest_runner(inspect.getmembers(sys.modules[__name__], inspect.isclass))
