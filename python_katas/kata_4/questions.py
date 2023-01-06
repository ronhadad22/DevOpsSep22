def sudoku_solver():
    pass


class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        print(f"class attribute is {Singleton._instance}")
        if Singleton._instance is not None:
            print("instance exist your welcome")
            return Singleton._instance

        print("instance not exist creating...")
        return Singleton()

    def __init__(self):
        if Singleton._instance is not None: #instance exist
            raise RuntimeError('class singleton instance already exist')
        else:   #instance not exist run only once
            Singleton._instance = self




my_singleton2 = Singleton.getInstance()

print(my_singleton2)

my_singleton3 = Singleton.getInstance()

print(my_singleton3)
#
# print(my_singleton3)


def binary_search():
    pass


def psutils():
    pass  # https://github.com/giampaolo/psutil


def mailer():
    pass  # https://github.com/kootenpv/yagmail


def run_config_env_var():
    pass


def logger():
    pass


def geo():
    pass


def pyjwt_demo():
    pass


def pyaudio():
    pass

def pyaudio():
    pass



