# 1) Dona Maria é viciada em potes plásticos. Sua coleção cresce semanalmente, e
# atualmente está toda bagunçada, os potes estão sem a referida tampa. Ajude-a na
# organização associando os P potes de tamanhos diferentes às N tampas
# correspondentes. Você pode testar um pote e uma tampa juntos, no qual você pode
# verificar se o pote é maior, menor ou corresponde exatamente à tampa. No entanto,
# não há como comparar dois potes juntos ou duas tampas juntas. O problema é
# combinar cada pote a sua tampa. Implemente um algoritmo para esse problema com
# custo médio de (n log n). Justifique a complexidade do algoritmo proposto.

Panelas = [1, 5, 99, 20, 2, 3, 4, 6, 6, 10]
Tampas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 99]


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


def matchPanAndCover(pan, cover):
    # When pan matches cover
    pan_cover = []

    # Pan without cover
    pan_without_cover = []

    # Create a new array equal the cover, but with other memory address usage to modify this array
    cover_sorted = [*cover]
    # Sort the cover array
    mergeSort(cover_sorted)  # O(nlogn)

    # Manage the cover array sorted
    cover_size = len(cover_sorted)
    mid_cover_index = cover_size // 2
    mid_cover_value = cover_sorted[mid_cover_index]
    cover_left = cover_sorted[:mid_cover_index]
    cover_right = cover_sorted[mid_cover_index + 1:]

    # Avoid use the same mid_cover_value for two different pans
    is_mid_cover_value_used = False

    # This FOR has a complexity O(n*log(n)). It's log(n) because we divide the covers array in the middle
    # and when a cover matches a pan we delete the param from the cover array (cover_left or cover_right)
    for p in range(len(pan)):
        pan_value = pan[p]

        if pan_value == mid_cover_value and is_mid_cover_value_used is False:
            pan_cover.append([pan_value, mid_cover_value])
            is_mid_cover_value_used = True

        elif pan_value <= mid_cover_value:
            index = findIndex(cover_left, pan_value)
            if index >= 0:
                pan_cover.append([pan_value, cover_left[index]])
                cover_left.pop(index)
            else:
                pan_without_cover.append(pan_value)

        elif pan_value >= mid_cover_value:
            index = findIndex(cover_right, pan_value)
            if index >= 0:
                pan_cover.append([pan_value, cover_right[index]])
                cover_right.pop(index)
            else:
                pan_without_cover.append(pan_value)

        else:
            pan_without_cover.append(pan_value)

    # Cover's array that don't have the pan
    cover_array_without_pan = [*cover_left, *cover_right]

    print("Pan that matched with Cover:", pan_cover)
    print("Pan without cover:", pan_without_cover)
    print("Covers without pan:", cover_array_without_pan)


matchPanAndCover(Panelas, Tampas)  # Complexity is O(nlogn)


# 2) Implemente um algoritmo que retorne o I itens mais próximos de um valor V, para um
# vetor qualquer de elementos inteiros. V pode estar ou não presente no vetor. Sua
# solução deve ser O(nlogn).

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
        mid = lower + higher // 2

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


entrada = [5, 5, 5, 4, 5, 3, 2, 1]
k = 7
V = 6

get_nearest_values(entrada, k, V)
