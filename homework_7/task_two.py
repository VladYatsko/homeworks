def is_right_triangle(side_one: int, side_two: int, side_three: int):
    result = dict()
    if side_one + side_two < side_three or \
            side_one + side_three < side_two\
            or side_two + side_three < side_one:
        result['result'] = False
        result['description'] = 'no such triangle exists'
    elif side_one**2 + side_two**2 == side_three**2:
        result['result'] = True
        result['description'] = 'the triangle is right-angled'
    else:
        result['result'] = False
        result['description'] = 'the triangle is not right-angled'
    return result


is_triangle = is_right_triangle(11, 11, 21)
print(is_triangle)
