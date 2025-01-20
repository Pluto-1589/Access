import math


def zoo(number):
    return (math.floor(number), math.ceil(number), math.atan(number), math.modf(number), math.nextafter(number, -math.inf), math.cbrt(number))


print(zoo(-23.6))

"""def zoo(number):
    return (
        floor(number),
        ceil(number),
        atan(number),
        modf(number),
        nextafter(number, -inf),
        cbrt(number)
    )"""
