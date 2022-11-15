import json
import pandas as pd
import subprocess
import sys

def revisions(filename):
	output = subprocess.check_output(['git', 'log', '--pretty=%H %ct %ci', filename])
	lines = output.decode('UTF-8').rstrip().split("\n")
	return [
		line.split(" ", 2) for line in lines
	]

def getrevision(filename, ref):
	output = subprocess.check_output(['git', 'show', f'{ref}:{filename}'])
	return output.decode('UTF-8').rstrip()

def recurse(data: dict, value, prefix = ''):
	if isinstance(value, dict):
		if prefix:
			prefix = prefix + "."

		for key, val in value.items():
			recurse(data, val, f"{prefix}{key}")

	elif isinstance(value, list):
		if prefix:
			prefix = prefix + "."

		for idx, val in enumerate(value):
			recurse(data, val, f"{prefix}{idx}")

	else:
		data[prefix] = value

def parse(data: dict):
	result = {}
	recurse(result, data)
	return result

revs = reversed(revisions(sys.argv[1]))
rows = []

for rev in revs:
	ref, timestamp, rfcdate = rev

	txt = getrevision(sys.argv[1], ref)
	js = json.loads(txt)

	item = parse(js)

	rows.append({
		'captureTimestamp': timestamp,
		'captureDateTime': rfcdate,
		'captureRevision': ref,
		**item
	})

df = pd.DataFrame.from_records(rows)
df.to_csv(sys.argv[2], index=False)