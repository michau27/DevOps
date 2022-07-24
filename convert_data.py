with open('data.txt', 'r') as txt_file:
    lines = txt_file.readlines()

for idx, item in enumerate(lines):
    lines[idx] = item.split(';', 1)[1]
    print(lines[idx])

with open('/output/converted_data.txt', 'w') as txt_file:
    txt_file.writelines(lines)
