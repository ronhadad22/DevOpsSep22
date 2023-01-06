import pprint
x = 6

#fs


def func():
    print('--------------func locals----------------------')
    x=8
    val="ster"
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(locals())


func()
print('--------------top level locals----------------------')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(locals())


