
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(i[0]) - len(i[1]) for i in list(zip(first,second)) if len(i[0]) != len(i[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))
print(list(first_result))
print(list(second_result))
print(list(zip(first,second)))