import requests
import re
import imdb
import webbrowser

ia = imdb.IMDb()
top250_url = "http://akas.imdb.com/chart/top"
 
def get_top250():
	r = requests.get(top250_url)
    	html = r.text.split("\n")
   	result = []
    	for line in html:
        	line = line.rstrip("\n")
        	m = re.search(r'data-titleid="tt(\d+?)">', line)
        	if m:
           	_id = m.group(1)
            	result.append(_id)
   	return result
	
for movie_id in get_top250():
	the_matrix = ia.get_movie(movie_id)
	print(the_matrix['title'])
	print(the_matrix['year'])
	print(the_matrix.summary())
	webbrowser.open(the_matrix['cover url'])
	print('\n')
