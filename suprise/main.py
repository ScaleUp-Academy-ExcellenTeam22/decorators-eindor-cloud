
#a decorator for any function
#it will make the function prit suprise! instead of its original functionality
def print_surprise(function):
    def inside(*args):
        print("surprise!")
    return inside

