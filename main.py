from random import randint
    def s(x, y, z):
        p = (x + y + z) / 2
        return (p * (p - x) * (p - y) * (p - z)) ** 0.5
n = 0
    array = [randint(1, 50) for i in range(50)]
    print(array)

    array.sort(reverse=True)

    for i in range(len(array) - 2):
        if array[i] < (array[i + 1] + array[i + 2]):
            print(array[i], array[i + 1], array[i + 2], s(array[i], array[i + 1], array[i + 2]))
            break
