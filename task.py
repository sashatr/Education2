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
    return person


def prep_data(person_dict):
    try:
        data = json.load(open('persons.json'))
    except:
        data = []

    data.append(person_dict)
    return data


def write_json(data):
    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def main():
    for i in range(5):
        write_json(prepd_data(gen_person()))








if __name__ == '__main__':
    main()


