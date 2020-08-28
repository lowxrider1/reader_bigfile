def counter(filename, encoding, letter):
    with open(filename, 'r', encoding=encoding) as f:
        counter = 0
        line = f.readline()
        counter_letter = counter_letter + line.count(letter)
        while line:
            counter = counter + 1
            line = f.readline()
            counter_letter = counter_letter + line.count(letter)
        return counter, {letter: counter_letter}


if __name__ == '__main__':
    filename = "QAtest.txt"
    encoding = "utf-8"
    letter = 'а'
    res = counter(filename, encoding, letter)
    print("Количество строк: {0}, Количество букв {1}: {2}".format(res[0], letter, res[1][letter]))
