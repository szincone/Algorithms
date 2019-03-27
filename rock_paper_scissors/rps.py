#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    rps_list = ['rock', 'paper', 'scissors']
    result = []
    if n == 0:
        return [result]

    def rounds(rps_order, round_number):
        for i in range(len(rps_list)):
            rps_order.append(rps_list[i])
            if (round_number == n):
                result.append(rps_order[:])
            else:
                rounds(rps_order, round_number + 1)
            rps_order.pop()
    rounds([], 1)
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
