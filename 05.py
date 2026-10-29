def count_items(items_list):
    frequency = {}
    for item in items_list:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency


if __name__ == "__main__":
    items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    print(count_items(items))
