# Advent of Code 2019
# Day 2 code
import copy


def intcode_computer(filename):
    fp = open(filename)
    broken_program = fp.read()
    # program comes in as one long str. This splits into list at commas and converts to ints
    broken_program = broken_program.split(",")
    broken_program = list(map(int, broken_program))

    # repair program to state it was in prior to 1202 program alarm
    program = restore_gravity_assist_program(broken_program)
    # make a copy as to not change original during part 2
    test_program = copy.copy(program)

    # run the program to find output
    program_output = run_program(test_program)

    # result for day 2 part 1. comment out for results for day 2 part 2
    # return program_output

    # finding noun and verb to get output = 19690720
    for x in range(0, 100):
        for y in range(0, 100):
            test_program = copy.copy(program)
            test_program[1] = x
            test_program[2] = y
            if run_program(test_program) == 19690720:
                return "{:02d}{:02d}".format(x, y)







def restore_gravity_assist_program(broken_program):
    broken_program[1] = 12
    broken_program[2] = 2

    return broken_program


def run_program(program):
    instruction_pointer = 0
    while program[instruction_pointer] != 99:
        if program[instruction_pointer] == 1:
            parameter1 = program[instruction_pointer + 1]
            parameter2 = program[instruction_pointer + 2]
            parameter3 = program[instruction_pointer + 3]
            program[parameter3] = program[parameter1] + program[parameter2]
        elif program[instruction_pointer] == 2:
            parameter1 = program[instruction_pointer + 1]
            parameter2 = program[instruction_pointer + 2]
            parameter3 = program[instruction_pointer + 3]
            program[parameter3] = program[parameter1] * program[parameter2]
        instruction_pointer += 4

    output = program[0]

    return output
