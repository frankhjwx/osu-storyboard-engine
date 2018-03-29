codeArgNum = {
    'M': 2, 'F': 1, 'S': 1,
    'V': 2, 'MX': 1, 'MY': 1,
    'VX': 1, 'VY': 1, 'R': 1,
    'C': 3, 'P': 1
}


def time_parser(s):
    args = s.split(':')
    m = int(args[0])
    s = int(args[1])
    ms = int(args[2])
    if not (0 <= 59 and 0 <= ms <= 999):
        raise RuntimeError('Wrong Timing Format.')
    return (m * 60 + s) * 1000 + ms


def command(*args):
    s = ','.join(str(arg) for arg in args)
    return s


def get_timing(start_t, end_t=''):
    """Return a list like [start_t, end_t], end_t default value is a empty."""
    return [start_t, end_t]


def array_to_list(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            a = array_to_list(i, a)
        else:
            a.append(i)
    return a
