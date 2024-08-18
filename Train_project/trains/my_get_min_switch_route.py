import itertools

def modify_combinations(combos):
    modified_combos = []
    for combo in combos:
        # Start with the first pair, converting it to a list for modification
        modified_list = [list(combo[0])]
        for i in range(1, len(combo)):
            if combo[i][0] == modified_list[-1][0]:
                # Update the last element of the last pair in modified_list
                modified_list[-1][3] = combo[i][3]
            else:
                # Convert the current tuple to a list before appending
                modified_list.append(list(combo[i]))
        # Convert modified lists back to tuples before appending to modified_combos
        modified_combos.append([tuple(item) for item in modified_list])
    return modified_combos


def get_min_switch_route(list_of_lists):
    # Generate all combinations
    merged_list_of_trains_for_all_paths = []
    for list_of_trains_for_path1 in list_of_lists:
        combinations = list(itertools.product(*list_of_trains_for_path1))

        # Convert tuples to lists of tuples
        combinations = [list(item) for item in combinations]
        
        # Modify the combinations
        modified_combinations = modify_combinations(combinations)
       
        merged_list_of_trains_for_all_paths += (modified_combinations)

    # Determine the minimum size of the modified lists
    if(len(merged_list_of_trains_for_all_paths)==0):
        return [[]]
    min_size = min(len(combo) for combo in merged_list_of_trains_for_all_paths)
    # Filter out lists with the minimum size
    min_size_combinations = [combo for combo in merged_list_of_trains_for_all_paths if len(combo) == min_size]
     

    return min_size_combinations

