import requests
import pprint
from bs4 import BeautifulSoup
# import bs4 as bs

url = ("https://www.imdb.com/india/top-rated-indian-movies/")
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
div = soup.find('div', class_='lister')
tbody = div.find('tbody',class_='lister-list')
tr = tbody.find_all('tr')
# print(tr)

def scrape_top_list():
    movie_list = []
    year_list = []
    pos_list = []
    url_list = []
    rating_list = []
    position = 1
    for i in tr:
         
        movie_year = i.find('td', class_='titleColumn').span.get_text()
        
        year_list.append(movie_year)



        title_colomn = i.find('td',class_='titleColumn').get_text().strip()
        
        movie_name = i.find('td', class_='titleColumn').a.get_text()
        movie_url = i.find('td', class_='titleColumn').a['href']
        imdb_link = ("https://www.imdb.com")
        # print(imdb_link + movie_url)
        url_list.append(imdb_link + movie_url)

        rating = i.find('td', class_='ratingColumn imdbRating').get_text().strip()
        rating_list.append(rating)
        # print(rating[0:3])

        movie_list.append(movie_name)
        pos_list.append(position)
        position = position + 1
               
    # print(movie_list)
    # print(year_list)
    movie_year = []
    for j in year_list:
        j = j.replace("(", '')
        j = j.replace(")", "")
        movie_year.append(j)
    # print(movie_year)
    # print(pos_list)
    # pprint.pprint(url_list)
    # print(rating_list)

    top_movies_list = []
    for index in range(len(pos_list)):
        small_dic = {}
        small_dic["movie_name"]=(movie_list[index])
        small_dic['year'] = movie_year[index]
        small_dic['position'] = pos_list[index]
        small_dic['rating'] = rating_list[index]
        small_dic['url'] = url_list[index]
        top_movies_list.append(small_dic)   
    return top_movies_list
my_data = scrape_top_list()



