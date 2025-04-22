
import lvgl as lv

member_name_cache = {}

def get_event_name(obj, value):
    try:
        return member_name_cache[id(obj)][id(value)]
    except KeyError:
        pass

    for member in dir(obj):
        if getattr(obj, member) == value:
            try:
                member_name_cache[id(obj)][id(value)] = member
            except KeyError:
                member_name_cache[id(obj)] = {id(value): member}
            return member