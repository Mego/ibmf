from collections import Iterable
from itertools import tee


class IBMF:
    def __init__(self):
        self.i = 0
        self.filters = []

    def __iter__(self):
        while True:
            options = range(256)
            for f in self.filters:
                prev_options, options = tee(options)
                try:
                    options = f(self.i, options)
                except:
                    return
                if options is None:
                    options = prev_options
                if not isinstance(options, Iterable):
                    options = [options]
                else:
                    options = list(options)
            self.i += 1
            if(len(options)) == 1:
                yield options[0]
            else:
                return

    def add_filters(self, *filters):
        self.filters.extend(*filters)
        return self
