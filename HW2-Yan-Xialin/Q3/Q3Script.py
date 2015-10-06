import csv
import json
import os
import operator

csvfile = open('arsenal_players.csv', 'r')
q = open('arsenal_players.csv', 'r')
jsonfile = open('afc.json', 'w')

reader = csv.DictReader(csvfile)
jsonfile.write('{"nodes":[')


temp_list = []
for derpy in reader:
    temp_dict = {}
    temp_dict['name'] = derpy['NAME']
    temp_dict['position'] = derpy['POSITION']
    temp_dict['appearances'] = int(derpy['APPEARANCES'])
    temp_dict['goals'] = int(derpy['GOALS'])
    temp_dict['START_SEASON'] = int(derpy['START_SEASON'])
    temp_dict['END_SEASON'] = int(derpy['END_SEASON'])
    temp_list.append(temp_dict)

sorted_list = sorted(temp_list, key=lambda t: (-t['appearances'], t['name'].lower()))
sorted_list = sorted_list[:50]

for i in range(0,50):
	jsonfile.write('\n{"name":"'+sorted_list[i]['name']+'","position":"'+sorted_list[i]['position']+'","appearances":'+str(sorted_list[i]['appearances'])+',"goals":'+str(sorted_list[i]['goals'])+'},')

jsonfile.close()

with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open('afc.json', 'a') as filehandle:
    filehandle.write(']}')


# print(data['nodes'][0]['START_SEASON'])
with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()

with open('afc.json', 'a') as filehandle:
    filehandle.write(',' + '\n' +'"links":[')
    for x in range (0, 50):
		for y in range(x, 50):
			if(x!=y and sorted_list[x]['START_SEASON'] <= sorted_list[y]['END_SEASON'] and sorted_list[y]['START_SEASON'] <= sorted_list[x]['END_SEASON']):
				# print(data['nodes'][x]['START_SEASON'] + " " + data['nodes'][x]['END_SEASON'] + "\n");
				# print(data['nodes'][y]['START_SEASON'] + " " + data['nodes'][y]['END_SEASON'] + "\n");
				startDate = int(max(sorted_list[x]['START_SEASON'], sorted_list[y]['START_SEASON']));
				endDate = int(min(sorted_list[x]['END_SEASON'], sorted_list[y]['END_SEASON']));
				tempValue = endDate-startDate+1
				# print(str(startDate) + " " + str(endDate) + " " + str(tempValue) + "\n")
				filehandle.write('\n{"source":' + str(x) + ',"target":' + str(y) + ',"value":' + str(tempValue) + '},')


with open('afc.json', 'rb+') as filehandle:
    filehandle.seek(-1, os.SEEK_END)
    filehandle.truncate()


with open('afc.json', 'a') as filehandle:
    filehandle.write('\n]}')

