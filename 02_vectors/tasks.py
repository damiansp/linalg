import numpy as np


def scalar_mult(scalar, vector):
    return [scaler * x for x in vector]


def segment(p1, p2, n=100):
    '''
    Return a list of n points evenly spaced along the segment from p1 to p2
    '''
    p1 = np.array(p1)
    p2 = np.array(p2)
    alpha = np.linspace(0, 1, n)
    return np.array([a*p1 + (1 - a)*p2 for a in alpha])


class Vec:
    def __init__(self, labels, func):
        self.D = labels # domain of func (inputs)
        self.f = func   # maps inputs to outputs

    def set_item(self, key, val):
        self.f[key] = val

    def get_item(self, key, default=None):
        return self.f.get(key, default)

    def scalar_mul(self, alpha):
        prod = Vec(self.D, {k: alpha*v for k, v in self.f.items()})
        return prod
                   

def zero_vec(D, sparse=False):
    assert type(D) is set, 'D must be a set'
    if sparse:
        return Vec(D, {})
    return Vec(D, {i: 0 for i in D})


def add(u, v):
    keys = u.D
    dct = {k: u.f.get(k, 0) + v.f.get(k, 0) for k in keys}
    return Vec(keys, dct)


def neg(v):
    return v.scalar_mul(-1)


# Test
v = Vec({'A', 'B', 'C'}, {'A': 1, 'B': 2, 'C': 3})
b = v.scalar_mul(3)
for key, val in b.f.items():
    print(f'{key} -> {val}')

u = Vec(v.D, {'A': 5., 'C': 10.})
x = add(u, v)
print(x.f)
print(neg(x).f)
