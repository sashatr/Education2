import socket
import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['q', 'w', 'r', 'y', 't', 'l', 'o', 'h', 'g']         # ...
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 5:
        name += choice(letters)
        tel += choice(nums)

    person = {
        'name': name.capitalize(),
        'tel': tel
    }
    data_ = [person]
    return data_


def write_json(data_):
    json_data = json.dumps(data_)
    data_file = open('data.json', 'w')
    data_file.write(json_data)
    data_file.close()

    return data_file


data = write_json(gen_person())


print(type(data))

conn = socket.socket()
conn.connect(('127.0.0.1', 15010))
conn.send(data)


conn.close()
