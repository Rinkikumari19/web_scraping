# from task5_top_ten_movie import *
from task1_top_movie import *
from task4_seprate_data_scrape import *
# pprint.pprint(seprate_movie_data)
# pprint.pprint(my_data)

def  get_movie_list_details(movie_list):
    url_list1 = []
    for index_url in movie_list[:50]:
        url_list1.append(index_url['url'])
    # print(url_list1)
    top_ten_movies_list = []
    for index_top_ten_movies in url_list1:
        # print(scrape_movie_details(index_top_ten_movies))
        data = (scrape_movie_details(index_top_ten_movies))
        top_ten_movies_list.append(data)
    return(top_ten_movies_list)
ten_movies_list = get_movie_list_details(my_data)



def analyse_language_and_directors(movies_list):
    big_dic = {}
    for index in movies_list:
        for dir_name in index['director']:
            big_dic[dir_name] = {}
    for index1 in range(len(movies_list)):
        for dir_name in big_dic:
            if dir_name in movies_list[index1]['director']:
                for lan_1 in movies_list[index1]['language']:
                    big_dic[dir_name][lan_1] = 0
    # print(big_dic)
    for index1 in range(len(movies_list)):   
        for dir_name in big_dic:
            if dir_name in movies_list[index1]['director']:
                for lan_1 in movies_list[index1]['language']:
                    big_dic[dir_name][lan_1] += 1 
    # pprint.pprint(big_dic)
    return (big_dic)

dir_lang = analyse_language_and_directors(ten_movies_list)
print(len(dir_lang))


