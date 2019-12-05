# Advent of Code 2019


def main():
    # coding is fun
    filename = "aoc_input1.txt"

    fp = open(filename)

    inputs = fp.readlines()
    print(len(inputs))

    total = 0

    for mass in inputs:
        num = int(mass.strip())
        num = int(num/3)
        num -= 2
        total += num

    print(total)

    fp.close()


main()
