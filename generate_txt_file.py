import random


def make_two_digits(digit):
    if len(str(digit)) == 1:
        digit = '0' + str(digit)
    return digit


hours = []
with open("data.txt", "a") as txt_file:
    for i in range(1, 101):
        while True:
            hour = make_two_digits(random.randint(0, 23))
            minute = make_two_digits(random.randint(0, 59))
            full_hour = str(hour) + ':' + str(minute)
            if full_hour in hours:
                continue
            else:
                hours.append(full_hour)
                txt_file.write(str(i) + ';' + full_hour + ';' + str(random.randint(1,100)) + '\n')
                break
