def find_my_list(all_lists, my_list):
    for index, lst in enumerate(all_lists):
        # Change the next line
        if my_list is lst:
            return index
    return None
