import csv
import json
import os
import operator

csvfile = open('arsenal_players.csv', 'r')
q = open('arsenal_players.csv', 'r')
jsonfile = open('afc.json', 'w')

reader = csv.DictReader(csvfile)
jsonfile.write('{"nodes":[')

derp = {}

data = {}

for derpy in reader:
	# print(derp[derpy['NAME']]+"\n")
	derp[derpy['NAME']] = int(derpy['APPEARANCES']);
	# print(str(derp[derpy['NAME']])+"\n")

sorted_derp = sorted(derp.items(), key=operator.itemgetter(1,0))

sigh = sorted_derp[-50:]

# print(sigh)

derpsighugh = {}

for iterate in sigh:
	derpsighugh[iterate[0]] = iterate[1]

readerd = csv.DictReader(q)

for i in readerd:
	if i['NAME'] in derpsighugh:
		jsonfile.write('\n')
		json.dump(i, jsonfile)
		jsonfile.write(',')
jsonfile.close()

with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open('afc.json', 'a') as filehandle:
    filehandle.write(']}')

with open('afc.json') as data_file:    
    data = json.load(data_file)

# print(data['nodes'][0]['START_SEASON'])
with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open('afc.json', 'a') as filehandle:
    filehandle.write(',' + '\n' +'"links":[')
    for x in range (0, 50):
		for y in range(x, 50):
			if(x!=y and data['nodes'][x]['START_SEASON'] <= data['nodes'][y]['END_SEASON'] and data['nodes'][y]['START_SEASON'] <= data['nodes'][x]['END_SEASON']):
				# print(data['nodes'][x]['START_SEASON'] + " " + data['nodes'][x]['END_SEASON'] + "\n");
				# print(data['nodes'][y]['START_SEASON'] + " " + data['nodes'][y]['END_SEASON'] + "\n");
				startDate = int(max(data['nodes'][x]['START_SEASON'], data['nodes'][y]['START_SEASON']));
				endDate = int(min(data['nodes'][x]['END_SEASON'], data['nodes'][y]['END_SEASON']));
				tempValue = endDate-startDate+1
				# print(str(startDate) + " " + str(endDate) + " " + str(tempValue) + "\n")
				filehandle.write('\n{"source":' + str(x) + ',"target":' + str(y) + ',"value":' + str(tempValue) + '},')


with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()


with open('afc.json', 'a') as filehandle:
    filehandle.write('\n]}')

