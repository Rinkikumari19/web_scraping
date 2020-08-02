from task5_top_ten_movie import *
# pprint.pprint(ten_movies_list)

def analyse_movies_language(movies_list):
    dic = {}
    for index_lang in movies_list:
        seprate_lang = (index_lang['language'])
        for index1_lang in seprate_lang:
            if index1_lang in dic:
                dic[index1_lang] += 1
            else:
                dic[index1_lang] = 1
    print(dic)

analyse_movies_language(ten_movies_list)
