import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(in_file: str, out_file: str) -> None:
    data = []
    with open(in_file) as f1:
        reader = csv.DictReader(f1, quotechar='\n')
        for row in reader:
            data.append(row)
    with open(out_file, 'w') as f2:
        json.dump(data, f2, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
