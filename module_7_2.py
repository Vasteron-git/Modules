
def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    number_string = 0
    dict = {}
    for str in strings:
        number_string += 1
        start_number_byte = file.tell()
        file.write(str + '\n')
        dict[(number_string, start_number_byte)] = str
    file.close()
    return dict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
