def convert_list(cast_type, origin_list):
    if isinstance(origin_list, list):
        return [convert_list(cast_type, i) for i in origin_list]
    else:
        return cast_type(origin_list)
