import json


def load_data(filepath):
    file = open(filepath, "r", encoding="utf8")
    pretty_print_json(json.loads(file.read()))
    file.close()


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_filepath = input('Input a path to json-file:')
    load_data(json_filepath)

