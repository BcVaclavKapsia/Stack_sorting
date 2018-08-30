import math
from plebs import *
import itertools

critical_7 = 'C://Users//Miroslav//Stack_sorting//critical_7'
critical_8 = 'C://Users//Miroslav//Stack_sorting//critical_8'
critical_8_no_subs = 'C://Users//Miroslav//Stack_sorting//critical_8_no_sub'
new_critical_8 = 'C://Users//Miroslav//Stack_sorting//new_critical_8'


def stack_permutation(permutation, pattern):
    if type(pattern).__name__ == 'str':
        return bracketing_permutation(permutation, pattern)
    list_ret = permutation
    for bracketing in pattern:
        list_ret = bracketing_permutation(list_ret, bracketing)
    return tuple(list_ret)


def check_monotony_relation(tuple1, tuple2):
    for i in tuple1:
        for j in tuple1:
            if tuple1.index(i) < tuple1.index(j):
                if not matching(i, j, tuple2[tuple1.index(i)], tuple2[tuple1.index(j)]):
                    return False
    return True


# TODO: Unfinished
def generate_bracketing_of_permutation(permutation):
    if check_monotony_relation(permutation, (3, 1, 2)):
        return False
    n = len(permutation)
    mutated_list = list(permutation)
    operational_list = []
    v_ret = ''
    while n > 0:
        if not operational_list or operational_list[len(operational_list)-1] != n:
            # print('operational list: ' + str(operational_list))
            # print(v_ret)
            operational_list.append(mutated_list.pop())
            v_ret = ')' + v_ret
            # print(v_ret)
            # print('operational list: ' + str(operational_list))
        if operational_list[len(operational_list)-1] == n:
            # print('operational list: ' + str(operational_list))
            # print(v_ret)
            operational_list.pop()
            v_ret = '(' + v_ret
            n = n - 1
    return v_ret



def odd_basic(permutation):
    l = len(permutation)
    permutation = list(permutation)
    changed = True
    while changed:
        changed = False
        old = list(permutation)
        new = cleanse(permutation, '-')
        if new != old:
            permutation = new
            changed = True
    if len(permutation) == l:
        return False
    return permutation


def even_basic(permutation):
    l = len(permutation)
    permutation = list(permutation)
    changed = True
    while changed:
        changed = False
        old = list(permutation)
        new = cleanse(permutation, '+')
        if new != old:
            permutation = new
            changed = True
    if len(permutation) == l:
        return False
    return permutation


def naive(permutation):
    layout = {'generated_word': '', 'output': '', 'stacks': {}}
    k = math.log2(len(permutation))
    if not int(k) == k:
        k = int(k) + 1
    else:
        k = int(k)
    layout['permutation'] = permutation
    for i in range(k):
        layout['stacks'][str(i+1)] = []

    for i in range(k):
        for j in range(i+1):
            pass
    print_layout(layout, k)


def generate_beginning_layout(permutation, k):
    layout = {'permutation': list(permutation), 'stacks': {}, 'output': [], 'generated_word': '',
                 'capacity_score': 2**k-1}
    for i in range(k):
        layout['stacks'][str(i+1)] = []
    return layout


def fix_values(layout, value):
    if layout['permutation']:
        if value in layout['permutation']:
            layout['permutation'].remove(value)
        l = []
        for i in layout['permutation']:
            if i > value:
                l.append(i-1)
            else:
                l.append(i)
            layout['permutation'] = l

    for stack_number in range(len(layout['stacks'])):
        if layout['stacks'][str(stack_number+1)]:
            if value in layout['stacks'][str(stack_number+1)]:
                layout['stacks'][str(stack_number + 1)].remove(value)
            l = []
            for i in layout['stacks'][str(stack_number+1)]:
                if i > value:
                    l.append(i-1)
                else:
                    l.append(i)
                layout['stacks'][str(stack_number + 1)] = l
    return layout


def other(flag):
    if flag == 'desc':
        return 'asc'
    return 'desc'


def trim_agenda(p_agenda):
    v_ret = []
    for i in p_agenda:
        v_ret.append((i[0], i[1]))
    return v_ret


def generate_agenda(k):
    agenda = []
    for i in range(k, 0, -1):
        agenda.append((i, 'desc'))
    for i in range(k, 1, -1):
        while True:
            if (i, 'desc') in agenda:
                index = agenda.index((i, 'desc'))
                flag = 'asc'
                treasure = []
                for j in range(i-1, 0, -1):
                    treasure.append((j, flag))
                mean = list(agenda)
                agenda = mean[:index] + treasure + mean[index:]
                agenda[agenda.index((i, 'desc'))] = (i, 'desc', 'served')
            elif (i, 'asc') in agenda:
                index = agenda.index((i, 'asc'))
                flag = 'desc'
                treasure = []
                for j in range(i-1, 0, -1):
                    treasure.append((j, flag))
                mean = list(agenda)
                agenda = mean[:index] + treasure + mean[index:]
                agenda[agenda.index((i, 'asc'))] = (i, 'asc', 'served')
            else:
                break
    return trim_agenda(agenda)