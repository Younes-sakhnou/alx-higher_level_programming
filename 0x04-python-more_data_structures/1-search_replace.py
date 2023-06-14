#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_List = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_List.append(replace)
        else:
            new_List.append(my_list[i])
    return new_List
