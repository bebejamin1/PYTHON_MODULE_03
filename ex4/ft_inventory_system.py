#! /bin/python3.10

import sys


# =============================================================================
# ================================ test =======================================
# =============================================================================


def test_entry(argv: list) -> dict:
    item_dict = {}
    for item in argv[1:]:
        try:
            if (':' not in item):
                raise AttributeError("❌​ Incorrect format, try object:qty")
            item = item.split(":")
            item[1] = int(item[1])
            if (item[1] <= 0):
                raise ValueError()
            item_dict[item[0]] = item[1]
        except AttributeError as e:
            print(e)
        except ValueError:
            print(f"❌​ Quantity not in the correct data type '{item[1]}', "
                  "try with an int positiv")
    return (item_dict)


# =============================================================================


def inventory_sys(item_dict: dict) -> int:
    sum_dict = 0
    for v in item_dict.values():
        sum_dict += v
    print(f"Total items in inventory: {sum_dict}")
    print("Unique item types:", len(item_dict))
    return (sum_dict)


# =============================================================================


def current_inventory(item_dict: dict, sum_dict: int) -> int:
    for keys, values in sorted(item_dict.items(),
                               key=lambda item: item[1], reverse=True):
        print(f"{keys}: {values} ", end="")
        print(f"units ({((values/sum_dict)*100):.1f}%)")


# =============================================================================


def stat_inventory(item_dict: dict, scarce: list) -> None:

    # =========================================================================
    # ======================= Inventory Statistic =============================
    # =========================================================================

    print("\n" + " Inventory Statistic ".center(79, "="))
    restock = []
    max = 0
    min = 100000000
    for keys, values in zip(item_dict.keys(), item_dict.values()):
        if (values > max):
            max = values
            max_dict = keys
            moderate = {keys: values}
        if (values < min):
            min = values
            restock == (keys)
        if (values == min):
            restock.append(keys)

    print(f"Most abundant: {max_dict} ({max} units)")
    print(f"Least abundant: {restock[0]} ({item_dict[restock[0]]} units)")

    # =========================================================================
    # ========================= Item Categories ===============================
    # =========================================================================

    print("\n" + " Item Categories ".center(79, "="))
    print(f"Moderate: {moderate}")

    rare_dict = {}
    for rare in item_dict.items():
        rare = str(rare)
        rare = rare.split(", ")
        rare[1] = rare[1].replace(")", "")
        rare[1] = int(rare[1])
        for scar in scarce:
            if (item_dict.get(scar, 0) != 0):
                rare_dict[scar] = item_dict[scar]
    print("Scarce: ", rare_dict)

    # =========================================================================
    # ====================== Management Suggestions ===========================
    # =========================================================================

    print("\n" + " Management Suggestions ".center(79, "="))
    print("Restock needed: ", restock)
    # for values in item_dict.values():


# =============================================================================
# ================================ MAIN =======================================
# =============================================================================


if __name__ == "__main__":

    scarce = ["sword", "shield", "armor", "helmet"]

    n = len(sys.argv)
    if (n > 1):
        item_dict = test_entry(sys.argv)

        print("\n" + " Inventory System Analysis ".center(79, "="))
        sum_dict = inventory_sys(item_dict)

        print("\n" + " Current Inventory ".center(79, "="))
        current_inventory(item_dict, sum_dict)

        stat_inventory(item_dict, scarce)

        print("\n" + " Dictionary Properties Demo ".center(79, "="))
        print("Dictionary keys: ", list(item_dict.keys()))
        print("Dictionary values: ", list(item_dict.values()))

        search_in_inventory = "sword"
        if (item_dict.get(search_in_inventory)):
            print(f"Sample lookup - '{search_in_inventory}' "
                  "in inventory: True")
        else:
            print(f"Sample lookup - '{search_in_inventory}' "
                  "in inventory: False")
    else:
        f = "try with this command example\n./" \
            "ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1"
        print(f)
