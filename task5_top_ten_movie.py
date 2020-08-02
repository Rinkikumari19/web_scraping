from task1_top_movie import *
# pprint.pprint(my_data)
from task4_seprate_data_scrape import *
# print(seprate_movie_data)
# pprint.pprint(my_data)

def  get_movie_list_details(movie_list):
    url_list1 = []
    for index_url in movie_list[:10]:
        url_list1.append(index_url['url'])
    # print(url_list1)
    top_ten_movies_list = []
    for index_top_ten_movies in url_list1:
        # scrape_movie_details(index_top_ten_movies)
        data = (scrape_movie_details(index_top_ten_movies))

        top_ten_movies_list.append(data)
    return(top_ten_movies_list)

ten_movies_list = get_movie_list_details(my_data)