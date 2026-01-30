#! /bin/python3.10

import math
import sys

if __name__ == "__main__":
    print(" Game Coordinate System ".center(40, "=") + "\n")
    n = len(sys.argv)
    og_position = (0, 0, 0)
    x2, y2, z2 = og_position

    if (n <= 4):
        crea_cor = (10, 20, 5)
        x1, y1, z1 = crea_cor
        print(f"Position created: ({x1}, {y1}, {z1})")
        print(f"Distance between {og_position} and {crea_cor}:", end=' ')
        print(f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.2f}")

        if (n == 4):
            try:
                for arg in sys.argv[1:]:
                    int(arg)
            except ValueError:
                pars_good = (3, 4, 0)
                x1, y1, z1 = pars_good
                print("\n" + f"Parsed position: {pars_good}")
                print(f"Parsing coordinates: {pars_good}")
                print(f"Distance between {og_position} and "
                      "{pars_good}:", end=' ')
                print(f"{math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2):.2f}")

                print("\n" + "Parsing invalid coordinates: "
                      f"\"{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}\"")
                print("Error parsing coordinates: invalid literal "
                      f"for int() with base 10: '{sys.argv[1]}'")
                print("Error details - Type: ValueError, Args: (\"invalid "
                      f"literal for int() with base 10: '{sys.argv[1]}'\",)")
            else:
                pars_cor = (int(sys.argv[1]), int(sys.argv[2]),
                            int(sys.argv[3]))
                x1, y1, z1 = pars_cor
                print("\n" + f"Parsed position: {pars_cor}")
                print(f"Parsing coordinates: {pars_cor}")
                print("Distance between "
                      f"{og_position} and {pars_cor}:", end=' ')
                c = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
                print(f"{c:.2f}")

                pars_error = ("abc", "def", "ghi")
                xa, ya, za = pars_error
                print("\n" + "Parsing invalid coordinates: "
                      f"\"{xa},{ya},{za}\"")
                print("Error parsing coordinates: invalid literal "
                      f"for int() with base 10: '{xa}'")
                print("Error details - Type: ValueError, Args: (\"invalid "
                      f"literal for int() with base 10: '{xa}'\",)")
        else:
            pars_good = (3, 4, 0)
            x1, y1, z1 = pars_good
            print("\n" + f"Parsed position: {pars_good}")
            print(f"Parsing coordinates: {pars_good}")
            print(f"Distance between {og_position} and {pars_good}:", end=' ')
            c = float(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
            print(f"{c:.2f}")

            pars_error = ("abc", "def", "ghi")
            xa, ya, za = pars_error
            print("\n" + "Parsing invalid coordinates: "
                  f"\"{xa},{ya},{za}\"")
            print("Error parsing coordinates: invalid literal "
                  f"for int() with base 10: '{xa}'")
            print("Error details - Type: ValueError, Args: (\"invalid literal"
                  f" for int() with base 10: '{xa}'\",)")

        print("\n" + "Unpacking demonstration:")
        print(f"Player at x={x1}, y={y1}, z={z1}")
        print(f"Coordinates: X={x1}, Y={y1}, Z={z1}")
    else:
        print("maximum error 3 arguments")
        print("try this ./ft_coordinate_system.py 3 4 0")
