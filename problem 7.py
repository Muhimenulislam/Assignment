def second_largest(lst):
    unique_sorted_list = sorted(set(lst), reverse=True)
    if len(unique_sorted_list) > 1:
        print(f"The second largest number is: {unique_sorted_list[1]}")
    else:
        print("List does not have a second largest number.")

second_largest([1, 22, 35, -10, 7])
