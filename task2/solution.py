import inspect
import collections
import functools


def groupby(func, seq):
    returned_dict = defaultdict(list)
    for item in seq:
        returned_dict[func(item).append(item)
    return dict(returned_dict)

def iterate(func):
    def composition(function_one, function_two):
        return lambda arg: function_one(function_two(arg))
    
    function = lambda arg: arg
    
    while True:
        yield function
        function = compose(func, function)


def zip_with(func, *iterables):
    for args in zip(*iterables):
        yield func(*args)



def cache(func, cache_size):

    if cache_size <= 0:
        return func

    cache_store = collections.OrderedDict()

    def cached_func(*args):
        if args not in cache_store:
            if len(cache_store) >= cache_size:
                cache_store.popitem(False)

            cache_store[args] = func(*args)

        return cache_store[args]

    return cached_func
