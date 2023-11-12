import json


def task(filename: str) -> float:
    with open(filename, 'r') as file:
        data = json.load(file)
    return round(sum([i['score'] * i['weight'] for i in data]), 3)


print(task('input.json'))
