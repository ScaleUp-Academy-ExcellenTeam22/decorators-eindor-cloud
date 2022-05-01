
def twice(func):
    def inside(*args):
        func(*args)
        func(*args)
        return
    return inside

def func(mila):
    print(mila)

func = twice(func)

func("mm")