# Advent of Code 2019
import day1
import day2
import day3


def main():
    # initial input from day 1 of Advent of Code 2019
    module_masses = "aoc_input1.txt"
    intcode_program = "aoc_input2.txt"
    crossed_wires = "aoc_input3.txt"

    # day 1 solutions:
    fuel_part1, fuel_part2 = day1.calculate_fuel(module_masses)
    print("Fuel for day 1 part 1 is {} and for part 2 is {}".format(fuel_part1, fuel_part2))

    # day 2 solutions:
    # part 1 solution:     (make sure code is uncommented in day2.py)
    # start_value = day2.intcode_computer(intcode_program)
    # print("Start value for day 2 part 1 is {}".format(start_value))
    # part 2 solution:     (make sure part 1 code is commented out in day2.py)
    nounverb = day2.intcode_computer(intcode_program)
    print("The four digit nounverb code is {}".format(nounverb))

    # day 3 solutions
    wires = day3.shortest_distance(crossed_wires)


main()
