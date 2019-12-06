# Advent of Code 2019
# Day 1 code


def calculate_fuel(filename):
    fp = open(filename)

    # get list of each line of file in str form
    inputs = fp.readlines()
    # print(len(inputs))

    # will be answers to part 1 and 2 for day 1
    total_part1 = 0
    total_part2 = 0

    # calculate mass for both parts
    for mass in inputs:
        num = int(mass.strip())
        num = int(num / 3)
        num -= 2
        total_part1 += num
        total_part2 += num

        # recursive loop for finding fuel for fuel for fuel...
        # 8 is minimum that will result in 0 which is excluded as defined by problem
        while num > 8:
            num = int(num / 3)
            num -= 2
            total_part2 += num

    # close opened file, good habit to get into :D
    fp.close()

    return total_part1, total_part2
