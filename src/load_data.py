import sys
import json



def load(filename):
    try:
        f = open(f"data/{filename}","r")
    except OSError:
        print(f"Невозможно открыть файл:{filename}")
        sys.exit()
    json_input = f.read()
    data_json = json.loads(json_input)
    return data_json