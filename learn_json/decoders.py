import json


def main():
    with open('persons.json', 'r') as data:
        res = json.load(data)

    print(type(data))
    print(type(res))
    print(res)


if __name__ == '__main__':
    main()
