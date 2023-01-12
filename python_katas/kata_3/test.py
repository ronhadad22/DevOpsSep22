import unittest
from datetime import datetime

from python_katas.kata_3 import questions
from python_katas.kata_3.questions import ISO_FORMAT, tasks_scheduling
from python_katas.utils import unittest_runner


class TestKnapsack(unittest.TestCase):
    """
    5 Kata
    """
    def test_sample(self):
        # your code here
        pass


class TestTimeMe(unittest.TestCase):
    """
    2 Kata
    """
    def test_sample(self):
        # your code here
        pass

################## AYAM ##########################


class TestYoutubeDownload(unittest.TestCase):
    """
    3 Kata
    """
    def test_empty_Url(self):
        video_id = ' '
        self.assertEqual(questions.youtube_download(video_id), " There is no video id in this URL")

    def testWrongId(self):
        video_id = 'AA0'
        self.assertEqual(questions.youtube_download(video_id), " It's Unacceptable id, Can't download")


class TestTasksScheduling(unittest.TestCase):
    """
    5 Kata
    """
    def test_empty_list(self):
        tasks = []
        self.assertEqual(questions.tasks_scheduling(tasks), 0)

    def testThereIsNoStartingTime(self):
        tasks = tasks_scheduling([
         (datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT)),
         (datetime.strptime('2022-01-01T14:30:00Z', ISO_FORMAT)),
         (datetime.strptime('2022-01-01T16:00:00Z', ISO_FORMAT)),
         (datetime.strptime('2022-01-01T14:05:00Z', ISO_FORMAT)),
        ])

        self.assertEqual(questions.tasks_scheduling(tasks), False)

    def testThereIsNoEndingTime(self):
        tasks = tasks_scheduling([
            (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT)),
            (datetime.strptime('2022-01-01T13:00:00Z', ISO_FORMAT)),
            (datetime.strptime('2022-01-01T11:00:00Z', ISO_FORMAT)),
            (datetime.strptime('2022-01-01T14:00:00Z', ISO_FORMAT)),
            (datetime.strptime('2022-01-01T12:00:00Z', ISO_FORMAT)),
            (datetime.strptime('2022-01-01T10:00:00Z', ISO_FORMAT))
        ])

        self.assertEqual(questions.tasks_scheduling(tasks), False)


##################AYAM##########################


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
