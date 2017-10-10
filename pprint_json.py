import json


def load_data(filepath):
    f = open(filepath, "r", encoding="utf8")
    pretty_print_json(json.loads(f.read()))
    f.close()


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_filepath = input('Input a path to json-file:')
    load_data(json_filepath)

