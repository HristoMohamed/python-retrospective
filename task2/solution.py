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
    cache.cache_dict = collections.OrderedDict()
    cache.cache_size = cache_size
    cache.current_size = 0

    def func_cached(value):
        if cache.current_size == 0 and cache.cache_size == 0:
            return func(value)
        if cache.current_size == 0 and cache.cache_size > 0:
                cache.cache_dict[value] = func(value)
                cache.current_size += 1
                return cache.cache_dict[value]
        flag = False
        for key in cache.cache_dict:
            if key == value:
                flag = True
                break
        if flag:
            return cache.cache_dict[value]
        else:
            if cache.cache_size <= cache.current_size:
                trash = cache.cache_dict.popitem(last=False)
                cache.cache_dict[value] = func(value)
                trash = cache.cache_dict.move_to_end(value, last=True)
                cache.current_size += 1
                return cache.cache_dict[value]
            else:
                cache.cache_dict[value] = func(value)
                cache.current_size += 1
                return cache.cache_dict[value]
    return func_cached
