#! /bin/python3.10

import sys


def ft_command_quest() -> None:
    n = len(sys.argv)

    if (n == 1):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {n}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {n - 1}")
        i = 1
        while (i < n):
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {n}")


if __name__ == "__main__":
    print(" Command Quest ".center(40, "="))
    ft_command_quest()
