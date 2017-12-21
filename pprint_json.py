import json


def load_data(json_filepath):
    with open(json_filepath) as json_file:
        return json.loads(json_file.read())


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_filepath = input('Input a path to json-file:')
    loaded_data = load_data(json_filepath)
    pretty_print_json(loaded_data)
