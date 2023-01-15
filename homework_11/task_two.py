class TextUp:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        upper_cased_string = self._func(*args, **kwargs).upper()
        return upper_cased_string


@TextUp
def get_text(list_of_items):
    result_string = ' '.join(list_of_items)
    return result_string


print(get_text(['hello', 'world', 'i', 'am', 'upper cased']))
