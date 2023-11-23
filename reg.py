def original_name():
    name = input()
    name_list = []
    while name != '':
        if name in name_list:
            name += '1'
        name_list.append(name)
        name = input()
        print(name_list)
original_name()