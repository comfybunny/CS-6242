import csv
import json
import os

csvfile = open('unhcr_persons_of_concern.csv', 'rU')
jsonfile = open('poc.json', 'w')

fieldnames = ("Year","Country / territory of asylum/residence","Origin","Refugees (incl. refugee-like situations)","Asylum-seekers (pending cases)","Returned refugees","Internally displaced persons (IDPs)","Returned IDPs","Stateless persons","Others of concern","Total Population")
reader = csv.DictReader( csvfile, fieldnames)
jsonfile.write('[')
for row in reader:
	jsonfile.write('\n')
	json.dump(row, jsonfile)
	jsonfile.write(',')

jsonfile.close()

with open('poc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open('poc.json', 'a') as filehandle:
    filehandle.write(']')
