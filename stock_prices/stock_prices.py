#!/usr/bin/python

import argparse


def find_max_profit(prices):
    profit_list, profit, loss = [], [], []
    down_bool = False
    for i in range(len(prices) - 1):
        if prices[i] > prices[i + 1]:
            down_bool = True
        elif prices[i] < prices[i + 1]:
            down_bool = False
        if down_bool is True:
            profit.append(prices[i + 1] - prices[i])
        elif down_bool is False:
            loss.append(prices[i + 1] - prices[i])
        if down_bool is True and len(loss) > 0:
            profit_list.append(sum(x for x in loss))
            loss = []
        elif down_bool is False and len(profit) > 0:
            profit_list.append(sum(x for x in profit))
            profit = []
        if i == len(prices) - 2 and len(profit_list) == 0:
            profit_list.append(profit)
            profit_list.append(loss)
    if isinstance(max(profit_list), int):
        return max(profit_list)
    else:
        if len(profit_list[0]) > 0:
            return max([x for x in profit_list[0]])
        else:
            return max([x for x in profit_list[1]])


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
