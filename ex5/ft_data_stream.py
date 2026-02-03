#! /bin/python3.10

import random
import time


# =============================================================================
# =============================== Stream ======================================
# =============================================================================


def name_data():
    name = ["Elouann", "Leo", "Hugo", "NomiNoe", "Timothee", "Marie-Ève",
            "Augustine", "Fleur", "Valerie", "Benjamin", "Ronan", "Georgine",
            "Marceau", "Lya", "Flavie", "Eulalie", "Maxime", "Cédric",
            "Killian", "Simon", "Yvonne", "Jean-Christophe", "Timéo"]
    while True:
        yield random.choice(name)


def level_data():
    while True:
        x = random.randint(1, 8000)
        yield x


def achievement_data():
    achievement = ["Don't Need to Stop", "In One Go!", "Like a Record Baby",
                   "Recharging...", "Well Done", "I'm a Bomb!",
                   "Beyond the Darkness", "Freeplay Freeway",
                   "Killed Monster", "Treasure", "leveled up"]
    while True:
        yield random.choice(achievement)


def event_proc(number_of_event: int) -> list:
    nb = [0, 0, 0]
    n = name_data()
    g = level_data()
    a = achievement_data()

    for i in range(1, (number_of_event + 1)):
        n2 = next(n)

        g2 = next(g)
        if (g2 > nb[0]):
            nb[0] = g2

        a2 = next(a)
        if (a2 == "Treasure"):
            nb[1] += 1
        elif (a2 == "leveled up"):
            nb[2] += 1
        if (i <= 3):
            print(f"Event {i}: Player {n2} (level {g2}) {a2}")

    print("..." + "\n")
    return (nb)


def stream_analystics(nb: list, number_of_event: int):
    print(f"Total events processed: {number_of_event}")
    print(f"High-level players (10+): {nb[0]}")
    print(f"Treasure events: {nb[1]}")
    print(f"Level-up events: {nb[2]}")


# =============================================================================
# ============================== FIBONACCI ====================================
# =============================================================================


def generator_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci(nbr: int) -> None:
    print(f"Fibonacci sequence (first {nbr}): ", end="")
    i = 1
    g = generator_fibonacci()
    while (i <= nbr):
        g2 = next(g)
        print(g2, end=" ")
        i += 1
    print()


# =============================================================================
# ============================= PRIME NUMBER ==================================
# =============================================================================


def generator_fprime():
    f = 2
    while True:
        if (if_fprime(f) == 1):
            yield f
        f += 1


def if_fprime(nb: int) -> int:
    test_nbr = 2
    while (test_nbr < nb):
        if (nb % test_nbr == 0):
            return (0)
        test_nbr += 1
    return (1)


def prime_numbers(nbr: int) -> None:
    print(f"Prime numbers (first {nbr}): ", end="")
    g = generator_fprime()
    for count in range(nbr):
        g1 = next(g)
        print(g1, end=" ")
    print()


# =============================================================================
# ================================ MAIN =======================================
# =============================================================================


if __name__ == "__main__":
    s = time.process_time()
    print(" Game Data Stream Processor ".center(79, "=") + "\n")
    number_of_event = 1000

    print(f"Processing {number_of_event} game events...")

    nb = event_proc(number_of_event)

    print(" Stream Analytics ".center(79, "="))
    stream_analystics(nb, number_of_event)

    print("\n" + "Memory usage: Constant (streaming)")
    e = time.process_time()
    print(f"Processing time: {(e - s):.3f}, seconds")

    print("\n" + " Generator Demonstration ".center(79, "="))
    fibonacci(10)
    prime_numbers(5)
