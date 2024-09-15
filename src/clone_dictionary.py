def clone_dictionary(target_dict, source_dict):
    for key in source_dict:
        target_dict[key] = source_dict[key]
    return target_dict