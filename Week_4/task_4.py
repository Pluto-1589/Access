def hamming_dist(signal_1, signal_2):
    """If one of the Hamming distances cannot be computed because the lengths of corresponding strings differ, your function should return the string "Sensor defect detected" instead.

    Perhaps, one or both sensors lost power during the recording and now you have datasets of different length or two empty datasets. In this case, your function should return the string "Empty signal on at least one of the sensors"."""
    if not signal_1["data"] or not signal_2:
        return "Empty signal on at least one of the sensors"
    else:
        res = []

        for x, y in zip(signal_1["data"], signal_2):
            if len(x) != len(y):
                return "Sensor defect detected"
            else:
                ham_d = sum(a != b for a, b in zip(x, y))

                if ham_d != 0:
                    res.append((x, y, ham_d))
        return res


# signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5], "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
# signal_sensor_2 = ("00101110", "11001001", "11110011","01111011", "11001101", "00011011")

# signal_sensor_3 = {'times': [0, 1, 2], 'data': ['00110101', '01010101', '10001110']}
# signal_sensor_4 = ('00110101', '01010101', '10001110')

signal_sensor_5 = {'times': [0, 1, 2], 'data': [
    '00110101', '10101010', '01111110']}
signal_sensor_6 = ('00110101', '10101010', '00011000')

# print(hamming_dist(signal_sensor_1, signal_sensor_2))
# print(hamming_dist(signal_sensor_3, signal_sensor_4))
# [('01111110', '00011000', 4)]
print(hamming_dist(signal_sensor_5, signal_sensor_6))
