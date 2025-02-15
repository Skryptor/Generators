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



def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if isinstance(item, list):
                self.stack.append(iter(item))
            else:
                return item

        raise StopIteration

def flat_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flat_generator(item)  # Рекурсивный вызов для вложенных списков
        else:
            yield item  # Возвращаем элемент, если это не список



