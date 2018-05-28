f = lambda i, x: b"Hello,"[i] if i < len(b"Hello,") else x


def g(i, x):
    if i >= 6:
        return b" World!\n"[i-6]


filters = [f, g]
