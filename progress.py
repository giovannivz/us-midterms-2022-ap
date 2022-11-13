import json
import os
import os.path
import subprocess

js = json.load(open('AP/progress.json'))
urls = open('updated-urls.txt', 'w')

for key, race in js.items():
	path = f'AP/{key}'

	if not os.path.exists(path):
		os.mkdir(path)

	tspath = f'AP/{key}/timestamp'
	timestamp = None

	if os.path.exists(tspath):
		ts = open(tspath)
		timestamp = ts.read()
		ts.close()

	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{race['statePostal']}/{race['raceID']}/detail.json\n")
	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{race['statePostal']}/{race['raceID']}/metadata.json\n")
	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{race['statePostal']}/{race['raceID']}/summary.json\n")
