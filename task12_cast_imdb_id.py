from task1_top_movie import *
import json
import os.path

cast_list = []
url2 = ("fullcredits?ref_=tt_cl_sm#cast")
for id_cast in my_data:
    all_cast_url = (id_cast['url'] + url2)
    cast_list.append(all_cast_url)
# pprint.pprint(cast_list)

def scrape_movie_cast(movie_caste_url):
    response = requests.get(movie_caste_url)
    soup = BeautifulSoup(response.text,'html.parser')
    table = soup.find('table', class_='cast_list')

    tr1 = table.find_all('tr', class_='odd')
    tr2 = table.find_all('tr', class_='even')
    imdb_list = []
    
    for i_tr1 in tr1:
        imdb_dic= {}
        td = i_tr1.find('td', class_='primary_photo').a['href']
        imdb_id = (td[6:-1])
        # print(imdb_id)
        name = i_tr1.find('td', class_='primary_photo').img['alt']
        # print(name)
        imdb_dic['imdb_id'] = imdb_id
        imdb_dic['name'] = name
        imdb_list.append(imdb_dic)

    for i_tr2 in tr2:
        imdb_dic= {}
        name = i_tr2.find('td', class_='primary_photo').img['alt']
        # print(name)
        td = i_tr2.find('td', class_='primary_photo').a['href']
        imdb_id = (td[6:-1])
        # print(imdb_id)

        imdb_dic['imdb_id'] = imdb_id
        imdb_dic['name'] = name
        imdb_list.append(imdb_dic)
    return(imdb_list)
cast_data = scrape_movie_cast("https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast")


def cast_caching():
    for id in cast_list:
        url_id =(id[27:36])
        # print(url_id)
        exists = os.path.exists('cast_imdb_id/'+url_id+"cast"+'.json')
        if exists:
            with open ('cast_imdb_id/'+url_id+"cast"+'.json', 'r') as id_file:
                id_data = id_file.read()
                return(id_data)
        else:
            id_response = requests.get(id)
            with open('cast_imdb_id/'+url_id+"cast"+'.json', 'w') as id_file:
                seprate_cast_id = scrape_movie_cast(id)
                json.dump(seprate_cast_id, id_file)
                return(seprate_cast_id)
            
cast_caching()