#!/usr/bin/env python3

# Created by: Khang Le
# Created on: November 2019
# This program convert TC to TF


def main():

    tc = int(input("Enter temperature in Celsius: "))
    tf = 9/5 * tc + 32
    print("The temperature in Fahrenheit is: {}".format(tf))


if __name__ == "__main__":
    main()
