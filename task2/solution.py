import inspect
import collections
import functools


def groupby(func, seq):
    returned_dict = {}
    for item in seq:
        key_to_test = func(item)
        if key_to_test in returned_dict:
            returned_dict[key_to_test].append(item)
        else:
            returned_dict[key_to_test] = [item]
    return returned_dict


def iterate(fn):
    def repeater(arg, _count=1):
        for i in range(_count):
            arg = fn(arg)
        return arg
    count = 0
    while True:
        yield functools.partial(repeater, _count=count)
        count += 1


def zip_with(func, *iterables):
    if len(iterables) == 0:
        def generator():
            yield None
    else:
        variable_length = len(iterables)
        shortest_variable_length = len(iterables[0])
        for item in iterables:
            if shortest_variable_length > len(item):
                shortest_variable_length = len(item)

        def generator(variable_length, iterables, shortest_variable_length):

            argument_list = []
            second_position = 0
            for first_position in range(0, variable_length):
                argument_list.append(
                    iterables[first_position][second_position])
            while second_position < shortest_variable_length:
                yield func(*argument_list)
                second_position += 1
                argument_list = []
                for first_position in range(0, variable_length):
                    argument_list.append(
                        iterables[first_position][second_position])
        generate_it = generator(
            variable_length,
            iterables,
            shortest_variable_length)
        return_list = []
        for items in range(0, shortest_variable_length):
            return_list.append(next(generate_it))
    return return_list


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
