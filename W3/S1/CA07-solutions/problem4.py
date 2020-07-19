

def flip_list(my_list):
    result_list = []

    if list == []:
        return list()
    elif isinstance(my_list[0], list):
        # Vertical list
        for i in my_list:
            result_list.append(i[0])
        return result_list
    else:
        # Horizontal list
        for i in my_list:
            i_list = []
            i_list.append(i)
            result_list.append(i_list)

        return result_list


horizontal_list = [1, 2, 3]
vertical_list = [[1], [2], [3]]

print(flip_list(horizontal_list))
print(flip_list(vertical_list))
