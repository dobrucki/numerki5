def horner(args, x):
    if args:
        res = 0
        for arg in args:
            res *= x
            res += arg
        return res
    return None
