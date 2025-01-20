def add_stock(warehouse, product):

    if not product in warehouse:
        warehouse[product] = 1
    else:
        warehouse[product] += 1


def remove_stock(warehouse, product):

    if not product in warehouse:
        print(f"{product} not in stock")
    elif warehouse[product] == 1:
        del (warehouse[product])
    else:
        warehouse[product] -= 1


def get_stock(warehouse, product):
    return int(warehouse.get(product, 0))


warehouse = {"A": 10, "B": 15, "C": 1, "D": 2}

add_stock(warehouse, "A")    # stock for A should now be 11
remove_stock(warehouse, "D")  # stock for D should now be 1
# The key/value pair for key "C" should be removed
remove_stock(warehouse, "C")
remove_stock(warehouse, "X")  # should print: X not in stock
print(get_stock(warehouse, "B"))    # should return 15
print(get_stock(warehouse, "C"))    # should return 0


print(warehouse)
