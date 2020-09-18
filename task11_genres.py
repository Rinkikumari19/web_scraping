# from task5_top_ten_movie import *
# pprint.pprint(ten_movies_list)

# def analyse_movies_genre(movies_list):
#     genre_dic = {}
#     for i_genre in movies_list:
#         list_genre = i_genre['genres']
#         for index_genre in list_genre:
#             if index_genre in genre_dic:
#                 genre_dic[index_genre] += 1
#             else:
#                 genre_dic[index_genre] = 1
#     pprint.pprint(genre_dic)

# analyse_movies_genre(ten_movies_list)




# ==========OR===========#



from task1_top_movie import *
from task4_seprate_data_scrape import *
def  get_movie_list_details(movie_list):
    url_list1 = []
    for index_url in movie_list:
        url_list1.append(index_url['url'])
    top_ten_movies_list = []

    for index_top_ten_movies in url_list1:
        data = (scrape_movie_details(index_top_ten_movies))
        top_ten_movies_list.append(data)
    return(top_ten_movies_list)

ten_movies_list = get_movie_list_details(my_data)

def analyse_movies_genre(movies_list):
    genre_dic = {}
    for i_genre in movies_list:
        list_genre = i_genre['genres']
        for index_genre in list_genre:
            if index_genre in genre_dic:
                genre_dic[index_genre] += 1
            else:
                genre_dic[index_genre] = 1
    pprint.pprint(genre_dic)

analyse_movies_genre(ten_movies_list)
