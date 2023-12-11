import settings

logger = settings.logger

"""
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


def main():
    data = read_calibration_data()

    calibration_sum = 0

    for calibration_string in data:
        calibration_sum += find_digits_and_create_integer(calibration_string)

    logger.info(calibration_sum)


def find_digits_and_create_integer(calibration_string):

    digits = []
    for i in range(len(calibration_string)):
        if calibration_string[i].isdigit():
            digits.append(calibration_string[i])
            break
        else:
            spelled_out_digit = find_spelled_out_digit(calibration_string[i:])

            if spelled_out_digit is not None:
                digits.append(spelled_out_digit)
                break

    for i in range(len(calibration_string) - 1, -1, -1):
        if calibration_string[i].isdigit():
            digits.append(calibration_string[i])
            break
        else:
            spelled_out_digit = find_spelled_out_digit(calibration_string[i:])

            if spelled_out_digit is not None:
                digits.append(spelled_out_digit)
                break

    if len(digits) == 0:
        return 0

    return int("".join(digits))


def find_spelled_out_digit(string):
    possible_spelled_out_digits = [
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
        ("zero", "0"),
    ]

    for spelled_out_digit, digit in possible_spelled_out_digits:
        if string.startswith(spelled_out_digit):
            return digit

    return None


def read_calibration_data():
    with open(settings.CALIBRATION_DATA_FILENAME, 'r') as file:
        data = [line.rstrip('\n') for line in file.readlines()]

    return data


if __name__ == "__main__":
    main()


