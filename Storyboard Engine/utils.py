import shutil


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


def copy_file(src_name, dst_name):
    try:
        shutil.copy(src_name, dst_name)
    except shutil.SameFileError:
        pass
    return
