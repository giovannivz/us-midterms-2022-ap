import json
import sys
import csv

def recurse(item, prefix=None):
    if type(item) is dict:
        result = {}

        if item:
            first_key = list(item.keys())[0]

            if first_key.endswith('_id'):
                first_val = list(item.values())[0]
                prefix = f'{prefix}_{first_val}'

        for key in item:
            new_key = f'{prefix}_{key}'
            recursed = recurse(item[key], new_key)

            if type(recursed) is dict:
                for subkey in recursed:
                    result[f'{key}_{subkey}'] = recursed[subkey]
            else:
                result[key] = recursed

        return result

    if item and type(item) is list and type(item[0]) is dict:
        print(f"writing {prefix}.csv")

        fp = None
        writer = None
        keys = []

        for row in item:
            if not row:
                continue

            row = recurse(row, prefix)

            if not fp:
                fp = open(f'{prefix}.csv', 'w')
                writer = csv.writer(fp)
                keys = row.keys()
                writer.writerow(keys)

            writer.writerow([row.get(key, '') for key in keys])

        if fp:
            fp.close()

        return ''

    if type(item) is list:
        return ','.join(item)

    return item

if len(sys.argv) != 2:
    print(f'{sys.argv[0]} file.json')
    sys.exit(1)

# load json file
with open(sys.argv[1], 'r') as f:
    js = json.load(f)
    recurse(js['data']['races'], 'races')
