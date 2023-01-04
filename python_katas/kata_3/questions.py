from python_katas.kata_3.utils import open_img, save_img
import requests   # to be used in simple_http_request()
from python_katas.kata_2 import questions
ISO_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

import cv2

def time_me(func):

    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time


def youtube_download(video_id):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_id])


def tasks_scheduling(tasks):

    tasks.sort(key=lambda x: x[1])  # sort tasks by ending time
    result = []
    current_time = tasks[0][0]  # start with the earliest starting time
    for i in range(len(tasks)):
        if current_time <= tasks[i][0]:  # if current time is before or at the start of the task
            result.append(i)  # add task to result
    current_time = tasks[i][1]  # update current time to end time of task
    return result


if __name__ == '__main__':
    import time
    import youtube_dl
    from random import random
    from datetime import datetime

    print('\ntime_me\n--------------------')
    time_took = time_me(lambda: time.sleep(5 + random()))
    print(time_took)

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
