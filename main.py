
import pymysql
from urllib3 import connection_from_url


def read_data_file(file_name):
    file_lines = []
    file = open(file_name,'r')
    for line in file:
        file_lines.append(line)
    return file_lines
def split_line(line):
    splited_line = line.split(';')
    return splited_line

def connect_to_db(host,user,port,db_name,password):
    connection = pymysql.connect(host=host,user=user,port=port,db=db_name,password=password)
    cursor=connection.cursor()
    return cursor,connection


if __name__ == '__main__':
    cursor, connection = connect_to_db('192.168.1.7','student',3306,'test','123456')
    connection.commit()
    stroki_iz_faila = read_data_file('data.csv')

    for stroka in stroki_iz_faila:
        razbitay_stroka = split_line(stroka)
        cursor.execute("insert into sprav values('{}', '{}', '{}', '{}', '{}');".format(razbitay_stroka[0], razbitay_stroka[1],razbitay_stroka[2],razbitay_stroka[3],razbitay_stroka[4].strip()))
    connection.commit()
