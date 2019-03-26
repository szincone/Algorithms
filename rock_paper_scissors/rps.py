#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps_list = ['rock', 'paper', 'scissors']
    result = []

    def rounds(rps_order, round_number):
        r = rps_order
        for i in range(len(rps_list)):
            r.append(rps_list[i])
            if (round_number == n):
                result.append(r[:])
            else:
                rounds(r, round_number + 1)
            r.pop()
    rounds([], 1)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
