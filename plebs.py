def parity(_object):
    if _object % 2 == 0:
        return 'even'


def catalan(n):
    b = 0
    if n in (0, 1):
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 5
    if n == 4:
        return 14
    if n == 5:
        return 42
    else:
        for i in range(n):
            b += (catalan(i))*(catalan(n-1-i))
    return b


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def sum(lll):
    x = 0
    for i in lll:
        x = x + i
    return x


def sort(_object, way):
    _object = list(_object)
    v_ret = []
    if way == 'inc':
        while _object:
            mini = min(_object)
            v_ret.append(mini)
            _object.remove(mini)
    else:
        while _object:
            maxi = max(_object)
            v_ret.append(maxi)
            _object.remove(maxi)
    return v_ret


def matching(a, b, c, d):
    if (a < b and c < d) or (a > b and c > d):
        return True
    return False


def to_string(iter, spaces=True):
    word = ''
    if spaces:
        for i in range(len(iter)):
            word = word + ' ' + str(iter[i])
        return word[1:]
    else:
        for i in range(len(iter)):
            word = word + str(iter[i])
        return word


def bracketing_permutation(permutation, bracketing):
    active_permutation = list(permutation)
    active_stack = []
    v_return = []
    for symbol in bracketing:
        if symbol == '(':
            active_stack.insert(0, active_permutation.pop(0))
        if symbol == ')':
            v_return.append(active_stack.pop(0))
    return tuple(v_return)


def trimmed_permutation(permutation, sub_permutation):
    sub_min_location = sub_permutation.index(min(sub_permutation))
    sub_max_location = sub_permutation.index(max(sub_permutation))
    popped = True
    perm_min_location = permutation.index(min(sub_permutation))
    perm_max_location = permutation.index(max(sub_permutation))
    # print(sub_permutation)  # erase
    # print(permutation)  # erase
    while popped and len(permutation) >= len(sub_permutation):
        popped = False
        if perm_min_location < sub_min_location or len(permutation) - perm_min_location < len(sub_permutation) - sub_min_location:
            permutation.pop(perm_min_location)
            # print(permutation, ' min taken out')  # erase
            perm_min_location = permutation.index(min(permutation))
            perm_max_location = permutation.index(max(permutation))
            popped = True
        if perm_max_location < sub_max_location or len(permutation) - perm_max_location < len(sub_permutation) - sub_max_location:
            permutation.pop(perm_max_location)
            # print(permutation, ' max taken out')  # erase
            perm_min_location = permutation.index(min(permutation))
            perm_max_location = permutation.index(max(permutation))
            popped = True
    if len(permutation) < len(sub_permutation):
        return tuple([])
    return tuple(permutation)


def increasing(li):
    for i in range(0, len(li) - 1):
        if li[i] > li[i+1]:
            return False
    return True


def decreasing(li):
    for i in range(0, len(li) - 1):
        if li[i] < li[i+1]:
            return False
    return True


def apply_permutation(original, tool):
    v_ret = []
    for i in tool:
        v_ret.append(original[i-1])
    return tuple(v_ret)


def valid_bracketing(_object):
    x = 0
    for char in _object:
        if char == '(':
            x = x + 1
        elif char == ')':
            x = x - 1
        else:
            return False
        if x != 0:
            return False
    if x == 0:
        return True
    return False


def valid_word(_object):
    l = []
    for i in _object:
        l.append(int(i))
    k = max(l)
    for i in range(0, max(l)):
        if i not in l:
            return False
    zero_count = l.count(0)
    for i in range(max(l)+1):
        if l.count(i) != zero_count:
            return False
    length = len(l)
    for i in range(int(length/(k+1))):
        for j in range(k):
            if l.index(j) > l.index(j+1):
                return False
        for j in range(k+1):
            l.pop(l.index(j))
    if not l:
        return True
    else:
        return False


def valid_pattern(_object):
    l = len(_object[0])
    for i in _object:
        if len(i) != l or not valid_bracketing(i):
            return False
    return True


def valid_permutation(_object):
    if type(_object).__name__ in ('list', 'tuple') and type(_object[0]).__name__ == 'int':  # this is for permutation
        for i in range(1, len(_object)+1):
            if i not in _object:
                return False
        return True
    return False


def valid(_object):
    if type(_object).__name__ in ('list', 'tuple') and type(_object[0]).__name__ == 'int':
        return valid_permutation(_object)

    if 'str' == type(_object).__name__ and _object[0] == '0':
        return valid_word(_object)

    if type(_object).__name__ == 'str' and x[0] == '(':
        return valid_bracketing(_object)

    if type(_object).__name__ in ('list', 'tuple') and type(_object[0]).__name__ == 'str':
        if _object[0][0] == '(':
            return valid_pattern(_object)
    return False


def to_tuple(_object):
    v_ret = []
    if type(_object).__name__ == 'str':
        for num in _object.split(' '):
            v_ret.append(int(num))
        return tuple(v_ret)
    if type(_object).__name__ == 'dict':
        k = 1
        while True:
            try:
                v_ret.append(_object[str(k)])
                k = k + 1
            except KeyError:
                break
        return v_ret


def symmetric(bracketing):
    v_ret = ''
    for char in bracketing[::-1]:
        if char == '(':
            v_ret = v_ret + ')'
        if char == ')':
            v_ret = v_ret + '('
    return v_ret


def reversing_bracketing(n):
    v_ret = ''
    for i in range(0, n):
        v_ret = v_ret + '('
    for i in range(0, n):
        v_ret = v_ret + ')'
    return v_ret


def get_brackets(n):
    if n == 0:
        return ['']
    if n == 1:
        return ['()']
    if n == 2:
        return ['()()', '(())']
    if n == 3:
        return ['((()))', '(())()', '()(())', '(()())', '()()()']
    if n == 4:
        return ['()((()))', '()(())()', '()()(())', '()(()())', '()()()()', '(())()()', '(())(())',
                '(()())()', '((()))()', '(((())))', '((())())', '(()(()))', '((()()))', '(()()())']
    ret = []

    for i in range(n):
        brackets1 = get_brackets(i)
        brackets2 = get_brackets(n-i-1)
        for b1 in brackets1:
            for b2 in brackets2:
                ret.append("(" + b1 + ")" + b2)
    return tuple(ret)


def get_inverse_permutation(permutation):
    n = len(permutation)
    v_ret = []
    for i in range(1, n + 1):
        v_ret.append(list(permutation).index(i) + 1)
    return tuple(v_ret)


def print_controls():
    print('to enter first stack enter 0')
    print('to pop from stack number i enter i')
    print('to undo enter "undo"')
    print('for ending the game enter "end"')


def print_layout(situation, k):
    print('\n')
    print('input is: ' + str(situation['permutation']) + '    output is: ' + str(situation['output']) +
          '      generated word is:              ' + situation['generated_word'])
    print('\n')
    length = 0
    for lll in situation['stacks'].values():
        if len(lll) > length:
            length = len(lll)
    for i in range(length):
        line = ''
        for j in range(k):
            if len(situation['stacks'][str(j+1)]) > i:
                if situation['stacks'][str(j+1)][i] > 9:
                    line = line + '   ' + str(situation['stacks'][str(j+1)][i])
                else:
                    line = line + '    ' + str(situation['stacks'][str(j+1)][i])
            else:
                line = line + '     '
        print(line)
    caption = '   '
    for i in range(k):
        caption = caption + 'st' + str(i+1) + '  '
    print(caption + '\n')


def open_bracket(pattern):
    for i in pattern:
        if i[:1] == ')':
            return True
    return False


def normalize_word(word):
    l = []
    for char in word:
        l.append(int(char))
    changed = True
    while changed:
        changed = False
        for i in range(len(l)-1):
            if l[i+1] - l[i] > 1:
                changed = True
                c = l[i+1]
                l[i+1] = l[i]
                l[i] = c
    return to_string(l, False)


def word_to_pattern(word):  # TODO: not tested
    if not valid(word):
        return False
    stacks = {}
    k = int(word[-1:])
    for i in range(1, k+1):
        stacks[str(i)] = ''
    for char in word:
        if char == '0':
            stacks['1'] = stacks['1'] + '('
        elif char == str(k):
            stacks[str(k)] = stacks[str(k)] + ')'
        else:
            stacks[char] = stacks[char] + ')'
            next_stack = str(int(char)+1)
            stacks[next_stack] = stacks[next_stack] + '('
    return to_tuple(stacks)


def pattern_to_word(pattern):
    if type(pattern).__name__ == 'str':
        pattern = pattern.replace('(', '0')
        pattern = pattern.replace(')', '1')
        return pattern

    if type(pattern).__name__ in ('tuple', 'list'):
        v_ret = ''
        while pattern[0]:
            pattern[0] = pattern[0][1:]
            v_ret = v_ret + '0'
            # print('added to first stack')
            # print(pattern)
            # print(v_ret)
            # print('\n')
            while open_bracket(pattern):
                for i in range(len(pattern)):
                    if i == len(pattern) - 1 and pattern[i][:1] == ')':
                        pattern[i] = pattern[i][1:]
                        v_ret = v_ret + str(i + 1)
                        # print('cleaning last')
                        # print(pattern)
                        # print(v_ret)
                        # print('\n')
                    elif pattern[i][:1] == ')':
                        pattern[i] = pattern[i][1:]
                        pattern[i+1] = pattern[i+1][1:]
                        v_ret = v_ret + str(i+1)
                        # print('cleaning')
                        # print(pattern)
                        # print(v_ret)
                        # print('\n')

        return v_ret
# def two_stack_unsolvable(n):
#     f = open(critical_8, 'w')
#     v_ret = []
#     brackets = get_brackets(n)
#     all_permutations = itertools.permutations(list(range(1, n + 1)))
#     for perm in all_permutations:
#         if (perm.index(1) < 6 and perm.index(2) < 6) or \
#                 (perm.index(n) in (0, 1, n - 1) and perm.index(n-1) in (0, 1, n - 1)):
#             continue
        # for b in brackets:
        #     if not exists_monotonic_image(bracketing_permutation(perm, b), (2, 3, 1)):
        #         break
        # else:
        #     print(perm)
        #     word = ''
        #     for i in range(n):
        #         word = word + ' ' + str(perm[i])
        #     f.write(word[1:])
        #     f.write('\n')
        #     v_ret.append(tuple(perm))
        # f.close()
    # return tuple(v_ret)


def cleanse(permutation, sign):
    if permutation == [1]:
        return [1]
    l = []
    x = len(permutation) + 2
    if sign == '+':
        for i in range(len(permutation) - 1):
            if permutation[i+1] - permutation[i] == 1:
                x = permutation[i + 1]
                permutation.remove(x)
                break

        for i in permutation:
            if i > x:
                l.append(permutation.index(i))
        for i in l:
            permutation[i] = permutation[i] - 1

    if sign == '-':
        for i in range(len(permutation) - 1):
            if permutation[i] - permutation[i+1] == 1:
                x = permutation[i]
                permutation.remove(x)
                break

        for i in permutation:
            if i > x:
                l.append(permutation.index(i))
        for i in l:
            permutation[i] = permutation[i] - 1
    return permutation


def stack_sort_1(permutation):
    permutation = list(permutation)
    l = len(permutation)
    v_ret = ''
    x = 1
    operational = []
    ok = True
    while ok:
        if not operational or operational[0] != x:
            if permutation:
                operational.insert(0, permutation.pop(0))
                v_ret = v_ret + '('
            else:
                return False
        elif operational[0] == x:
            operational.pop(0)
            v_ret = v_ret + ')'
            if x == l:
                return v_ret
            x = x + 1


def stack_gen_1(permutation):
    permutation = list(permutation)
    permutation.reverse()
    l = 1
    v_ret = ''
    x = len(permutation)
    operational = []
    ok = True
    while ok:
        if not operational or operational[0] != x:
            if permutation:
                operational.insert(0, permutation.pop(0))
                v_ret = v_ret + '('
            else:
                return False
        elif operational[0] == x:
            operational.pop(0)
            v_ret = v_ret + ')'
            if x == l:
                return symmetric(v_ret)
            x = x - 1
