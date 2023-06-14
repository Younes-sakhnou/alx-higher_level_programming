#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        max_int = list(my_dict.keys())[0]
        for key in my_dict:
            if my_dict[key] > my_dict[max_int]:
                max_int = key
        return max_int
    return None
