import sys


def fill_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}
    for arg in args:
        item_parts = arg.split(":")
        if len(item_parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item_name = item_parts[0]
        if item_name in inventory.keys():
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            quantity = int(item_parts[1])
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        inventory.update({item_name: quantity})
    return inventory


def print_item_percentages(
    inventory: dict[str, int],
    total_quantity: int,
) -> None:
    for key in inventory.keys():
        if total_quantity == 0:
            percentage = 0.0
        else:
            percentage = round(inventory[key] / total_quantity * 100, 1)
        print(
            f"Item {key} represents "
            f"{percentage}%"
        )


def find_most_abundant_item(inventory: dict[str, int]) -> str:
    keys = list(inventory.keys())
    item_name = keys[0]
    quantity = inventory[keys[0]]

    for key in keys[1:]:
        if quantity < inventory[key]:
            item_name = key
            quantity = inventory[key]

    return item_name


def find_least_abundant_item(inventory: dict[str, int]) -> str:
    keys = list(inventory.keys())
    item_name = keys[0]
    quantity = inventory[keys[0]]

    for key in keys[1:]:
        if inventory[key] < quantity:
            item_name = key
            quantity = inventory[key]

    return item_name


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print(
            "No items provided. Usage: "
            "python3 ft_inventory_system.py <item_name>:<quantity> ..."
        )
        return

    inventory = fill_inventory(sys.argv[1:])

    if len(inventory) == 0:
        print("Got inventory: {}")
        return

    total_quantity = sum(list(inventory.values()))
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")
    print_item_percentages(inventory, total_quantity)

    most_abundant = find_most_abundant_item(inventory)
    least_abundant = find_least_abundant_item(inventory)
    print(
        f"Item most abundant: {most_abundant} "
        f"with quantity {inventory[most_abundant]}"
    )
    print(
        f"Item least abundant: {least_abundant} "
        f"with quantity {inventory[least_abundant]}"
    )

    inventory.update(magic_item=1)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
