import json
import os
import subprocess

js = json.load(open('AP/progress.json'))
urls = open('updated-urls.txt', 'w')

for key, val in js.items():
	os.mkdir(f'AP/{key}')

	ts = open(f'AP/{key}/timestamp')

	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{item['statePostal']}/{item['raceID']}/detail.json")
	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{item['statePostal']}/{item['raceID']}/metadata.json")
	urls.write(f"https://interactives.ap.org/election-results/data-live/2022-11-08/results/races/{item['statePostal']}/{item['raceID']}/summary.json")
