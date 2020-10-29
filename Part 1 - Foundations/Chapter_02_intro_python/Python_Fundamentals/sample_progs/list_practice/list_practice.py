# Program to practice list processing

from random import randrange, seed
import timeit


def load_lists(length1, length2):
    seed(1234)
    new_list1 = [randrange(100) for _ in range(length1)]
    new_list2 = [randrange(100) for _ in range(length2)]
    return new_list1, new_list2


def process_list_loop(in_list1, in_list2):
    return_list = []
    for i in range(len(in_list1)):
        result = 0
        for j in range(len(in_list2)):
            if in_list1[i] == in_list2[j]:
                result = 1
                #break  # uncomment for a more efficient version
        return_list.append(result)

    return return_list


def process_list_loop_better(in_list1, in_list2):
    return_list = []
    for i in range(len(in_list1)):
        return_list.append(in_list1[i] in in_list2)

    return return_list


def process_list_loop_lc(in_list1, in_list2):
    return [_ in in_list2 for _ in in_list1]


if __name__ == '__main__':
    # generate a list
    list1, list2 = load_lists(1000, 5000)

    print('\n---------- RESULTS -----------------')

    # process the list
    start_time = timeit.default_timer()
    new_list = process_list_loop(list1, list2)
    end_time = timeit.default_timer()
    print('Function time:', end_time - start_time, '\n')
    #print(sum(new_list))

    # process the list a better way
    start_time = timeit.default_timer()
    new_list = process_list_loop_better(list1, list2)
    end_time = timeit.default_timer()
    print('Function time second algorithm:', end_time - start_time, '\n')
    #print(sum(new_list))

    # process the list in list comprehension
    start_time = timeit.default_timer()
    new_list = process_list_loop_lc(list1, list2)
    end_time = timeit.default_timer()
    print('Function time list comprehension', end_time - start_time, '\n')
    #print(sum(new_list))






