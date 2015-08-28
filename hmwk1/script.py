from urllib2 import Request, urlopen

import json

import time

import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" )


API_KEY = ''
#QUESTION : should I be returning the dupSet instead of passing it in and out?
#QUESTION : there is a 	total_pages attribute, is that worth checking?
def findKeywordinTitle(querySearch, dupSet):
	pageNum = 1
	entries = 0

	headers = {'Accept': 'application/json'}

	with open('movie_ID_name.txt', 'w') as f:
		while entries < 300:
			request = Request('http://api.themoviedb.org/3/search/movie?api_key='+API_KEY+'&query='+querySearch+'&page='+str(pageNum), headers=headers)
			response_body = urlopen(request)
			values = json.load(response_body)
			response_body.close()
			for y in values['results']:
				currID = y['id']
				currTitle = y['title']
				if currID not in dupSet and querySearch in currTitle.lower():
					dupSet.add(currID)
					f.write('<{}, {}>\n'.format(currID, currTitle))
					entries += 1
					if entries >= 300:
						break
			pageNum += 1

def similarMovies(movieSet, similarSet):

	headers = {'Accept': 'application/json'}

	with open('movie_ID_sim_movie_ID.txt', 'w') as f:
		for id in movieSet:
			time.sleep(.3)
			pageNum = 1
			currSimilar = 0
			while currSimilar < 5:
				request = Request('http://api.themoviedb.org/3/movie/'+str(id)+'/similar?api_key='+API_KEY+'&page='+str(pageNum), headers=headers)
				response_body = urlopen(request)
				values = json.load(response_body)
				response_body.close()
				if pageNum < values['total_pages']:
					for y in values['results']:
						currSimilarID = y['id']
						tempTuple = None
						if currSimilarID < id:
							tempTuple = (currSimilarID, id)
						elif id < currSimilarID:
							tempTuple = (id, currSimilarID)
						if tempTuple is not None:
							if currSimilar < 5:
								currSimilar += 1
								if tempTuple not in similarSet:
									similarSet.add(tempTuple)
									f.write('<{}, {}>\n'.format(tempTuple[0], tempTuple[1]))
							elif currSimilar >= 5:
								break
					pageNum+=1
				else:
					break



if __name__ == '__main__':
	querySearch = 'life'
	dupSet = set()
	findKeywordinTitle(querySearch, dupSet)
	similarSet = set()
	similarMovies(dupSet, similarSet)