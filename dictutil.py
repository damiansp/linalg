def dict2list(dct, keylist):
    return [dct[k] for k in keylist]


def list2dict(L, keylist):
    return {k: v for k, v in zip(keylist, L)}


def listrange2dict(L):
    return {k: v for k, v in enumerate(L)}


if __name__ == '__main__':
    def test():
        test_dict2_list()
        test_list2dict()
        test_listrange2dict()
        print('Tests passed')

    def check(test_name, ex, got):
        assert ex == got, f'Expected: {expected}, got: {got}'
        print(f'{test_name} passed')
        
    def test_dict2_list():
        dct = {'a': 'A', 'b': 'B', 'c': 'C'}
        keylist = ['b', 'c', 'a']
        expected = ['B', 'C', 'A']
        got = dict2list(dct, keylist)
        check('dict2list', expected, got)

    def test_list2dict():
        L = ['A', 'B', 'C']
        keylist = ['a', 'b', 'c']
        expected = {'a': 'A', 'b': 'B', 'c': 'C'}
        got = list2dict(L, keylist)
        check('list2dict', expected, got)

    def test_listrange2dict():
        L = ['0', '1', '10', '11']
        expected = {0: '0', 1: '1', 2: '10', 3: '11'}
        got = listrange2dict(L)
        check('listrange2dict', expected, got)
    test()
