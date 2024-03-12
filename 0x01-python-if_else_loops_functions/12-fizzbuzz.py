#!/usr/bin/python3


def fizzbuzz():
    """
    The classic FizzBuzz...
    For multiples of three print Fizz.
    For multiples of five print Buzz.
    For numbers which are multiples of both print FizzBuzz.
    For all other numbers, print them as they are.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        else:
            print("{}".format(i), end=' ')
