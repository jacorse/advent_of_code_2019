# Advent of Code 2019
# Day 3 code
import numpy as np


def shortest_distance(filename):
    fp = open(filename)
    wires = fp.readlines()

    # separate variables for both wires and split instructions
    wire1_instructions = wires[0].split(",")
    wire2_instructions = wires[1].split(",")
    # wire1 = wire1.split(",")
    # wire2 = wire2.split(",")
    wire1_pos = [(0, 0)]

    for instr in wire1_instructions:
        direction, dist, last_index = instr[0], int(instr[1:]), len(wire1_pos) - 1
        lastx, lasty = wire1_pos[last_index][0], wire1_pos[last_index][1]
        if direction is "U":
            wire1_pos.append((lastx, lasty + dist))
        elif direction is "D":
            wire1_pos.append((lastx, lasty - dist))
        elif direction is "L":
            wire1_pos.append((lastx - dist, lasty))
        else:      # dir is "R"
            wire1_pos.append((lastx + dist, lasty))


    solution = wires
    return solution


def man_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def get_lines(wire1, wire2):    #(1 or 2, static, (range))
    for instr in wire1:
        direction, dist, last_index = instr[0], int(instr[1:]), len(wire1_pos) - 1
        lastx, lasty = wire1_pos[last_index][0], wire1_pos[last_index][1]
        if direction is "U":
            wire1_pos.append((lastx, lasty + dist))
        elif direction is "D":
            wire1_pos.append((lastx, lasty - dist))
        elif direction is "L":
            wire1_pos.append((lastx - dist, lasty))
        else:      # dir is "R"
            wire1_pos.append((lastx + dist, lasty))
