from task1_top_movie import *
from task4_seprate_data_scrape import *
import json
import os.path

def caching():
    for id in my_data:
        url_id =(id['url'][-10:-1])
        exists = os.path.exists('movies_data/'+url_id+'.json')
        if exists:
            with open ('movies_data/'+url_id+'.json', 'r') as id_file:
                id_data = id_file.read()
                return(id_data)
            
        else: 
            id_res = requests.get(id['url'])
            with open('movies_data/'+url_id+'.json', 'w') as id_file:
                seprate_movie_data = scrape_movie_details(id['url'])
                json.dump(seprate_movie_data,id_file)
                # return (seprate_movie_data)
caching()

