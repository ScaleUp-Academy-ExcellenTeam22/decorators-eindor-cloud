
#a function decorator that get a function
#decorate that function to run twice
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