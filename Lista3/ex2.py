# 2) Implemente um algoritmo que retorne o I itens mais próximos de um valor V, para um
# vetor qualquer de elementos inteiros. V pode estar ou não presente no vetor. Sua
# solução deve ser O(nlogn).


def mergeSort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        # Recursive call
        mergeSort(left)
        mergeSort(right)
        # Index for each array
        left_index = 0
        right_index = 0
        # Index for my_list
        k = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                my_list[k] = left[left_index]
                left_index += 1
            else:
                my_list[k] = right[right_index]
                right_index += 1
            k += 1

        # Add the rest of values to array
        while left_index < len(left):
            my_list[k] = left[left_index]
            left_index += 1
            k += 1

        while right_index < len(right):
            my_list[k] = right[right_index]
            right_index += 1
            k += 1


def findIndex(array, value):
    try:
        return array.index(value)
    except ValueError:
        return -1


# Binary Search to get the lower index or the index value when exist the value
def search_lower_index(array, lower, higher, value):
    if array[higher] <= value:
        return higher
    if array[lower] > value:
        return lower

    while lower <= higher:
        mid = (lower + higher) // 2

        if array[mid] <= value < array[mid + 1]:
            return mid
        elif array[mid] < value:
            lower = mid + 1
        else:
            higher = mid - 1


def return_left_value(array, array_to_check, index):
    while index >= 0 and findIndex(array_to_check, array[index]) >= 0:
        index -= 1
    return index


def return_right_value(array, array_to_check, index):
    while index < len(array) - 2 and findIndex(array_to_check, array[index]) >= 0:
        index += 1
    return index


def map_lower_and_higher_nearest(array, number_of_nears, lower_index, higher_index, value):
    result_array = []
    while len(result_array) < number_of_nears and (lower_index >= 0 and higher_index < len(array)):  #
        if value - array[lower_index] <= array[higher_index] - value:
            # Prevent duplicated values
            left = return_left_value(array, result_array, lower_index)
            result_array.append(array[left])
            lower_index = left - 1
        else:
            right = return_right_value(array, result_array, higher_index)
            result_array.append(array[right])
            higher_index = right + 1

    while len(result_array) < number_of_nears and lower_index >= 0:
        left = return_left_value(array, result_array, lower_index)
        result_array.append(array[left])
        lower_index = left - 1

    while len(result_array) < number_of_nears and higher_index < len(array):
        right = return_right_value(array, result_array, higher_index)
        result_array.append(array[right])
        higher_index = right + 1

    return result_array


def get_nearest_values(list, number_of_nears, value):
    if len(list) <= number_of_nears:
        number_of_nears = len(list)
    new_list = [*list]
    mergeSort(new_list)
    if len(new_list) > 1:
        lower_index = search_lower_index(new_list, 0, len(new_list) - 1, value)
        higher_index = lower_index + 1
        result = map_lower_and_higher_nearest(new_list, number_of_nears, lower_index, higher_index, value)
        print(lower_index, result)


entrada = [5, 3, 8, 7, 1, 4, 5]
k = 3
V = 6

get_nearest_values(entrada, k, V)




# O(n)
def findIndex(array, value):
    try:
        return array.index(value)
    except ValueError:
        return -1


# O(n)
def return_left_value(array, array_to_check, index):
    while index >= 0 and findIndex(array_to_check, array[index]) >= 0:
        index -= 1
    return index


# O(n)
def return_right_value(array, array_to_check, index):
    while index < len(array) - 2 and findIndex(array_to_check, array[index]) >= 0:
        index += 1
    return index


def map_lower_and_higher_nearest(array, number_of_nears, lower_index, higher_index, value):
    result_array = []
    while len(result_array) < number_of_nears and (lower_index >= 0 and higher_index < len(array)):  # O(n)
        if value - array[lower_index] <= array[higher_index] - value:
            # Prevent duplicated values
            left = return_left_value(array, result_array, lower_index) # O(n)
            result_array.append(array[left])
            lower_index = left - 1
        else:
            right = return_right_value(array, result_array, higher_index)
            result_array.append(array[right])
            higher_index = right + 1

    while len(result_array) < number_of_nears and lower_index >= 0:
        left = return_left_value(array, result_array, lower_index)
        result_array.append(array[left])
        lower_index = left - 1

    while len(result_array) < number_of_nears and higher_index < len(array):
        right = return_right_value(array, result_array, higher_index)
        result_array.append(array[right])
        higher_index = right + 1

    return result_array

