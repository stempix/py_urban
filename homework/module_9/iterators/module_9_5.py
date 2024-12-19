class StepValueError(ValueError):
    pass

class Iterator:

    def __init__(self, start, stop, step = 1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        # Здесь нужно присваивать start - step, т.к. в __next__ изначально будет добавление pointer += step,
        # которое сдвинет на одну позицию вперед pointer и вернется уже второе значение
        self.pointer = self.start - self.step

    def __iter__(self):
        # По аналогии с __init__
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if (self.step < 0 and self.pointer < self.stop) or (self.step > 0 and self.pointer > self.stop):
            raise StopIteration()
        else:
            return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
    print()
except StepValueError as exc:
    print(*exc.args)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()