#!/bin/python3

import os


class VendingMachine:
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price

    def buy(self, req_items, money):
        if req_items > self.num_items:
            raise ValueError("Not enough items in the machine")

        total_cost = req_items * self.item_price
        if money < total_cost:
            raise ValueError("Not enough coins")

        change = money - total_cost
        self.num_items -= req_items

        return change


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            fptr.write(str(change) + "\n")
        except ValueError as e:
            fptr.write(str(e) + "\n")

    fptr.close()
