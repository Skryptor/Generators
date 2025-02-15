class FlatIterator:

    def __init__(self, list_of_list):
        self.lists = list_of_list


    def __iter__(self):
        self.cursor = 0
        self.cursor2 = 0
        return self

    def __next__(self):

        if self.cursor == len(self.lists):
            raise StopIteration

        if self.cursor2 >= len(self.lists[self.cursor]):
            self.cursor += 1
            self.cursor2 = 0
            return self.__next__()
        result = self.lists[self.cursor][self.cursor2]
        self.cursor2 += 1
        return result

import types


def flat_generator(list_of_lists):

    ...
    yield
    ...



