def fill_list():
    empty_list = []
    filled_list = False
    while not filled_list:
        value = input()
        try:
            empty_list.append(int(value))
        except ValueError:
            if value != "":
                print("not number")
            else:
                return empty_list


def find_max(unsorted_list):
    max = 0
    for i in range(0, len(unsorted_list)):
        if unsorted_list[i] > max:
            max = unsorted_list[i]
    return max


def counting_sort(unsorted_list):
    max = find_max(unsorted_list)
    counted_list = []
    # print(max + 1)
    for i in range(0, max + 1):
        # print(i)
        counted_list.append(0)

    number_of_times = len(unsorted_list)
    for i in range(0, number_of_times):
        counted_list[unsorted_list[i]] += 1

    sorted_list = []
    for i in range(0, max + 1):
        for j in range(0, counted_list[i]):
            sorted_list.append(i)

    return sorted_list


unsorted_list = fill_list()
unsorted_list = counting_sort(unsorted_list)
print(unsorted_list)