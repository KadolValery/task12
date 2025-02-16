class RangeSquared:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            square = self.current ** 2
            self.current += 1
            return square
        else:
            raise StopIteration

range_squared = RangeSquared(1, 5)
for square in range_squared:
    print(square)

    #task2

def factorials(n):
    factorial_list = []
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            factorial_list.append(1)
        else:
            factorial *= i
            factorial_list.append(factorial)
    return factorial_list


result = factorials(5)
print(result)

#task 3
def read_file_lines(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.rstrip('\n'))
    return lines


filename = 'example.txt'
lines = read_file_lines(filename)
for line in lines:
    print(line)