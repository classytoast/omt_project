

def create_dataclasses(data, dc):
    objects = []
    for count in range(len(data)):
        obj = dict(data[count])
        obj_with_true_fields = {}
        for field in obj:
            if field not in ('file_path',):
                obj_with_true_fields[field] = obj[field]
        objects.append(dc(**obj_with_true_fields))

    return objects