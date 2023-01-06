x=7
def func():

    def func2():
        global x
        x = 8
    func2()
    print("func() ran in one.py")



print("top-level print inside of one.py")


func()
print(globals())

class yossi:
    pass

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")
    print(f'the __name__ is {__name__}')
