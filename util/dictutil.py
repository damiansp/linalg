def dict2list(dct, keylist):
    return [dct[k] for k in keylist]


def list2dict(L, keylist):
    return {k: v for k, v in zip(keylist, L)}


def listrange2dict(L):
    return {k: v for k, v in enumerate(L)}


def make_inverse_index(strlist):
    out = {}
    for i, s in enumerate(strlist):
        for word in s.split():
            out[word] = out.get(word, set()).union({i})
    return out


def or_search(inv_index, query):
    out = set()
    for word in query:
        out = out.union(inv_index.get(word, set()))
    return out


def and_search(inv_index, query):
    out = inv_index[query[0]]
    if len(query) > 1:
        for word in query[1:]:
            out = out.intersection(inv_index.get(word, set()))
    return out



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
