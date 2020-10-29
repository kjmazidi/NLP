# Program to practice list processing

from random import randrange, seed
import timeit


def load_lists(len1, len2):
    seed(1234)
    list1 = [randrange(10000) for _ in range(len1)]
    list2 = [randrange(10000) for _ in range(len2)]
    return list1, list2


def find_common(list1, list2):
    new_list = []
    for num in list1:
        if num in list2 and num not in new_list:
            new_list.append(num)
    return new_list


def find_common_LC(list1, list2):
    # don't do this
    new_list = []
    [new_list.append(_) for _ in list1 if _ in list2 and _ not in new_list]
    return new_list


def find_unique(list1, list2):
    new_list = []
    for num in list1:
        if num not in list2 and num not in new_list:
            new_list.append(num)
    for num in list2:
        if num not in list1 and num not in new_list:
            new_list.append(num)
    return new_list


def find_unique_LC(list1, list2):
    # don't do this either
    new_list = []
    [new_list.append(_) for _ in list1 if _ not in list2 and _ not in new_list]
    [new_list.append(_) for _ in list2 if _ not in list1 and _ not in new_list]
    return new_list


if __name__ == '__main__':
    # generate two lists
    list1, list2 = load_lists(9000, 7500)

    print('\n---------- RESULTS -----------------')

    # find common elements
    start_time = timeit.default_timer()
    common = find_common(list1, list2)
    end_time = timeit.default_timer()
    print(len(common), 'numbers are common to both lists, including:',
          common[:5])
    print('Function time:', end_time - start_time, '\n')

    # find common elements with list comprehension
    start_time = timeit.default_timer()
    common = find_common_LC(list1, list2)
    end_time = timeit.default_timer()
    print(len(common), 'numbers are common to both lists, including:',
          common[:5])
    print('Function time using list comprehension:', end_time - start_time, '\n')

    start_time = timeit.default_timer()
    unique = find_unique(list1, list2)
    end_time = timeit.default_timer()
    print(len(unique), 'numbers are unique to one list only, including:',
          unique[:5])
    print('Function time:', end_time - start_time, '\n')

    start_time = timeit.default_timer()
    unique = find_unique_LC(list1, list2)
    end_time = timeit.default_timer()
    print(len(unique), 'numbers are unique to one list only, including:',
          unique[:10])
    print('Function time using list comprehension:', end_time - start_time, '\n')

    # now try set operations
    start_time = timeit.default_timer()
    common = set(list1).intersection(set(list2))
    end_time = timeit.default_timer()
    print(len(common), 'numbers are common to both lists')
    print('Set time:', end_time - start_time, '\n')

    start_time = timeit.default_timer()
    unique = set(list1).symmetric_difference(set(list2))
    end_time = timeit.default_timer()
    print(len(unique), 'numbers are unique to one list only')
    print('Set time:', end_time - start_time, '\n')
