#! /bin/python3.10

import sys

print(" Player Score Analytics ".center(40, "="))
n = len(sys.argv)
arguments = []

try:
    if (n == 1):
        raise ValueError("No scores provided. Usage: python3 "
                         "ft_score_analytics.py<score1> <score2> ...")
except ValueError as e:
    print(e)
else:
    for element in sys.argv[1:]:
        try:
            element = int(element)
            if (element < 0):
                raise ValueError(f"No negative numbers {element}")
        except IndexError:
            print(f"oops, I slipped, I typed ’{element}’ instead of a number.")
        except ValueError as e:
            print(e)
        else:
            arguments.append(element)
    print(f"Scores processed: {arguments}")
    print(f"Total players: {len(arguments)}")
    print(f"Total score: {sum(arguments)}")
    print(f"Average score: {sum(arguments) / len(arguments)}")
    print(f"High score: {max(arguments)}")
    print(f"Low score: {min(arguments)}")
    print(f"Score range: {max(arguments) - min(arguments)}" + "\n")
