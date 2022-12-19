def text_up(func):
    def wrapper(*args, **kwargs):
        upper_cased_string = func(*args, **kwargs).upper()
        return upper_cased_string
    return wrapper


@text_up
def get_text(list_of_items):
    result_string = ' '.join(list_of_items)
    return result_string


print(get_text(['hello', 'world', 'i', 'am', 'upper cased']))
