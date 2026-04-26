def read_data_file(file_name):
    file_lines = []
    file = open(file_name,'r')
    for line in file:
        file_lines.append(line)
    return file_lines
def split_line(line):
    splited_line = line.split(';')
    return splited_line

if __name__ == '__main__':
    stroki_iz_faila = read_data_file('data.csv')
    #print(stroki_iz_faila)
    for stroka in stroki_iz_faila:
        razbitay_stroka = split_line(stroka)
        print(razbitay_stroka)
        print(f'Мое имя {razbitay_stroka[0]} {razbitay_stroka[1]}, мой пол - {razbitay_stroka[2]}, год моего рождения {razbitay_stroka[3]}-й, мой контактный телефон - {razbitay_stroka[4]}')

