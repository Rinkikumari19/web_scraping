# from task5_top_ten_movie import *
from task1_top_movie import *
from task4_seprate_data_scrape import *
# pprint.pprint(ten_movies_list)

# def analyse_language_and_directors(movies_list):
#     big_dic = {}
#     for dir_name in movies_list:
#         dir1 = (dir_name['director'][0])
#         lang1 = (dir_name['language'])
#         smoll_dic = {}
#         for mul_lang in lang1:
#             if mul_lang in smoll_dic:
#                 smoll_dic[mul_lang] += 1
#             else:
#                 smoll_dic[mul_lang] = 1
#         big_dic[dir1]=smoll_dic
#     pprint.pprint(big_dic)
# analyse_language_and_directors(ten_movies_list)




def  get_movie_list(movie_list):
    url_list1 = []
    for index_url in movie_list:
        url_list1.append(index_url['url'])
    # print(url_list1)
    top_ten_movies_list = []
    for index_top_ten_movies in url_list1:
        # scrape_movie_details(index_top_ten_movies)
        data = (scrape_movie_details(index_top_ten_movies))
        top_ten_movies_list.append(data)
    pprint.pprint(top_ten_movies_list)

get_movie_list(my_data)