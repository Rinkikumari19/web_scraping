from task12_cast_imdb_id import *
from task4_seprate_data_scrape import *

cast_list = []
url2 = ("fullcredits?ref_=tt_cl_sm#cast")
for id_cast in my_data:
    all_cast_url = (id_cast['url'] + url2)
    cast_list.append(all_cast_url)
# print(cast_list)

def  get_movie_list_details(movie_list):
    url_list1 = []
    for index_url in movie_list[:5]:
        url_list1.append(index_url['url'])
    # print(url_list1)
    top_ten_movies_list = []
    i_cast_list = 0
    for index_top_ten_movies in url_list1:
        dic3 = {}
        # print(scrape_movie_details(index_top_ten_movies))
        data = (scrape_movie_details(index_top_ten_movies))
        while i_cast_list < len(cast_list):
            data2 = scrape_movie_cast(cast_list[i_cast_list])
            i_cast_list = i_cast_list + 1

            break
        dic3.update({"cast":data2})
        data.update(dic3)
        top_ten_movies_list.append(data)
    return(top_ten_movies_list)
cast_movies_list = get_movie_list_details(my_data)
# pprint.pprint(ten_movies_list)











