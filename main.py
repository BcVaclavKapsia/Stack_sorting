from helpers import *


class Meta(type):
    def __iter__(self):
        return self.class_iter()


class Permutation:
    __metaclass__ = Meta
    by_id = {}

    def __init__(self, perm_tuple):
        self.perm_tuple = perm_tuple
        self.n = len(perm_tuple)

        key = to_string(perm_tuple)  # registration for iteration
        self.by_id = key
        self.by_id[key] = self

    @classmethod
    def class_iter(cls):  # iterate over class by giving all instances which have been instantiated
        return iter(cls.by_id.values())

    def show(self):
        print(self.perm_tuple)


class Bracketing:
    def __init__(self, code):
        self.code = code
        self.n = len(code)/2

    def show(self):
        print(self.code)


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.n = len(pattern[0])/2

    def show(self):
        for bracketing in self.pattern:
            print(bracketing)


class Word:
    def __init__(self, string):
        self.string = string
        self.k = int(self.string[-1:])
        self.n = int(len(self.string) / self.k)


def monotonic_image(permutation, sub_permutation):
    # TODO: Optimize
    permutation = trimmed_permutation(list(permutation), list(sub_permutation))  # massive optimization!!!
    v_ret = []
    if not permutation:
        return tuple(v_ret)
    n = len(sub_permutation)
    for actual_sub_permutation in itertools.combinations(permutation, n):
        if check_monotony_relation(actual_sub_permutation, sub_permutation):
            v_ret.append(actual_sub_permutation)
    return tuple(v_ret)


def exists_monotonic_image(permutation, sub_permutation):
    n = len(sub_permutation)
    for actual_sub_permutation in itertools.combinations(permutation, n):
        if check_monotony_relation(actual_sub_permutation, sub_permutation):
            return True
    return False


def game(permutation, k):
    number_test = '0123456789'
    game_on = True
    layout = {'permutation': list(permutation), 'output': [], 'generated_word': '', 'stacks': {}}
    print_controls()

    for i in range(k):
        layout['stacks'][str(i+1)] = []
    while game_on:
        print_layout(layout, k)
        user_input = input('\nplease enter next move: ')
        if user_input not in ('undo', 'end'):
            try:
                user_input = int(user_input)
            except ValueError:
                print('\ninput not valid')
                continue
            user_input = str(user_input)
            if int(user_input) > k:
                print('\ninput not valid')
                continue
        if user_input == 'end':
            break

        if user_input == 'undo':
            if not layout['generated_word']:
                print('\ninput not valid')
                continue
            else:
                last_char = layout['generated_word'][-1:]
                if last_char == '0':
                    layout['permutation'].insert(0, layout['stacks']['1'].pop(0))
                    # new_generated_word = layout['generated_word']
                    # layout['generated_word'] = new_generated_word[:-1]
                elif last_char == str(k):
                    layout['stacks'][str(k)].append(layout['output'].pop())
                else:
                    layout['stacks'][last_char].insert(0, layout['stacks'][str(int(last_char) + 1)].pop(0))
                new_generated_word = layout['generated_word']
                layout['generated_word'] = new_generated_word[:-1]

        if user_input in number_test[:k+1]:
            if user_input == '0':
                if layout['permutation']:
                    layout['stacks']['1'].insert(0, layout['permutation'].pop(0))
                    layout['generated_word'] = layout['generated_word'] + '0'
                else:
                    print('\ninput not valid try something different')
            else:
                print('proslo to pres nulu')
                if user_input == str(k):
                    if layout['stacks'][user_input]:
                        layout['output'].append(layout['stacks'][str(k)].pop(0))
                        layout['generated_word'] = layout['generated_word'] + str(k)
                    else:
                        print('\ninput not valid try something different')
                else:
                    if layout['stacks'][user_input]:
                        layout['stacks'][str(int(user_input) + 1)].insert(0, layout['stacks'][user_input].pop(0))
                        layout['generated_word'] = layout['generated_word'] + user_input
                    else:
                        print('\ninput not valid try something different')


def game_on_word(permutation, word, k):
    if not valid(word) or not valid(permutation):
        print('something went wrong')
        return False
    layout = {'permutation': list(permutation), 'output': [], 'generated_word': '', 'stacks': {}}

    for i in range(k):
        layout['stacks'][str(i + 1)] = []
    print_layout(layout, k)

    for char in word:
        if char == '0':
            if layout['permutation']:
                layout['stacks']['1'].insert(0, layout['permutation'].pop(0))
                layout['generated_word'] = layout['generated_word'] + '0'
        else:
            if char == str(k):
                if layout['stacks'][char]:
                    layout['output'].append(layout['stacks'][str(k)].pop(0))
                    layout['generated_word'] = layout['generated_word'] + str(k)
            else:
                layout['stacks'][str(int(char) + 1)].insert(0, layout['stacks'][char].pop(0))
                layout['generated_word'] = layout['generated_word'] + char
        print_layout(layout, k)


def permutate(permutation, tool):
    pass


def minimal_value(layout):
    pass


def stronger(permutation, k):
    # layout = generate_beginning_layout(permutation, k)
    # agenda = generata_agenda(k)
    pass